# Job Market Analytics 📊

A data analytics project that analyzes job market data using **Python, MySQL, FastAPI, Pandas, and Power BI**.

## 📌 Project Overview

The Job Market Analytics project stores job listing data in MySQL, analyzes it using Python and Pandas, provides data through a FastAPI backend, and presents insights through an interactive Power BI dashboard.

## 🛠️ Technologies Used

* **Python** – Data analysis and processing
* **Pandas** – Data manipulation and analysis
* **MySQL** – Database management and SQL queries
* **FastAPI** – REST API development
* **Power BI** – Data visualization and dashboard
* **GitHub** – Version control and project hosting

## ✨ Features

* Store job market data in MySQL
* Analyze job titles and locations
* Search job listings through API
* Get individual job details
* Analyze job counts by category
* Analyze skills required in job listings
* Analyze job types
* Analyze salary ranges
* Interactive Power BI dashboard

## ⚡ API Endpoints

| Endpoint                 | Description                      |
| ------------------------ | -------------------------------- |
| `/`                      | Check whether the API is running |
| `/jobs`                  | Get all job listings             |
| `/jobs/{job_id}`         | Get a specific job               |
| `/search?keyword=Python` | Search jobs by keyword           |
| `/analytics/jobs`        | Get job statistics               |
| `/analytics/locations`   | Get location statistics          |
| `/analytics/summary`     | Get overall job market summary   |

## 📊 Dashboard

The Power BI dashboard provides visual insights into:

* Total Jobs
* Total Companies
* Total Locations
* Jobs by Job Title
* Jobs by Location
* Skills Analysis
* Jobs by Job Type
* Average Salary by Job Title

## 🗄️ Database

The project uses a MySQL database named `job_market` with a `jobs` table containing:

* Job ID
* Job Title
* Company
* Location
* Experience
* Salary
* Skills
* Job Type

## 🚀 How to Run

### 1. Install dependencies

```bash
pip install pandas mysql-connector-python fastapi uvicorn
```

### 2. Configure MySQL

Create the `job_market` database and `jobs` table in MySQL.

Update the MySQL connection settings in `database.py` with your own local credentials.

### 3. Run the API

```bash
python -m uvicorn app:app --reload
```

### 4. Open API documentation

Open:

`http://127.0.0.1:8000/docs`

## 🎯 Project Goal

The goal of this project is to demonstrate practical skills in **SQL, Python, data analysis, API development, database management, and data visualization** using a real-world job market analytics use case.

