
class CountCalls:

    def __init__(self, fun):
        self.func = fun
        self.num_calls = 0
        print("[Decorator Syntax logic check][CountCalls][__init__] CountCalls instance init happened.")

    def __new__(cls, *args, **kwargs):
        print("[Decorator Syntax logic check][CountCalls][__new__] "
              "Creating a new instance of CountCalls decorator/class [args: ", *args, "; ", kwargs, "].", sep="")
        return super().__new__(cls)

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print("Number of calls:", self.num_calls)
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print("hello")

# say_hello()
# say_hello()
# say_hello()
