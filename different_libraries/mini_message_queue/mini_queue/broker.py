from .queue import Queue
from .message import Message


class Broker:

    def __init__(self):
        self._queues = {}

    def publish(self, message_obj: Message, queue_name: str) -> None:
        self._queues[queue_name].publish(message_obj)

    def consume(self, queue_name: str) -> Message:

        return self._queues[queue_name].consume()

    def add_queue(self, queue_obj: Queue) -> None:
        self._queues[queue_obj.name] = queue_obj
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
