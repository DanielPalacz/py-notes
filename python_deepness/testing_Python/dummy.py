class DummyLogger:
    pass  # Doesn't do anything, just to fulfill the method signature

def some_function(logger: DummyLogger):
    pass  # Function expects a logger but doesn't use it

dummy = DummyLogger()
some_function(dummy)
