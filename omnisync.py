import dataset
import time

from tasks.task_queue import TaskQueue
from workers.pool import Pool

if __name__ == "__main__":

    db = dataset.connect("sqlite:////home/andre/.omnisync/database.db")

    config = db['config']
    down_limit = config.find_one(name='down_limit')
    up_limit = config.find_one(name='up_limit')
    config = config.find_one(name='max_conn')

    if not down_limit or not up_limit or not config:
        config.insert(dict(name='down_limit', value='0'))
        config.insert(dict(name='up_limit', value='0'))
        config.insert(dict(name='max_conn', value='4'))

    task_queue = TaskQueue()
    pool = Pool(task_queue)
    pool.set_worker_num(4)

    time.sleep(5)

    pool.start()

    time.sleep(5)

    task_queue.trigger()

    time.sleep(5)
