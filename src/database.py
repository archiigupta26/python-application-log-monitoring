import mysql.connector


def create_connection():

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="log_monitoring"
    )

    return connection


def insert_incident(
    connection,
    record,
    severity,
    occurrence_count,
    fingerprint,
    root_cause
):

    cursor = connection.cursor()

    query = """
        INSERT INTO incidents
        (timestamp, level, message, severity, occurrence_count, fingerprint, root_cause)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        record["timestamp"],
        record["level"],
        record["message"],
        severity,
        occurrence_count,
        fingerprint,
        root_cause
    )

    try:

        cursor.execute(query, values)

        connection.commit()

    except mysql.connector.IntegrityError:

        connection.rollback()

    cursor.close()


if __name__ == "__main__":

    connection = create_connection()

    if connection.is_connected():
        print("MySQL connection successful!")

    connection.close()