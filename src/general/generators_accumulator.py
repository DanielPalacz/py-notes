def accumulator():
    total = 1
    value = None
    while True:
        print("value (before yield):", value)
        value = yield total

        if value is None:
            break

        print("value (after yield):", value)

        total += value

gen = accumulator()

# print(next(gen))       # Start generator, output: 1
print(gen.send(None))    # Start generator, output: 1
print(gen.send(10))    # Add 10, output: 11
print(gen.send(10))    # Add 10, output: 21
print(gen.send(20))    # Add 20, output: 41
# gen.send(None)         # Stop generator


print()
print("gen2 iteration:")
gen2 = accumulator()

# value (before yield): None
# print(next(gen2))    # Start generator, output: 1
print(gen2.send(None)) # Start generator, output: 1
# value (after yield): 1
# value (before yield): 1

print(gen2.send(1))    # Add 1, output: 2
# value (after yield): 1
# value (before yield): 1

print(gen2.send(1))    # Add 1, output: 3
# value (after yield): 2
# value (before yield): 2

print(gen2.send(2))    # Add 2, output: 5
