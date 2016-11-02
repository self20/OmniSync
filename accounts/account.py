from sqlalchemy import Column, Integer, String, Boolean
from enum import Enum
from pathlib import Path
from typing import List
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class OperationType(Enum):
    download = 1
    upload = 2
    move = 3
    delete = 4


class Account(Base):
    __tablename__ = 'accounts'

    id = Column(String, primary_key=True)
    name = Column(String)
    email = Column(String)
    local_root = Column(String)
    selective_enabled = Column(Boolean)
    selective_partial_new = Column(Boolean)
    folder_mime_type = Column(String)
    capacity = Column(Integer)
    usage = Column(Integer)
    usage_in_drive = Column(Integer)
    max_upload_size = Column(Integer)
    last_changes_seen_flag = Column(String)
    ignore_list =
    connection_handler = None

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

    def checksum_function(self, path: str) -> str:
        pass

    def list_all_remote_files(self) -> List[dict]:
        pass

    def list_all_local_files(self) -> List[dict]:
        pass

    def initial_sync(self) -> None:
        pass

    @staticmethod
    def parse_user(obj, connection_handler):
        pass


def assemble_op_map(account: Account) -> dict:
    return {OperationType.download: account.download,
            OperationType.upload: account.upload,
            OperationType.move: account.move,
            OperationType.delete: account.delete}
