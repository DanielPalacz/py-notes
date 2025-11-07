import asyncio


async def task_1():
    await asyncio.sleep(1)
    raise ValueError("Błąd w task_1")


async def task_2():
    await asyncio.sleep(1)
    raise TypeError("Błąd w task_2")


async def task_3():
    await asyncio.sleep(1)
    return "Zadanie 3 zakończone poprawnie"


async def main():
    try:
        results = await asyncio.gather(task_1(), task_2(), task_3(), return_exceptions=True)
        # Przechwytywanie wyjątków w grupie
        errors = [e for e in results if isinstance(e, Exception)]
        if errors:
            raise ExceptionGroup("Błędy z asyncio.gather", errors)

        print(f"Wyniki: {results}")

    except* ValueError as e:
        print(f"Obsłużono ValueError: {e}")
    except* TypeError as e:
        print(f"Obsłużono TypeError: {e}")
    except* Exception as e:
        print(f"Obsłużono ogólny wyjątek: {e}")


asyncio.run(main())
