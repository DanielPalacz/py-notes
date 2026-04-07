

# nonlocal k

def hello():
    k = 21

    def aiii():
        nonlocal k
        k = k + 1
        print(k)

    aiii()

    k += 1
    return k


print(hello())
