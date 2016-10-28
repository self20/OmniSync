from pathlib import Path

from accounts.account import Account


class GDrive(Account):
    def __init__(self, name: str, email: str, local_root: Path):
        super().__init__(name, email, local_root)
