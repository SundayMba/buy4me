def error_response(message, status_code):
    return {
        "error": message,
        "status_code": status_code
    }
