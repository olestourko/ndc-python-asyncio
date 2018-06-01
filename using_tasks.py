import asyncio
from coop.main_asyncio import search, monitor_future, lucas, thirteen_digit_prime

""" Tasks are subclasses of Futures. They wrap a coroutine in a future. """
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    search_task = asyncio.ensure_future(
        search(lucas(), thirteen_digit_prime),
        loop=loop
    )
    # Can also use: task = loop.create_task(coroutine_object)

    monitor_task = asyncio.ensure_future(
        monitor_future(search_task, 1.0),
        loop=loop
    )

    # Waits for all tasks to return (refer to 44m20s)
    search_and_monitor_future = asyncio.gather(
        search_task,
        monitor_task
    )

    loop.run_until_complete(search_and_monitor_future)
    print(search_task.result())
    loop.close()
