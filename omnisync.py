import dataset
import time

from tasks.task_queue import TaskQueue
from workers.pool import Pool


def initialize() -> (dataset.Database, dataset.Table, TaskQueue, Pool):
    db = dataset.connect("sqlite:////home/andre/.omnisync/database.db")
    config = db.get_table('config')
    down_limit = config.find_one(id='down_limit')
    up_limit = config.find_one(id='up_limit')
    max_conn = config.find_one(id='max_conn')
    # loading/writing default config if current doesn't exist or is incosistent
    if not down_limit or not up_limit or not config:
        down_limit = 0
        up_limit = 0
        max_conn = 4
        config.insert(dict(id='down_limit', value=down_limit))
        config.insert(dict(id='up_limit', value=up_limit))
        config.insert(dict(id='max_conn', value=max_conn))
    task_queue = TaskQueue()
    pool = Pool(task_queue)
    pool.set_worker_num(max_conn)
    return db, config, task_queue, pool


if __name__ == "__main__":

    db, config, task_queue, pool = initialize()

    time.sleep(5)

    pool.start()

    time.sleep(5)

    task_queue.trigger()

    time.sleep(5)
