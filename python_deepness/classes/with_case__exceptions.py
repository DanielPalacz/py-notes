
class MyContext:
    def __init__(self, exc_name):
        self.exc_name = exc_name

    def __enter__(self):
        print("Enter - 1:", self.exc_name)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Exception: {exc_type} - 3")
        if exc_type == self.exc_name:
            return True  # tłumi wyjątek

        return False


with MyContext(ValueError):
    print("Inside with - 2")
    raise ValueError("Something went wrong")

print("Program continues - 4")

# Enter - 1
# Inside with - 2
# Exception: <class 'ValueError'> - 3
# Program continues - 4
