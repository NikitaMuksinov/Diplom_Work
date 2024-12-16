from flask import session

AUTH_CREDENTIALS = {
    "username": "Aura",
    "password": "07052002"
}


def is_authenticated():
    return session.get('logged_in', False)
