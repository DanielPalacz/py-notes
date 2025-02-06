from itertools import count
import gc

class A:
    def __init__(self):
        self.name = "a"

print("Initial GC count:", gc.get_count())
gc_objects_init = [id(obj) for obj in gc.get_objects()]

for number in count():

    A() # - Python ignores it. Reference counting is used here. It is clear from Python point of view. But how system deals with it?

    if number % 5000000 == 0:
        # gc_objects = gc.get_objects() # it increases (+1) number of Garbage Collector tracked objects - causing Memory Leak
        #print(len(gc_objects))
        dir_obj = dir()
        print(len(gc.get_objects()))

        print([type(obj) for obj in gc.get_objects() if id(obj) not in gc_objects_init]) # new objects
        print("GC counter:", gc.get_count())
        # del gc_objects # it solves the issue

