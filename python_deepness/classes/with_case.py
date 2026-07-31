
class MyContext:
    def __enter__(self):
        print("Enter - 1")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Exception: {exc_type} - 3")
        return True  # tłumi wyjątek


with MyContext():
    print("Inside with - 2")
    raise ValueError("Something went wrong")

print("Program continues - 4")

# Enter - 1
# Inside with - 2
# Exception: <class 'ValueError'> - 3
# Program continues - 4
