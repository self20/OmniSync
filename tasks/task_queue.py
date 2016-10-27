from multiprocessing import Event, get_context, Queue
from multiprocessing.queues import Queue

from tasks.task import Task


class TaskQueue(Queue):
    def __init__(self):
        super().__init__(ctx=get_context())
        self.event = Event()
        self.allow_event = True

    def hold(self):
        self.allow_event = False

    def trigger(self):
        self.allow_event = True
        self.event.set()

    def put(self, task: Task, block=True, timeout=None):
        super().put(task, block=block, timeout=timeout)
        if self.allow_event:
            self.event.set()

    def put_nowait(self, task: Task):
        super().put_nowait(task)
        if self.allow_event:
            self.event.set()
