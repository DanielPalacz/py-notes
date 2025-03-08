import asyncio


async def my_coroutine():
    print("Start")
    await asyncio.sleep(1)
    print("End")


async def main():
    task = asyncio.create_task(my_coroutine())
    print(type(task))
    print("Task created")
    await task


asyncio.run(main())
