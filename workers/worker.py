from asyncio.queues import QueueEmpty

import time

from tasks.task import Task
from tasks.task_queue import TaskQueue
from util.connection_test import is_connected


class Worker:
    num = 0

    def __init__(self, task_queue: TaskQueue):
        self.num = str(Worker.num)
        self.task_queue = task_queue
        self.task = None
        Worker.num += 1

    def work(self):
        print("Worker-" + self.num + " is starting to work...")
        try:
            while not self.task_queue.empty():
                self.task = self.task_queue.get_nowait()  # type: Task
                self.run_task()
        except QueueEmpty:
            pass
        self.task = None
        print("Worker-" + self.num + " Queue is empty. Back to waiting...")
        self.task_queue.event.clear()
        self.wait()

    def wait(self):
        print("Worker-" + self.num + " waiting for event...")
        self.task_queue.event.wait()
        print("Worker-" + self.num + " woke up...")
        self.work()

    def execute(self):
        self.wait()
        self.work()

    def run_task(self):
        operation = self.task.get_operation()
        print("Worker-" + self.num + " got task of type " + self.task.operation_type + ". Starting...")
        while True:
            try:
                operation()
                break
            except:
                print("ERROR: Worker-" + self.num + " when performing task of type " + self.task.operation_type + ".")
                if not is_connected():
                    time.sleep(15)
