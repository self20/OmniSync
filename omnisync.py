import subprocess

import dataset
import time

from tasks.task_queue import TaskQueue
from workers.pool import Pool
from util import constants


def load_config(database: dataset.Database) -> (int, int, int):
    constants.OMNISYNC_DIR.mkdir(exist_ok=True)
    cfg_table = database.get_table('config', primary_type='String')
    down_limit_cfg = cfg_table.find_one(id='down_limit_cfg')
    up_limit_cfg = cfg_table.find_one(id='up_limit_cfg')
    max_conn_cfg = cfg_table.find_one(id='max_conn_cfg')
    # writing default config if current doesn't exist or is incosistent
    if not down_limit_cfg or not up_limit_cfg or not max_conn_cfg:
        down_limit_cfg = 0
        up_limit_cfg = 0
        max_conn_cfg = 4
        cfg_table.insert(dict(id='down_limit_cfg', value=down_limit_cfg))
        cfg_table.insert(dict(id='up_limit_cfg', value=up_limit_cfg))
        cfg_table.insert(dict(id='max_conn_cfg', value=max_conn_cfg))
    return down_limit_cfg, up_limit_cfg, max_conn_cfg


def load_database() -> dataset.Database:
    db_path = constants.OMNISYNC_DIR / 'omnisync.db'
    if not db_path.is_file():
        subprocess.call(['sqlite3', str(db_path), '".databases"'])
    return dataset.connect('sqlite:///' + str(db_path))


def initialize(max_connections: int) -> (TaskQueue, Pool):
    new_task_queue = TaskQueue()
    new_pool = Pool(new_task_queue)
    new_pool.set_worker_num(max_connections)
    return new_task_queue, new_pool


if __name__ == "__main__":

    db = load_database()
    down_limit, up_limit, max_conn = load_config(db)
    task_queue, pool = initialize(max_conn)

    time.sleep(5)

    pool.start()

    time.sleep(5)

    task_queue.trigger()

    time.sleep(5)
