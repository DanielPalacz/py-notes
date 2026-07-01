from .queue import Queue
from .message import Message
from typing import Optional


class Broker:

    def __init__(self, queue_obj: Queue):
        self._queues = {"default": queue_obj}

    def publish(self, message: Message, queue_name: Optional[str] = None) -> None:

        if queue_name is None:
            queue_name = "default"

        self._queues[queue_name].publish(message)

    def consume(self, queue_name: Optional[str] = None) -> Message:

        if queue_name is None:
            queue_name = "default"

        return self._queues[queue_name].consume()


    def create_queue(self, queue_name: str) -> None:

        self._queues[queue_name] = Queue()

        return None



    # def ack(self):
    #     pass
    #

    def __repr__(self):
        return f"Broker(queues={self._queues!r})"

    def __str__(self):
        return f"Broker(queues={self._queues!r})"



# Na początku ack() nie ma sensu. W pierwszej wersji zrobiłbym po prostu:
# msg = broker.consume()
# i consume() od razu usuwa wiadomość z kolejki.
