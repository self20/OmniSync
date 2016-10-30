from enum import Enum
from pathlib import Path
from typing import List


class OperationType(Enum):
    download = 1
    upload = 2
    move = 3
    delete = 4


class Account:
    def __init__(self, email: str, local_root: Path):
        self.name = None
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

    def download(self):
        pass

    def upload(self):
        pass

    def move(self):
        pass

    def delete(self):
        pass

    def remote_root(self):
        pass

    def check_local_changes(self):
        pass

    def check_remote_changes(self):
        pass

    def checksum_function(self, file):
        pass

    def list_all_remote_files(self) -> List:
        pass

    @staticmethod
    def parse_user(obj, connection_handler):
        pass


def assemble_op_map(account: Account) -> dict:
    return {OperationType.download: account.download,
            OperationType.upload: account.upload,
            OperationType.move: account.move,
            OperationType.delete: account.delete}
