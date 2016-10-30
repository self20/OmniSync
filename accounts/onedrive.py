from pathlib import Path

from accounts.account import Account


class OneDrive(Account):
    def __init__(self, email: str, local_root: Path):
        super().__init__(email, local_root)
