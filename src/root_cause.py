def identify_root_cause(message):

    message = message.lower()

    if "database connection" in message:
        return "Database connectivity issue"

    elif "timeout" in message:
        return "Service response timeout"

    elif "authentication" in message:
        return "Authentication failure"

    elif "permission" in message:
        return "Permission or access issue"

    elif "file not found" in message:
        return "Missing file or incorrect file path"

    else:
        return "Root cause requires further investigation"