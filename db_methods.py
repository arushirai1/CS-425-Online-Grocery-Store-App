def validate_login(username, password):
    if username == 'admin' and password == 'pass':
        return 1000
    return 0