import asyncio

async def task1():
    await asyncio.sleep(1)
    print("Task 1 done")

async def task2():
    await asyncio.sleep(2)
    print("Task 2 done")

async def task3():
    await asyncio.sleep(3)
    print("Task 3 done")

async def main():
    # Uruchamiamy wszystkie zadania jednocześnie i czekamy na ich zakończenie
    await asyncio.gather(task1(), task2(), task3())

# Uruchomienie event loop
asyncio.run(main())
