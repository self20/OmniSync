from enum import Enum
from pathlib import Path


class OperationType(Enum):
    download = 1
    upload = 2
    move = 3
    delete = 4


class Account:
    def __init__(self, name: str, email: str, directory: Path):
        self.name = name
        self.email = email
        self.directory = directory
        self.selective = {"enabled": False, "new_partial": False, "tree": None}
        self.dic = {OperationType.download: self.download,
                    OperationType.upload: self.upload,
                    OperationType.move: self.move,
                    OperationType.delete: self.delete}

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

    def check_changes(self):
        pass