from math import sqrt
import time
import asyncio

def lucas():
    yield 2
    a = 2
    b = 1
    while True:
        yield b
        a, b = b, a + b


def search(iterable, predicate):
    for item in iterable:
        if predicate(item):
            return item
    raise ValueError("Not found")


async def search(iterable, predicate):
    for item in iterable:
        if await predicate(item):
            return item
    raise ValueError("Not found")


async def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
        await asyncio.sleep(0)
    return True


async def print_matches(iterable, async_predicate):
    for item in iterable:
        matches = await async_predicate(item)
        if matches:
            print("Found :", item, end= ", ")


async def repetitive_message(message, interval_seconds):
    while True:
        print(message)
        await asyncio.sleep(interval_seconds)

""" Futures """

async def monitored_search(iterable, predicate, future):
    """ Updated the search status in a "future" object.
    """
    try:
        found_item = await search(iterable, predicate)
    except ValueError as not_found:
        future.set_exception(not_found)
    else:
        future.set_result(found_item)


async def monitor_future(future, interval_seconds):
    while not future.done():
        print('Waiting...')
        await asyncio.sleep(interval_seconds)
    print('Done.')


async def thirteen_digit_prime(x):
    return (await is_prime(x)) and len(str(x)) == 13
