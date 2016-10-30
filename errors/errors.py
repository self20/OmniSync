class AuthError(Exception):
    def __init__(self, reason: str):
        super().__init__("Authenticartion error. Reason: " + reason)
