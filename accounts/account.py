from enum import Enum
from pathlib import Path
from typing import List


class OperationType(Enum):
    download = 1
    upload = 2
    move = 3
    delete = 4


class Account:
    def __init__(self, ident: str, email: str, local_root: Path):
        self.name = None
        self.ident = ident
        self.email = email
        self.local_root = local_root
        self.selective = {"enabled": False, "new_partial": False, "tree": None}
        self.operation_dic = assemble_op_map(self)
        self.folder_mime_type = None
        self.capacity = 0
        self.usage = 0
        self.usage_in_drive = 0
        self.max_upload_size = 0
        self.connection_handler = None
        self.last_changes_seen_flag = None

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
