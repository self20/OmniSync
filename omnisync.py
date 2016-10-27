import dataset
import time

from tasks.task_queue import TaskQueue
from workers.pool import Pool

if __name__ == "__main__":

    db = dataset.connect("sqlite:////home/andre/.omnisync/database.db")

    task_queue = TaskQueue()
    pool = Pool(task_queue)
    pool.set_worker_num(4)

    time.sleep(5)

    pool.start()

    time.sleep(5)

    task_queue.trigger()

    time.sleep(5)