
def state_machine():
    state = "IDLE"
    while True:
        command = yield f"Stan: {state}"

        if command == "get" or command is None:
            pass  # nie zmieniaj stanu
        elif command == "start":
            state = "RUNNING"
        elif command == "stop":
            state = "STOPPED"
        elif command == "reset":
            state = "IDLE"
        else:
            state = "ERROR"

# machine = state_machine()
# print(next(machine))           # Stan: IDLE
# print(machine.send("start"))   # Stan: RUNNING
# print(next(machine))           # Stan: RUNNING — sprawdzamy stan pasywnie
# print(machine.send("stop"))    # Stan: STOPPED
# print(machine.send("get"))     # Stan: STOPPED

