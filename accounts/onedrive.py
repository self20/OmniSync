from pathlib import Path

from accounts.account import Account


class OneDrive(Account):
    def __init__(self, name: str, email: str, directory: Path):
        super().__init__(name, email, directory)
