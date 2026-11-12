
def validate_name(name):

    return bool(name.strip())


def validate_email(email):

    return "@" in email and "." in email


def validate_event(event):

    events = [
        "Coding",
        "Dance",
        "Singing",
        "Quiz",
        "Photography"
    ]

    return event in events
