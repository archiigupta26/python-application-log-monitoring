from src.database import create_connection


def generate_health_report():

    connection = create_connection()

    cursor = connection.cursor()

    # Total incidents
    cursor.execute(
        "SELECT COUNT(*) FROM incidents"
    )

    total_incidents = cursor.fetchone()[0]

    # Critical incidents
    cursor.execute(
        "SELECT COUNT(*) FROM incidents WHERE severity = 'CRITICAL'"
    )

    critical_incidents = cursor.fetchone()[0]

    # Warning incidents
    cursor.execute(
        "SELECT COUNT(*) FROM incidents WHERE severity = 'WARNING'"
    )

    warning_incidents = cursor.fetchone()[0]

    # Normal incidents
    cursor.execute(
        "SELECT COUNT(*) FROM incidents WHERE severity = 'NORMAL'"
    )

    normal_incidents = cursor.fetchone()[0]

    # Calculate health score
    if total_incidents == 0:

        health_score = 100

    else:

        critical_percentage = (
            critical_incidents / total_incidents
        ) * 100

        warning_percentage = (
            warning_incidents / total_incidents
        ) * 100

        health_score = (
            100
            - (critical_percentage * 1.5)
            - (warning_percentage * 0.5)
        )

        health_score = max(
            0,
            min(100, health_score)
        )

    # Determine application status
    if health_score >= 90:

        status = "HEALTHY"

    elif health_score >= 70:

        status = "WARNING"

    else:

        status = "CRITICAL"

    cursor.close()
    connection.close()

    return {
        "total": total_incidents,
        "critical": critical_incidents,
        "warning": warning_incidents,
        "normal": normal_incidents,
        "health_score": round(health_score, 2),
        "status": status
    }