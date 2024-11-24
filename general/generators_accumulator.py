def accumulator():
    total = 1
    while True:
        value = yield total
        if value is None:
            break
        total += value

gen = accumulator()

# print(next(gen))       # Start generator, output: 1
print(gen.send(None))    # Start generator, output: 1
print(gen.send(10))    # Add 10, output: 11
print(gen.send(10))    # Add 10, output: 11
print(gen.send(20))    # Add 20, output: 31
gen.send(None)         # Stop generator
