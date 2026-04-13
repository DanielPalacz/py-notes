import asyncio


# def print_something():
#     print("print_something")
#     x = await print_something2


async def print_something1():
    print("[1] print_something1")
    return "[1] print_something1 returned"


async def print_something2():
    print("[2] print_something2")
    something = await print_something1()
    print("[2]", something)

# print_something()


# asyncio.run(print_something1())
asyncio.run(print_something2())
