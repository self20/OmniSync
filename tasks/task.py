from enum import Enum

from accounts.mapping import Account, AccountFile


class OperationType(Enum):
    download = 1
    upload = 2
    move = 3
    delete = 4


class Task:
    def __init__(self, operation_type: OperationType, account: Account, item: AccountFile):
        self.operation_type = operation_type
        self.account = account
        self.item = item

    def run(self) -> None:
        if self.operation_type == OperationType.download:
            pass
        elif self.operation_type == OperationType.upload:
            pass
        elif self.operation_type == OperationType.delete:
            pass
        elif self.operation_type == OperationType.move:
            pass
