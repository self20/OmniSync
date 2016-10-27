from multiprocessing import Queue, Event

from tasks.task import Task


class TaskQueue(Queue):
    def __init__(self):
        super().__init__()
        self.event = Event()
        self.hold = False

    def hold(self):
        self.hold = True

    def trigger(self):
        self.hold = False
        self.event.set()

    def put(self, task: Task, block=True, timeout=None):
        super().put(task, block, timeout)
        if not self.hold:
            self.event.set()

    def put_nowait(self, task: Task):
        super().put_nowait(task)
        if not self.hold:
            self.event.set()
