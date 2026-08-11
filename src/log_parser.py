import re


LOG_PATTERN = re.compile(
    r"(?P<timestamp>\d{4}-\d{2}-\d{2} "
    r"\d{2}:\d{2}:\d{2}) "
    r"(?P<level>INFO|WARNING|ERROR) "
    r"(?P<message>.*)"
)


def parse_log_file(file_path):

    records = []

    with open(file_path, "r") as file:

        for line in file:

            line = line.strip()

            match = LOG_PATTERN.match(line)

            if match:

                records.append({
                    "timestamp": match.group("timestamp"),
                    "level": match.group("level"),
                    "message": match.group("message")
                })

    return records