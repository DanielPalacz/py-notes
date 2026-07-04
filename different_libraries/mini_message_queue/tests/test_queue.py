from mini_queue.message import Message
from mini_queue.queue import Queue
from mini_queue.broker import Broker


def test_queue_fifo():
    q1 = Queue("def")
    broker = Broker()
    broker.add_queue(q1)

    msg = Message("text1")
    msg_2 = Message("text2")

    print()
    print()
    print(msg)
    print(msg_2)

    broker.publish(msg, "def")
    broker.publish(msg_2, "def")


    assert broker.consume("def") is msg
    assert broker.consume("def") is msg_2
