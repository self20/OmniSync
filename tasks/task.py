from pathlib import Path
from typing import Union

from accounts.account import Account, OperationType


class Task:
    def __init__(self, operation_type: OperationType, account: Account, item: Union[str, Path]):
        self.operation_type = operation_type
        self.account = account
        self.item = item

    def get_operation(self):
        return self.account.operation_dic[self.operation_type]
