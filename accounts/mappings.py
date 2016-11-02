from enum import Enum
from pathlib import Path
from typing import List, Union

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Index, ForeignKeyConstraint
from sqlalchemy.sql.sqltypes import Time

Base = declarative_base()


class OperationType(Enum):
    download = 1
    upload = 2
    move = 3
    delete = 4


class Account(Base):
    __tablename__ = 'accounts'

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    local_root = Column(String, nullable=False)
    selective_enabled = Column(Boolean, nullable=False)
    selective_partial_new = Column(Boolean, nullable=False)
    folder_mime_type = Column(String, nullable=False)
    capacity = Column(Integer, nullable=False)
    usage = Column(Integer, nullable=False)
    usage_in_drive = Column(Integer, nullable=False)
    max_upload_size = Column(Integer, nullable=False)
    last_changes_seen_flag = Column(String, nullable=False)
    connection_handler = None
    import_types_map = dict()
    export_types_map = dict()

    def connect(self) -> None:
        pass

    def set_current_last_changes(self) -> None:
        pass

    def download(self, remote_id: str, path: str) -> None:
        pass

    def upload(self, parent_id: str, path: str) -> None:
        pass

    def move(self, remote_id: str, new_parent_id: str) -> None:
        pass

    def delete(self, remote_id: str) -> None:
        pass

    def remote_root(self) -> str:
        pass

    def check_local_changes(self) -> List[dict]:
        pass

    def check_remote_changes(self) -> List[dict]:
        pass

    def list_all_remote_files(self) -> List[dict]:
        pass

    def list_all_local_files(self) -> List[dict]:
        pass

    def initial_sync(self) -> None:
        pass

    @staticmethod
    def checksum_function(path: Union[Path, str]) -> str:
        pass

    @staticmethod
    def parse_user(obj, connection_handler):
        pass


class AccountFile(Base):
    __tablename__ = 'accountfiles'

    __table_args__ = (
        Index('account_file_id_idx', 'account_id', 'file_account_id', unique=True),
        ForeignKeyConstraint(
            ['account_id', 'file_account_parent_id'],
            ['accountfiles.account_id', 'accountfiles.file_account_id']
        )
    )

    account_id = Column(String, ForeignKey('accounts.id'), primary_key=True)
    file_local_path = Column(String, primary_key=True)
    file_account_id = Column(String, nullable=False)
    file_account_parent_id = Column(String)
    file_remote_hash = Column(String)
    file_remote_mime = Column(String, nullable=False)
    file_remote_modified_time = Column(Time, nullable=False)
    file_remote_size = Column(Integer)
    file_remote_version = Column(Integer, nullable=False)
    ignore = Column(Boolean, nullable=False)

    account = relationship('Account', back_ref='files')
    parent = relationship('AccountFile', back_ref='children', remote_side=[account_id, file_account_id])
