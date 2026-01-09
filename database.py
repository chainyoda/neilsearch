"""Database operations for NeilSearch."""
import sqlite3
import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Any
import config


class Database:
    """Handle all database operations."""

    def __init__(self, db_path: Path = config.DB_PATH):
        """Initialize database connection."""
        self.db_path = db_path
        self.conn = None

    def __enter__(self):
        """Context manager entry."""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()

    def connect(self):
        """Connect to database."""
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row

    def close(self):
        """Close database connection."""
        if self.conn:
            self.conn.close()

    def init_db(self):
        """Initialize database schema."""
        cursor = self.conn.cursor()

        # Jobs table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS jobs (
                id TEXT PRIMARY KEY,
                board_name TEXT NOT NULL,
                company TEXT NOT NULL,
                title TEXT NOT NULL,
                location TEXT,
                description TEXT,
                url TEXT UNIQUE NOT NULL,
                posted_date TEXT,
                scraped_date TEXT NOT NULL,
                match_score REAL,
                match_breakdown TEXT,
                skills_matched TEXT,
                skills_missing TEXT,
                match_explanation TEXT
            )
        """)

        # Application tracking
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS applications (
                job_id TEXT PRIMARY KEY,
                status TEXT NOT NULL,
                notes TEXT,
                status_date TEXT NOT NULL,
                FOREIGN KEY(job_id) REFERENCES jobs(id) ON DELETE CASCADE
            )
        """)

        # Profile storage
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS profile (
                id INTEGER PRIMARY KEY CHECK (id = 1),
                resume_path TEXT,
                last_updated TEXT NOT NULL,
                profile_data TEXT NOT NULL
            )
        """)

        # Scan history
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                scan_date TEXT NOT NULL,
                jobs_found INTEGER NOT NULL,
                boards_scanned INTEGER NOT NULL,
                duration_seconds REAL NOT NULL
            )
        """)

        # Create indexes
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_jobs_match_score ON jobs(match_score DESC)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_jobs_scraped_date ON jobs(scraped_date DESC)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_jobs_company ON jobs(company)")

        self.conn.commit()

    def save_profile(self, resume_path: str, profile_data: Dict):
        """Save or update profile."""
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT OR REPLACE INTO profile (id, resume_path, last_updated, profile_data)
            VALUES (1, ?, ?, ?)
        """, (resume_path, datetime.now().isoformat(), json.dumps(profile_data)))
        self.conn.commit()

    def get_profile(self) -> Optional[Dict]:
        """Get profile data."""
        cursor = self.conn.cursor()
        row = cursor.execute("SELECT * FROM profile WHERE id = 1").fetchone()
        if row:
            return {
                "resume_path": row["resume_path"],
                "last_updated": row["last_updated"],
                "profile_data": json.loads(row["profile_data"])
            }
        return None

    def save_job(self, job_data: Dict) -> bool:
        """Save a job to database. Returns True if new job, False if duplicate."""
        cursor = self.conn.cursor()

        # Check if job already exists
        existing = cursor.execute(
            "SELECT id FROM jobs WHERE url = ?",
            (job_data["url"],)
        ).fetchone()

        if existing:
            return False

        cursor.execute("""
            INSERT INTO jobs (
                id, board_name, company, title, location, description,
                url, posted_date, scraped_date, match_score, match_breakdown,
                skills_matched, skills_missing, match_explanation
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            job_data["id"],
            job_data["board_name"],
            job_data["company"],
            job_data["title"],
            job_data.get("location"),
            job_data.get("description"),
            job_data["url"],
            job_data.get("posted_date"),
            job_data["scraped_date"],
            job_data.get("match_score"),
            json.dumps(job_data.get("match_breakdown", {})),
            json.dumps(job_data.get("skills_matched", [])),
            json.dumps(job_data.get("skills_missing", [])),
            job_data.get("match_explanation")
        ))
        self.conn.commit()
        return True

    def get_jobs(self,
                 min_score: Optional[float] = None,
                 status: Optional[str] = None,
                 days: Optional[int] = None) -> List[Dict]:
        """Get jobs with optional filters."""
        query = """
            SELECT j.*, a.status as app_status, a.notes, a.status_date
            FROM jobs j
            LEFT JOIN applications a ON j.id = a.job_id
            WHERE 1=1
        """
        params = []

        if min_score is not None:
            query += " AND j.match_score >= ?"
            params.append(min_score)

        if status:
            query += " AND a.status = ?"
            params.append(status)

        if days:
            cutoff = (datetime.now() - timedelta(days=days)).isoformat()
            query += " AND j.scraped_date >= ?"
            params.append(cutoff)

        query += " ORDER BY j.match_score DESC, j.scraped_date DESC"

        cursor = self.conn.cursor()
        rows = cursor.execute(query, params).fetchall()

        jobs = []
        for row in rows:
            job = dict(row)
            # Parse JSON fields
            if job["match_breakdown"]:
                job["match_breakdown"] = json.loads(job["match_breakdown"])
            if job["skills_matched"]:
                job["skills_matched"] = json.loads(job["skills_matched"])
            if job["skills_missing"]:
                job["skills_missing"] = json.loads(job["skills_missing"])
            jobs.append(job)

        return jobs

    def update_application_status(self, job_id: str, status: str, notes: str = ""):
        """Update application status for a job."""
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT OR REPLACE INTO applications (job_id, status, notes, status_date)
            VALUES (?, ?, ?, ?)
        """, (job_id, status, notes, datetime.now().isoformat()))
        self.conn.commit()

    def save_scan_history(self, jobs_found: int, boards_scanned: int, duration: float):
        """Save scan history."""
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO scans (scan_date, jobs_found, boards_scanned, duration_seconds)
            VALUES (?, ?, ?, ?)
        """, (datetime.now().isoformat(), jobs_found, boards_scanned, duration))
        self.conn.commit()

    def get_scan_history(self, days: int = 30) -> List[Dict]:
        """Get scan history."""
        cutoff = (datetime.now() - timedelta(days=days)).isoformat()
        cursor = self.conn.cursor()
        rows = cursor.execute("""
            SELECT * FROM scans
            WHERE scan_date >= ?
            ORDER BY scan_date DESC
        """, (cutoff,)).fetchall()
        return [dict(row) for row in rows]

    def clean_old_jobs(self, days: int = config.DATA_RETENTION_DAYS):
        """Delete jobs older than specified days."""
        cutoff = (datetime.now() - timedelta(days=days)).isoformat()
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM jobs WHERE scraped_date < ?", (cutoff,))
        deleted = cursor.rowcount
        self.conn.commit()
        return deleted

    def get_stats(self) -> Dict[str, Any]:
        """Get database statistics."""
        cursor = self.conn.cursor()

        stats = {}

        # Total jobs
        stats["total_jobs"] = cursor.execute("SELECT COUNT(*) FROM jobs").fetchone()[0]

        # Average match score
        result = cursor.execute("SELECT AVG(match_score) FROM jobs WHERE match_score IS NOT NULL").fetchone()
        stats["avg_match_score"] = round(result[0], 1) if result[0] else 0

        # Jobs by status
        status_counts = cursor.execute("""
            SELECT a.status, COUNT(*) as count
            FROM applications a
            GROUP BY a.status
        """).fetchall()
        stats["by_status"] = {row["status"]: row["count"] for row in status_counts}

        # Top companies
        top_companies = cursor.execute("""
            SELECT company, COUNT(*) as count
            FROM jobs
            GROUP BY company
            ORDER BY count DESC
            LIMIT 10
        """).fetchall()
        stats["top_companies"] = [{"company": row["company"], "count": row["count"]} for row in top_companies]

        # Recent scans
        recent_scan = cursor.execute("""
            SELECT * FROM scans
            ORDER BY scan_date DESC
            LIMIT 1
        """).fetchone()
        stats["last_scan"] = dict(recent_scan) if recent_scan else None

        return stats
