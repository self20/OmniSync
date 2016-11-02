from pathlib import Path

from accounts import onedrive_connect
from accounts.account import Account


class OneDrive(Account):
    def __init__(self, ident: str, email: str, local_root: Path):
        super().__init__(ident, email, local_root)

    def connect(self):
        onedrive_connect.authenticate(self)
