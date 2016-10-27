from multiprocessing import Event, get_context, Queue
from multiprocessing.queues import Queue

from tasks.task import Task


class TaskQueue(Queue):
    def __init__(self):
        super().__init__(ctx=get_context())
        self.event = Event()
        self.enable_event = False

    def hold(self):
        self.enable_event = True

    def trigger(self):
        self.enable_event = False
        self.event.set()

    def put(self, task: Task, block=True, timeout=None):
        super().put(task, block=block, timeout=timeout)
        if not self.enable_event:
            self.event.set()

    def put_nowait(self, task: Task):
        super().put_nowait(task)
        if not self.enable_event:
            self.event.set()
