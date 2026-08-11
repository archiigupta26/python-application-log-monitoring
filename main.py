import csv
from src.log_parser import parse_log_file
from src.incident_detector import (
    classify_incident,
    find_recurring_errors,
    generate_fingerprint
)
from src.database import create_connection, insert_incident
from src.report_generator import generate_health_report
from src.alert_manager import generate_alert
from src.root_cause import identify_root_cause


# Read and parse the application log file
records = parse_log_file("logs/application.log")


# Find recurring errors
recurring = find_recurring_errors(records)


# Connect to MySQL
connection = create_connection()


# Display and store each log record
for record in records:

    fingerprint = generate_fingerprint(record)

    severity = classify_incident(record)

    occurrence_count = recurring.get(
        record["message"],
        1
    )

    root_cause = identify_root_cause(
        record["message"]
    )


    generate_alert(
        record,
        severity,
        occurrence_count
    )

    print("Timestamp:", record["timestamp"])
    print("Level:", record["level"])
    print("Message:", record["message"])
    print("Severity:", severity)
    print("Occurrences:", occurrence_count)
    print("Root Cause:", root_cause)
    print("-----------------------------")

    insert_incident(
        connection,
        record,
        severity,
        occurrence_count,
        fingerprint,
        root_cause
    )

# Close MySQL connection
connection.close()


# Display recurring errors
print("\nRecurring Errors:")

for message, count in recurring.items():

    print(
        message,
        "->",
        count,
        "occurrences"
    )



health_report = generate_health_report()

report = f"""
APPLICATION HEALTH REPORT
=========================

Total Incidents: {health_report["total"]}
Critical Incidents: {health_report["critical"]}
Warning Incidents: {health_report["warning"]}
Normal Incidents: {health_report["normal"]}

Health Score: {health_report["health_score"]}/100
Application Status: {health_report["status"]}
"""

print(report)

with open("reports/health_report.txt", "w") as file:

    file.write(report)



connection = create_connection()

cursor = connection.cursor()

cursor.execute("""
    SELECT
        timestamp,
        level,
        message,
        severity,
        occurrence_count,
        root_cause
    FROM incidents
""")

rows = cursor.fetchall()

with open("reports/incidents.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Timestamp",
        "Level",
        "Message",
        "Severity",
        "Occurrence Count",
        "Root Cause"
    ])

    writer.writerows(rows)

cursor.close()
connection.close()

print("Incident CSV report generated successfully!")