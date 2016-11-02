from pathlib import Path

from sqlalchemy import Column, String
from sqlalchemy.sql.schema import ForeignKeyConstraint

from accounts import onedrive_connect
from accounts.mappings import Account


class OneDrive(Account):
    __mapper_args__ = {
        'polymorphic_identity': 'OneDrive',
    }

    __table_args__ = (ForeignKeyConstraint(['email', 'type'], ['accounts.email', 'accounts.type']),)

    email = Column(String, primary_key=True)
    type = Column(String, primary_key=True)

    def __init__(self, ident: str, email: str, local_root: Path):
        super().__init__(ident, email, local_root)

    def connect(self):
        onedrive_connect.authenticate(self)
