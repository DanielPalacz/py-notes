import asyncio


# def print_something():
#     print("print_something")
#     x = await print_something2


async def print_something1():
    print("print_something1")


async def print_something2():
    print("print_something2")
    something = print_something1()
    print(something)

# print_something()


asyncio.run(print_something1())
asyncio.run(print_something2())
