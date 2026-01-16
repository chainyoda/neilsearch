"""Generate HTML dashboard for job results."""
import json
from typing import List, Dict
from datetime import datetime
from jinja2 import Template


DASHBOARD_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NeilSearch - AI/ML Job Dashboard</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
            background: #f5f7fa;
            color: #2c3e50;
            padding: 20px;
        }

        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 30px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }

        .header h1 { font-size: 2.5em; margin-bottom: 10px; }
        .header .subtitle { opacity: 0.9; font-size: 1.1em; }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }

        .stat-card {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            text-align: center;
        }

        .stat-card .value {
            font-size: 2.5em;
            font-weight: bold;
            color: #667eea;
            display: block;
        }

        .stat-card .label {
            color: #7f8c8d;
            margin-top: 5px;
            font-size: 0.9em;
        }

        .filters {
            background: white;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 30px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        .filters h3 { margin-bottom: 15px; color: #2c3e50; }

        .filter-group {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin-bottom: 15px;
        }

        .filter-group label {
            display: block;
            margin-bottom: 5px;
            font-weight: 600;
            color: #34495e;
        }

        .filter-group input, .filter-group select {
            width: 100%;
            padding: 8px 12px;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-size: 14px;
        }

        .job-grid {
            display: grid;
            gap: 20px;
        }

        .job-card {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
            border-left: 4px solid #ddd;
        }

        .job-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        }

        .job-card.high-match { border-left-color: #2ecc71; }
        .job-card.medium-match { border-left-color: #f39c12; }
        .job-card.low-match { border-left-color: #95a5a6; }

        .job-header {
            display: flex;
            justify-content: space-between;
            align-items: start;
            margin-bottom: 15px;
        }

        .job-title {
            font-size: 1.3em;
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 5px;
        }

        .job-company {
            color: #667eea;
            font-size: 1.1em;
            margin-bottom: 5px;
        }

        .job-location {
            color: #7f8c8d;
            font-size: 0.9em;
        }

        .match-score {
            font-size: 2em;
            font-weight: bold;
            min-width: 60px;
            text-align: right;
        }

        .match-score.high { color: #2ecc71; }
        .match-score.medium { color: #f39c12; }
        .match-score.low { color: #95a5a6; }

        .job-details {
            margin-top: 15px;
            padding-top: 15px;
            border-top: 1px solid #ecf0f1;
        }

        .match-explanation {
            color: #7f8c8d;
            line-height: 1.6;
            margin-bottom: 10px;
        }

        .skills {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin: 10px 0;
        }

        .skill {
            padding: 4px 12px;
            border-radius: 15px;
            font-size: 0.85em;
            font-weight: 500;
        }

        .skill.matched {
            background: #d5f4e6;
            color: #27ae60;
        }

        .skill.missing {
            background: #fadbd8;
            color: #c0392b;
        }

        .job-actions {
            display: flex;
            gap: 10px;
            margin-top: 15px;
        }

        .btn {
            padding: 8px 16px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 0.9em;
            font-weight: 600;
            transition: opacity 0.2s;
        }

        .btn:hover { opacity: 0.8; }

        .btn-primary {
            background: #667eea;
            color: white;
        }

        .btn-secondary {
            background: #ecf0f1;
            color: #2c3e50;
        }

        .status-select {
            padding: 6px 12px;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-size: 0.9em;
        }

        .analytics {
            background: white;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 30px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        .analytics h3 {
            margin-bottom: 20px;
            color: #2c3e50;
        }

        .charts-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 30px;
            margin-top: 20px;
        }

        .chart-container {
            position: relative;
            height: 300px;
        }

        .no-results {
            text-align: center;
            padding: 60px 20px;
            color: #7f8c8d;
            font-size: 1.2em;
        }

        .expanded-details {
            display: none;
            margin-top: 15px;
            padding: 15px;
            background: #f8f9fa;
            border-radius: 5px;
        }

        .expanded-details.show {
            display: block;
        }

        .match-breakdown {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 15px;
            margin-top: 10px;
        }

        .breakdown-item {
            text-align: center;
            padding: 10px;
            background: white;
            border-radius: 5px;
        }

        .breakdown-item .value {
            font-size: 1.5em;
            font-weight: bold;
            color: #667eea;
        }

        .breakdown-item .label {
            font-size: 0.85em;
            color: #7f8c8d;
            margin-top: 5px;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>NeilSearch Dashboard</h1>
        <div class="subtitle" id="header-subtitle">All Jobs</div>
    </div>

    <div class="stats-grid">
        <div class="stat-card">
            <span class="value" id="stat-total-jobs">{{ stats.total_jobs }}</span>
            <span class="label">Total Jobs</span>
        </div>
        <div class="stat-card">
            <span class="value" id="stat-avg-score">{{ stats.avg_match_score }}</span>
            <span class="label">Avg Match Score</span>
        </div>
        <div class="stat-card">
            <span class="value" id="stat-showing">{{ stats.total_jobs }}</span>
            <span class="label">Showing</span>
        </div>
        <div class="stat-card">
            <span class="value" id="stat-companies">{{ stats.unique_companies }}</span>
            <span class="label">Companies</span>
        </div>
    </div>

    <div class="filters">
        <h3>Filters</h3>
        <div class="filter-group">
            <div>
                <label>Min Match Score</label>
                <input type="range" id="minScore" min="0" max="100" value="0" step="5">
                <span id="minScoreValue">0</span>
            </div>
            <div>
                <label>Search</label>
                <input type="text" id="searchInput" placeholder="Search title, company, skills...">
            </div>
            <div>
                <label>Application Status</label>
                <select id="statusFilter">
                    <option value="">All Statuses</option>
                    <option value="not_applied">Not Applied</option>
                    <option value="applied">Applied</option>
                    <option value="interviewing">Interviewing</option>
                    <option value="rejected">Rejected</option>
                </select>
            </div>
            <div>
                <label>Sort By</label>
                <select id="sortBy">
                    <option value="score">Match Score</option>
                    <option value="date">Date Posted</option>
                    <option value="company">Company Name</option>
                </select>
            </div>
            <div>
                <label>Company</label>
                <select id="companyFilter">
                    <option value="">All Companies</option>
                </select>
            </div>
            <div>
                <label>Sector</label>
                <select id="sectorFilter">
                    <option value="">All Sectors</option>
                </select>
            </div>
            <div>
                <label>Location</label>
                <select id="locationFilter">
                    <option value="">All Locations</option>
                </select>
            </div>
            <div>
                <label>Date Posted</label>
                <select id="dateFilter">
                    <option value="">Any Time</option>
                    <option value="week">Last 7 Days</option>
                    <option value="month">Last 30 Days</option>
                    <option value="quarter">Last 90 Days</option>
                </select>
            </div>
        </div>
        <button class="btn btn-secondary" id="resetFilters" onclick="resetAllFilters()">Reset All Filters</button>
    </div>

    <div class="analytics">
        <h3>Analytics</h3>
        <div class="charts-grid">
            <div class="chart-container">
                <canvas id="companiesChart"></canvas>
            </div>
            <div class="chart-container">
                <canvas id="scoresChart"></canvas>
            </div>
        </div>
    </div>

    <div class="job-grid" id="jobGrid">
        <!-- Jobs will be inserted here by JavaScript -->
    </div>

    <div class="no-results" id="noResults" style="display: none;">
        No jobs match your filters. Try adjusting the criteria.
    </div>

    <script>
        const jobsData = {{ jobs_json|safe }};
        const statsData = {{ stats_json|safe }};

        // Chart instances (for updating) - use var for global scope
        var companiesChart = null;
        var scoresChart = null;

        // Update stats based on filtered jobs
        function updateStats(filteredJobs) {
            console.log('updateStats called with', filteredJobs.length, 'jobs');
            try {
                // Update showing count
                document.getElementById('stat-showing').textContent = filteredJobs.length;

                // Update total jobs (filtered)
                document.getElementById('stat-total-jobs').textContent = filteredJobs.length;

                // Update average score
                if (filteredJobs.length > 0) {
                    const avgScore = filteredJobs.reduce((sum, job) => sum + (job.match_score || 0), 0) / filteredJobs.length;
                    document.getElementById('stat-avg-score').textContent = avgScore.toFixed(1);
                } else {
                    document.getElementById('stat-avg-score').textContent = '0';
                }

                // Update unique companies count
                const uniqueCompanies = new Set(filteredJobs.map(job => job.company).filter(c => c)).size;
                document.getElementById('stat-companies').textContent = uniqueCompanies;
            } catch (err) {
                console.error('Error updating stats:', err);
            }
        }

        // Update charts based on filtered jobs
        function updateCharts(filteredJobs) {
            console.log('updateCharts called with', filteredJobs.length, 'jobs');
            console.log('companiesChart exists:', !!companiesChart);
            console.log('scoresChart exists:', !!scoresChart);
            try {
                // Update companies chart
                const companyCounts = {};
                filteredJobs.forEach(job => {
                    if (job && job.company) {
                        companyCounts[job.company] = (companyCounts[job.company] || 0) + 1;
                    }
                });
                const sortedCompanies = Object.entries(companyCounts)
                    .sort((a, b) => b[1] - a[1])
                    .slice(0, 10);

                if (companiesChart) {
                    companiesChart.data.labels = sortedCompanies.length > 0 ? sortedCompanies.map(c => c[0]) : ['No data'];
                    companiesChart.data.datasets[0].data = sortedCompanies.length > 0 ? sortedCompanies.map(c => c[1]) : [0];
                    companiesChart.update();
                }

                // Update score distribution chart
                const scoreRanges = { '0-60': 0, '60-80': 0, '80-100': 0 };
                filteredJobs.forEach(job => {
                    if (job && typeof job.match_score === 'number') {
                        if (job.match_score < 60) scoreRanges['0-60']++;
                        else if (job.match_score < 80) scoreRanges['60-80']++;
                        else scoreRanges['80-100']++;
                    }
                });

                if (scoresChart) {
                    scoresChart.data.datasets[0].data = [scoreRanges['0-60'], scoreRanges['60-80'], scoreRanges['80-100']];
                    scoresChart.update();
                }
            } catch (err) {
                console.error('Error updating charts:', err);
            }
        }

        // Update header subtitle based on current filters
        function updateSubtitle() {
            const sectorFilter = document.getElementById('sectorFilter').value;
            const companyFilter = document.getElementById('companyFilter').value;
            const locationFilter = document.getElementById('locationFilter').value;

            let parts = [];

            // Sector or default "Jobs"
            if (sectorFilter) {
                parts.push(sectorFilter + ' Jobs');
            } else {
                parts.push('Jobs');
            }

            // Company
            if (companyFilter) {
                parts.push('at ' + companyFilter);
            }

            // Location
            if (locationFilter) {
                parts.push('in ' + locationFilter);
            }

            // Build the sentence
            let subtitle = parts.join(' ');

            // If no filters, show "All Jobs"
            if (!sectorFilter && !companyFilter && !locationFilter) {
                subtitle = 'All Jobs';
            }

            document.getElementById('header-subtitle').textContent = subtitle;
        }

        // Render jobs
        function renderJobs(jobs) {
            const grid = document.getElementById('jobGrid');
            const noResults = document.getElementById('noResults');

            if (jobs.length === 0) {
                grid.style.display = 'none';
                noResults.style.display = 'block';
                return;
            }

            grid.style.display = 'grid';
            noResults.style.display = 'none';

            grid.innerHTML = jobs.map(job => {
                const scoreClass = job.match_score >= 80 ? 'high' :
                                 job.match_score >= 60 ? 'medium' : 'low';
                const cardClass = job.match_score >= 80 ? 'high-match' :
                                job.match_score >= 60 ? 'medium-match' : 'low-match';

                const skillsMatched = (job.skills_matched || []).slice(0, 8);
                const skillsMissing = (job.skills_missing || []).slice(0, 5);

                return `
                    <div class="job-card ${cardClass}" data-job-id="${job.id}">
                        <div class="job-header">
                            <div>
                                <div class="job-title">${job.title}</div>
                                <div class="job-company">${job.company}</div>
                                <div class="job-location">${job.location || 'San Francisco, CA'}</div>
                            </div>
                            <div class="match-score ${scoreClass}">${job.match_score.toFixed(0)}</div>
                        </div>

                        <div class="job-details">
                            <div class="match-explanation">${job.match_explanation || 'No explanation available'}</div>

                            ${skillsMatched.length > 0 ? `
                                <div class="skills">
                                    ${skillsMatched.map(skill => `<span class="skill matched">${skill}</span>`).join('')}
                                </div>
                            ` : ''}

                            ${skillsMissing.length > 0 ? `
                                <div class="skills">
                                    ${skillsMissing.map(skill => `<span class="skill missing">${skill}</span>`).join('')}
                                </div>
                            ` : ''}

                            <div class="expanded-details" id="details-${job.id}">
                                <div class="match-breakdown">
                                    <div class="breakdown-item">
                                        <div class="value">${(job.match_breakdown?.skills || 0).toFixed(0)}</div>
                                        <div class="label">Skills</div>
                                    </div>
                                    <div class="breakdown-item">
                                        <div class="value">${(job.match_breakdown?.role_fit || 0).toFixed(0)}</div>
                                        <div class="label">Role Fit</div>
                                    </div>
                                    <div class="breakdown-item">
                                        <div class="value">${(job.match_breakdown?.company_traits || 0).toFixed(0)}</div>
                                        <div class="label">Company</div>
                                    </div>
                                    <div class="breakdown-item">
                                        <div class="value">${(job.match_breakdown?.experience_level || 0).toFixed(0)}</div>
                                        <div class="label">Experience</div>
                                    </div>
                                </div>
                            </div>

                            <div class="job-actions">
                                <a href="${job.url}" target="_blank" class="btn btn-primary">View Job</a>
                                <button class="btn btn-secondary" onclick="toggleDetails('${job.id}')">Details</button>
                                <select class="status-select" onchange="updateStatus('${job.id}', this.value)">
                                    <option value="">Set Status</option>
                                    <option value="applied">Applied</option>
                                    <option value="interviewing">Interviewing</option>
                                    <option value="rejected">Rejected</option>
                                    <option value="not_interested">Not Interested</option>
                                </select>
                            </div>
                        </div>
                    </div>
                `;
            }).join('');
        }

        function toggleDetails(jobId) {
            const details = document.getElementById(`details-${jobId}`);
            details.classList.toggle('show');
        }

        function updateStatus(jobId, status) {
            console.log(`Update status for ${jobId} to ${status}`);
            // In a real implementation, this would call back to Python to update the database
            alert(`Status updated to: ${status}\\nNote: This is a demo. Status updates aren't persisted in this version.`);
        }

        function resetAllFilters() {
            document.getElementById('minScore').value = 0;
            document.getElementById('minScoreValue').textContent = '0';
            document.getElementById('searchInput').value = '';
            document.getElementById('statusFilter').value = '';
            document.getElementById('sortBy').value = 'score';
            document.getElementById('companyFilter').value = '';
            document.getElementById('sectorFilter').value = '';
            document.getElementById('locationFilter').value = '';
            document.getElementById('dateFilter').value = '';
            filterAndSortJobs();
        }

        // Populate company dropdown
        function populateCompanyDropdown() {
            const companies = [...new Set(jobsData.map(job => job.company))].sort();
            const dropdown = document.getElementById('companyFilter');
            companies.forEach(company => {
                const option = document.createElement('option');
                option.value = company;
                option.textContent = company;
                dropdown.appendChild(option);
            });
        }
        populateCompanyDropdown();

        // Populate sector dropdown
        function populateSectorDropdown() {
            const sectors = [...new Set(jobsData.map(job => job.sector || 'Other'))].sort();
            const dropdown = document.getElementById('sectorFilter');
            sectors.forEach(sector => {
                const option = document.createElement('option');
                option.value = sector;
                option.textContent = sector;
                dropdown.appendChild(option);
            });
        }
        populateSectorDropdown();

        // Populate location dropdown - extract individual cities from multi-location jobs
        function populateLocationDropdown() {
            const allCities = new Set();
            jobsData.forEach(job => {
                const location = job.location || '';
                // Split on "; " to get individual cities from multi-location jobs
                const cities = location.split('; ');
                cities.forEach(city => {
                    if (city && city.trim()) {
                        allCities.add(city.trim());
                    }
                });
            });

            const sortedCities = [...allCities].sort();
            const dropdown = document.getElementById('locationFilter');
            sortedCities.forEach(city => {
                const option = document.createElement('option');
                option.value = city;
                option.textContent = city;
                dropdown.appendChild(option);
            });
        }
        populateLocationDropdown();

        // Filtering and sorting
        function filterAndSortJobs() {
            const minScore = parseInt(document.getElementById('minScore').value);
            const searchText = document.getElementById('searchInput').value.toLowerCase();
            const statusFilter = document.getElementById('statusFilter').value;
            const sortBy = document.getElementById('sortBy').value;
            const companyFilter = document.getElementById('companyFilter').value;
            const sectorFilter = document.getElementById('sectorFilter').value;
            const locationFilter = document.getElementById('locationFilter').value;
            const dateFilter = document.getElementById('dateFilter').value;

            // Calculate date thresholds
            const now = new Date();
            const oneWeekAgo = new Date(now.getTime() - 7 * 24 * 60 * 60 * 1000);
            const oneMonthAgo = new Date(now.getTime() - 30 * 24 * 60 * 60 * 1000);
            const threeMonthsAgo = new Date(now.getTime() - 90 * 24 * 60 * 60 * 1000);

            let filtered = jobsData.filter(job => {
                if (job.match_score < minScore) return false;
                if (searchText && !JSON.stringify(job).toLowerCase().includes(searchText)) return false;
                if (statusFilter && job.app_status !== statusFilter) return false;
                if (companyFilter && job.company !== companyFilter) return false;
                if (sectorFilter && job.sector !== sectorFilter) return false;
                // Location filter: check if selected city is in the job's location
                // This handles multi-location jobs like "NYC; San Francisco; Seattle"
                if (locationFilter) {
                    const jobLocations = (job.location || '').split('; ');
                    if (!jobLocations.includes(locationFilter)) return false;
                }
                // Date filter
                if (dateFilter) {
                    // Get the best available date - prefer posted_date, fall back to scraped_date
                    let dateStr = job.posted_date;

                    // Check if posted_date is invalid (null, undefined, empty, or 'nan')
                    if (dateStr === null || dateStr === undefined || dateStr === '' || dateStr === 'nan') {
                        dateStr = job.scraped_date;
                    }

                    // If still no date, include the job
                    if (!dateStr) return true;

                    const jobDate = new Date(dateStr);

                    // If date parsing failed, include the job
                    if (isNaN(jobDate.getTime())) return true;

                    // Filter based on selection
                    if (dateFilter === 'week' && jobDate < oneWeekAgo) return false;
                    if (dateFilter === 'month' && jobDate < oneMonthAgo) return false;
                    if (dateFilter === 'quarter' && jobDate < threeMonthsAgo) return false;
                }
                return true;
            });

            // Sort
            filtered.sort((a, b) => {
                if (sortBy === 'score') return b.match_score - a.match_score;
                if (sortBy === 'date') return new Date(b.scraped_date) - new Date(a.scraped_date);
                if (sortBy === 'company') return a.company.localeCompare(b.company);
                return 0;
            });

            console.log('Filtered to', filtered.length, 'jobs');
            renderJobs(filtered);
            updateStats(filtered);
            updateCharts(filtered);
            updateSubtitle();
            console.log('Filter complete');
        }

        // Event listeners
        document.getElementById('minScore').addEventListener('input', (e) => {
            document.getElementById('minScoreValue').textContent = e.target.value;
            filterAndSortJobs();
        });

        document.getElementById('searchInput').addEventListener('input', filterAndSortJobs);
        document.getElementById('statusFilter').addEventListener('change', filterAndSortJobs);
        document.getElementById('sortBy').addEventListener('change', filterAndSortJobs);
        document.getElementById('companyFilter').addEventListener('change', filterAndSortJobs);
        document.getElementById('sectorFilter').addEventListener('change', filterAndSortJobs);
        document.getElementById('locationFilter').addEventListener('change', filterAndSortJobs);
        document.getElementById('dateFilter').addEventListener('change', filterAndSortJobs);

        // Initialize Charts FIRST (before any filtering)
        // Companies chart
        function initCompaniesChart(jobs) {
            const companyCounts = {};
            jobs.forEach(job => {
                companyCounts[job.company] = (companyCounts[job.company] || 0) + 1;
            });
            const sortedCompanies = Object.entries(companyCounts)
                .sort((a, b) => b[1] - a[1])
                .slice(0, 10);

            return new Chart(document.getElementById('companiesChart'), {
                type: 'bar',
                data: {
                    labels: sortedCompanies.map(c => c[0]),
                    datasets: [{
                        label: 'Job Postings',
                        data: sortedCompanies.map(c => c[1]),
                        backgroundColor: '#667eea'
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        title: { display: true, text: 'Top Hiring Companies' }
                    }
                }
            });
        }

        function initScoresChart(jobs) {
            const scoreRanges = { '0-60': 0, '60-80': 0, '80-100': 0 };
            jobs.forEach(job => {
                if (job.match_score < 60) scoreRanges['0-60']++;
                else if (job.match_score < 80) scoreRanges['60-80']++;
                else scoreRanges['80-100']++;
            });

            return new Chart(document.getElementById('scoresChart'), {
                type: 'doughnut',
                data: {
                    labels: ['0-60 (Low)', '60-80 (Medium)', '80-100 (High)'],
                    datasets: [{
                        data: [scoreRanges['0-60'], scoreRanges['60-80'], scoreRanges['80-100']],
                        backgroundColor: ['#95a5a6', '#f39c12', '#2ecc71']
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        title: { display: true, text: 'Match Score Distribution' }
                    }
                }
            });
        }

        // Initialize charts with all data
        companiesChart = initCompaniesChart(jobsData);
        scoresChart = initScoresChart(jobsData);

        // Initial render
        renderJobs(jobsData);
        updateStats(jobsData);
    </script>
</body>
</html>
"""


def generate_dashboard(jobs: List[Dict], stats: Dict, profile: Dict) -> str:
    """Generate HTML dashboard from job data."""
    template = Template(DASHBOARD_TEMPLATE)

    # Prepare jobs data for JSON
    jobs_for_json = []
    for job in jobs:
        job_data = {
            "id": job["id"],
            "title": job["title"],
            "company": job["company"],
            "location": job.get("location", ""),
            "url": job["url"],
            "match_score": job.get("match_score", 0),
            "match_explanation": job.get("match_explanation", ""),
            "skills_matched": job.get("skills_matched", []),
            "skills_missing": job.get("skills_missing", []),
            "match_breakdown": job.get("match_breakdown", {}),
            "app_status": job.get("app_status", ""),
            "posted_date": job.get("posted_date"),
            "scraped_date": job["scraped_date"],
            "sector": job.get("sector", "Other")
        }
        jobs_for_json.append(job_data)

    # Render template
    html = template.render(
        jobs_json=json.dumps(jobs_for_json),
        stats_json=json.dumps(stats),
        stats=stats,
        profile=profile,
        generated_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

    return html
