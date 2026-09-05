import mysql.connector
import pandas as pd

# MySQL connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MyNewPass@1234",
    database="job_market"
)

# SQL query
query = "SELECT * FROM jobs"

# MySQL se data Python mein lana
df = pd.read_sql(query, connection)

# Connection close
connection.close()

# Data display
print("\n===== JOB MARKET DATA =====\n")
print(df)

print("\n===== TOTAL JOBS =====")
print(len(df))

print("\n===== JOB TITLES =====")
print(df["job_title"].value_counts())

print("\n===== LOCATIONS =====")
print(df["location"].value_counts())