from fastapi import FastAPI, HTTPException
from database import get_connection

app = FastAPI(
    title="Job Market Analytics API",
    description="API for Job Market Data Analysis",
    version="1.0"
)


# -------------------------
# HOME
# -------------------------

@app.get("/")
def home():
    return {
        "message": "Job Market Analytics API is running!"
    }


# -------------------------
# GET ALL JOBS
# -------------------------

@app.get("/jobs")
def get_jobs():

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM jobs")

    jobs = cursor.fetchall()

    cursor.close()
    connection.close()

    return jobs


# -------------------------
# GET JOB BY ID
# -------------------------

@app.get("/jobs/{job_id}")
def get_job(job_id: int):

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM jobs WHERE id = %s",
        (job_id,)
    )

    job = cursor.fetchone()

    cursor.close()
    connection.close()

    if job is None:
        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    return job


# -------------------------
# SEARCH JOBS
# -------------------------

@app.get("/search")
def search_jobs(keyword: str):

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    query = """
        SELECT *
        FROM jobs
        WHERE job_title LIKE %s
        OR company LIKE %s
        OR skills LIKE %s
    """

    search = f"%{keyword}%"

    cursor.execute(
        query,
        (search, search, search)
    )

    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return results


# -------------------------
# JOB STATISTICS
# -------------------------

@app.get("/analytics/jobs")
def job_statistics():

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    query = """
        SELECT
            job_title,
            COUNT(*) AS total_jobs
        FROM jobs
        GROUP BY job_title
        ORDER BY total_jobs DESC
    """

    cursor.execute(query)

    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return results


# -------------------------
# LOCATION STATISTICS
# -------------------------

@app.get("/analytics/locations")
def location_statistics():

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    query = """
        SELECT
            location,
            COUNT(*) AS total_jobs
        FROM jobs
        GROUP BY location
        ORDER BY total_jobs DESC
    """

    cursor.execute(query)

    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return results


# -------------------------
# DASHBOARD SUMMARY
# -------------------------

@app.get("/analytics/summary")
def dashboard_summary():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM jobs"
    )

    total_jobs = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(DISTINCT company) FROM jobs"
    )

    total_companies = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(DISTINCT location) FROM jobs"
    )

    total_locations = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    return {
        "total_jobs": total_jobs,
        "total_companies": total_companies,
        "total_locations": total_locations
    }

