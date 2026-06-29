from mini_queue.message import Message
from mini_queue.queue import Queue
from mini_queue.broker import Broker


def test_queue_fifo():
    Q = Queue()
    broker = Broker(Q)

    msg = Message("text1")
    msg_2 = Message("text2")

    print()
    print()
    print(msg)
    print(msg_2)

    broker.publish(msg)
    broker.publish(msg_2)


    assert broker.consume() is msg
    assert broker.consume() is msg_2
