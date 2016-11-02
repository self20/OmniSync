from tasks.task_queue import TaskQueue
from workers.pool import Pool

_db = None  # type: dataset.Database
_max_up = 0  # type: int
_max_down = 0  # type: int
_max_conn = 4  # type: int
_task_queue = None  # type: TaskQueue
_pool = None  # type: Pool


class GlobalAccessor:

    @staticmethod
    def set_db(db: dataset.Database):
        global _db
        _db = db

    @staticmethod
    def get_db() -> dataset.Database:
        return _db

    @staticmethod
    def set_max_up(max_up: int):
        global _max_up
        _max_up = max_up

    @staticmethod
    def get_max_up() -> int:
        return _max_up

    @staticmethod
    def set_max_down(max_down: int):
        global _max_down
        _max_down = max_down

    @staticmethod
    def get_max_down() -> int:
        return _max_down

    @staticmethod
    def set_max_conn(max_conn: int):
        global _max_conn
        _max_conn = max_conn

    @staticmethod
    def get_max_conn() -> int:
        return _max_conn

    @staticmethod
    def set_task_queue(task_queue: TaskQueue):
        global _task_queue
        _task_queue = task_queue

    @staticmethod
    def get_task_queue() -> TaskQueue:
        return _task_queue

    @staticmethod
    def set_pool(pool: Pool):
        global _pool
        _pool = pool

    @staticmethod
    def get_pool() -> Pool:
        return _pool
