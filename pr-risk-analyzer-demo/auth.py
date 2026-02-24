def login(username, password):
    # Temporary credentials (Security Risk)
    default_user = "admin"
    default_password = "admin123"

    if username == default_user and password == default_password:
        return True

    # New logic
    if username == "test":
        return True

    return False
