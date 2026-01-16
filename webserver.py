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
    print("\nLocal URL: http://localhost:5000")
    print("\nTo make accessible externally, run in another terminal:")
    print("  ngrok http 5000")
    print("\nThen share the ngrok URL with your son!")
    print("=" * 60 + "\n")

    app.run(host="0.0.0.0", port=5001, debug=False)
