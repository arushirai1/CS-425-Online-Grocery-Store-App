def validate_login(username, password):
    if username == 'admin' and password == 'pass':
        return True
    return False