"""Web server for NeilSearch dashboard."""
import os
from flask import Flask, send_file, jsonify, request, Response
from database import Database
from dashboard import generate_dashboard

app = Flask(__name__)

# Get the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DASHBOARD_PATH = os.path.join(BASE_DIR, "dashboard.html")


@app.route("/")
def index():
    """Serve the dashboard."""
    # Regenerate dashboard with latest data
    with Database() as db:
        db.init_db()
        jobs = db.get_jobs()
        stats = db.get_stats()
        profile = db.get_profile() or {}

    html = generate_dashboard(jobs, stats, profile)

    # Save to file
    with open(DASHBOARD_PATH, "w") as f:
        f.write(html)

    # Return with no-cache headers to prevent browser caching
    response = Response(html, mimetype='text/html')
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response


@app.route("/api/stats")
def api_stats():
    """Get job statistics."""
    with Database() as db:
        db.init_db()
        stats = db.get_stats()
    return jsonify(stats)


@app.route("/api/jobs")
def api_jobs():
    """Get all jobs."""
    min_score = request.args.get("min_score", 0, type=int)
    with Database() as db:
        db.init_db()
        jobs = db.get_jobs(min_score=min_score)
    return jsonify(jobs)


@app.route("/api/status", methods=["POST"])
def api_status():
    """Update application status for a job."""
    data = request.get_json()
    job_id = data.get("job_id", "")
    status = data.get("status", "")
    with Database() as db:
        db.init_db()
        if status:
            db.update_application_status(job_id, status)
        else:
            db.delete_application_status(job_id)
    return jsonify({"ok": True})


@app.route("/api/refresh")
def api_refresh():
    """Trigger a job scan (returns immediately, scan runs in background)."""
    import subprocess
    subprocess.Popen(
        ["python", "neilsearch.py", "scan-companies", "--top", "50"],
        cwd=BASE_DIR,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return jsonify({"status": "Scan started", "message": "Refresh the page in a few minutes"})


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("NeilSearch Dashboard Server")
    print("=" * 60)
    print("\nLocal URL: http://localhost:5001")
    print("\nThe server is bound to 0.0.0.0:5001 (accessible from anywhere)")
    print("External URL: http://<your-ip>:5001")
    print("=" * 60 + "\n")

    app.run(host="0.0.0.0", port=5001, debug=False)
