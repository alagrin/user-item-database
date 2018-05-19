class User:
    """Create a user, a valid user object to work with flask JWT"""
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password
