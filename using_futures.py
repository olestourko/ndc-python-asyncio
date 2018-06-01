import asyncio
from coop.main_asyncio import monitored_search, monitor_future, lucas, thirteen_digit_prime

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    future = loop.create_future()
    coroutine_object = monitored_search(lucas(), thirteen_digit_prime, future)
    loop.create_task(coroutine_object)
    loop.create_task(monitor_future(future, 1.0))
    loop.run_until_complete(future)
    print(future.result())
    loop.close()
