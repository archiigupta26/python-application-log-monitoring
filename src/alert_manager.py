def generate_alert(record, severity, occurrence_count):

    if severity == "CRITICAL":

        alert_message = (
            f"CRITICAL ALERT | "
            f"{record['timestamp']} | "
            f"{record['message']} | "
            f"Occurrences: {occurrence_count}"
        )

        print("\n🚨", alert_message)

        with open("reports/alerts.log", "a") as file:

            file.write(alert_message + "\n")

    elif severity == "WARNING":

        alert_message = (
            f"WARNING ALERT | "
            f"{record['timestamp']} | "
            f"{record['message']} | "
            f"Occurrences: {occurrence_count}"
        )

        print("\n⚠️", alert_message)

        with open("reports/alerts.log", "a") as file:

            file.write(alert_message + "\n")