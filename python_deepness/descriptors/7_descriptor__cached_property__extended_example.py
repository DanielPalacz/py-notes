import threading

# Extended Cache Property
#  - Thread-safe caching
#  - Writable cached value


class ThreadSafeWritableCachedProperty:
    __slots__ = ('function_obj', 'function_name', '_lock')

    def __init__(self, function):
        self.function_obj = function
        self.function_name = None  # Set by __set_name__
        self._lock = threading.Lock()

    def __set_name__(self, owner, name):
        self.function_name = f"_{name}"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self

        if self.function_name not in obj.__dict__:
            with self._lock:
                # Double-check inside lock
                if self.function_name not in obj.__dict__:
                    obj.__dict__[self.function_name] = self.function_obj(obj)

        return obj.__dict__[self.function_name]

    def __set__(self, obj, value):
        with self._lock:  # Ensures only one thread modifies at a time
            obj.__dict__[self.function_name] = value

    def __delete__(self, obj):
        if self.function_name in obj.__dict__:
            del obj.__dict__[self.function_name]


class A:
    @ThreadSafeWritableCachedProperty
    def heavy(self):
        print("Calculating...")
        return 99

a = A()

# print(a.heavy)     # -> "Calculating..." then 99
# print(a.heavy)     # -> 99 (cached)
#
# a.heavy = 123      # Manually override
# print(a.heavy)     # -> 123
#
# del a.heavy        # Delete cached value
# print(a.heavy)     # -> "Calculating..." then 99 again


def funct1(object_test):
    from time import sleep
    sleep(2)
    object_test.heavy = "thread 1 - set 1"

def funct2(object_test):
    from time import sleep
    sleep(2)
    object_test.heavy = "thread 2 - set 2"



t1 = threading.Thread(target=funct1, kwargs={"object_test": a}, daemon=True)
t2 = threading.Thread(target=funct2, kwargs={"object_test": a}, daemon=True)
t1.start()
t2.start()

from time import sleep
sleep(3)

# By adding the lock to the __set__ method - it is ensured that when either thread calls a.heavy = value,
#  - the assignment is thread-safe - then depending on which thread writes last - but without race conditions
print("last line:", a.heavy)
print("last line:", a.heavy)
print("last line:", a.heavy)
