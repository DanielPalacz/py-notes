from .queue import Queue
from .message import Message


class Broker:

    def __init__(self, queue_obj: Queue):
        self._queue_obj = queue_obj

    def publish(self, message) -> None:
        self._queue_obj.publish(message)

    def consume(self) -> Message:
        return self._queue_obj.consume()


    # def ack(self):
    #     pass
