from mini_queue.message import Message
from mini_queue.queue import Queue
from mini_queue.broker import Broker

Q = Queue()

print(len(Q), "- Num of Q elements after Queue creation. Q =", Q)
broker = Broker(Q)
print(broker)



msg = Message("text1")
broker.publish(msg)
print(len(Q), "- Num of Q elements after 1st publishing message by Broker. Q =", Q)

msg_2 = Message("text2")
broker.publish(msg_2)
print(len(Q), "- Num of Q elements after 2nd publishing message by Broker. Q =", Q)


# try:
#     msg_from_queue = broker.consume()
#     print(len(Q), "- Num of Q elements after consuming one message by Broker. Q =", Q)
#     print(msg_from_queue)
#
#     msg_from_queue = broker.consume()
#     print(msg_from_queue)
#     msg_from_queue = broker.consume()
# except IndexError as e:
#     print(f"Queue was empty ({e}, {Q}).")


broker.create_queue("1st queue")
msg_3 = Message("text3")
broker.publish(msg_3)
broker.publish(msg_3, queue_name="1st queue")

broker.create_queue("2nd queue")

print(broker)


print()
for key_q, q in broker._queues.items():
    print(key_q, q, len(q))

