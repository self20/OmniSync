import multiprocessing
from tasks.task_queue import TaskQueue
from workers.worker import Worker
from typing import List


class Pool:
    def __init__(self, task_queue: TaskQueue):
        self.process_list = []  # type: List[multiprocessing.Process]
        self.worker_list = []  # type: List[Worker]
        self.task_queue = task_queue
        self.can_start = False

    def start(self):
        self.can_start = True
        self.task_queue.trigger()

    def hold(self):
        self.task_queue.hold()

    def trigger(self):
        if self.can_start:
            self.task_queue.trigger()

    def set_worker_num(self, num):
        cur_num = len(self.process_list)
        self.hold()
        if num > cur_num:
            for i in range(0, num - cur_num):
                self.add()
        elif num < cur_num:
            for i in reversed(range(num, cur_num)):
                self.remove(i)
        self.trigger()

    def add(self):
        worker = Worker(self.task_queue)
        process = multiprocessing.Process(target=worker.execute)
        process.daemon = True
        self.worker_list.append(worker)
        self.process_list.append(process)
        print("Worker-" + worker.num + " added to the pool")
        process.start()

    def remove(self, i: int):
        if self.worker_list[i].task:
            self.task_queue.put_nowait(self.worker_list[i].task)
        print("Worker-" + self.worker_list[i].num + " removed from the pool")
        self.process_list[i].terminate()
        del self.worker_list[i]
        del self.process_list[i]

    def terminate_all(self):
        self.task_queue.hold()
        for i in reversed(range(0, len(self.process_list))):
            self.remove(i)
        self.task_queue.trigger()
