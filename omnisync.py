import dataset

from tasks.task_queue import TaskQueue
from workers.pool import Pool

if __name__ == "__main__":

    task_queue = TaskQueue()
    pool = Pool(task_queue)
    pool.set_worker_num(4)

    db = dataset.connect("sqlite:///home/andre/.omnisync/database.db")
