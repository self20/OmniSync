from sqlalchemy.orm.session import Session

from accounts.mapping import Config
from tasks.task_queue import TaskQueue
from workers.pool import Pool

_db_session = None
_max_up = None
_max_down = None
_max_conn = None
_task_queue = None
_pool = None


class GlobalAccessor:

    @staticmethod
    def set_db_session(db_session: Session):
        global _db_session
        _db_session = db_session

    @staticmethod
    def get_db_session() -> Session:
        return _db_session

    @staticmethod
    def set_max_up(max_up: Config):
        global _max_up
        _max_up = max_up

    @staticmethod
    def get_max_up() -> Config:
        return _max_up

    @staticmethod
    def set_max_down(max_down: Config):
        global _max_down
        _max_down = max_down

    @staticmethod
    def get_max_down() -> Config:
        return _max_down

    @staticmethod
    def set_max_conn(max_conn: Config):
        global _max_conn
        _max_conn = max_conn

    @staticmethod
    def get_max_conn() -> Config:
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
