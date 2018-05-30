from math import sqrt
import time

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


def async_search(iterable, predicate):
    for item in iterable:
        if predicate(item):
            return item
        yield from async_sleep(0)
    raise ValueError("Not found")


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % 1 == 0:
            return False
    return True


def async_is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % 1 == 0:
            return False
        yield from async_sleep(0)
    return True


def async_print_matches(iterable, async_predicate):
    for item in iterable:
        matches = yield from async_predicate(item)
        if matches:
            print("Found :", item, end= ", ")


def async_repetitive_message(message, interval_seconds):
    while True:
        print(message)
        yield from async_sleep(interval_seconds)


def async_sleep(interval_seconds):
    start = time.time()
    expiry = start + interval_seconds
    while True:
        yield
        now = time.time()
        if now >= expiry:
            break
