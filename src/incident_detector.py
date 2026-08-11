from collections import Counter
import hashlib

def classify_incident(record):

    if record["level"] == "ERROR":
        return "CRITICAL"

    elif record["level"] == "WARNING":
        return "WARNING"

    else:
        return "NORMAL"


def find_recurring_errors(records, threshold=2):

    error_messages = [
        record["message"]
        for record in records
        if record["level"] == "ERROR"
    ]

    counts = Counter(error_messages)

    recurring = {
        message: count
        for message, count in counts.items()
        if count >= threshold
    }

    return recurring


def generate_fingerprint(record):

    raw_data = (
        record["level"]
        + "|"
        + record["message"]
    )

    fingerprint = hashlib.sha256(
        raw_data.encode()
    ).hexdigest()

    return fingerprint