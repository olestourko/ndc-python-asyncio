import asyncio
from coop.main_asyncio import (repetitive_message, print_matches, is_prime, lucas)
from coop.main_asyncio import monitored_search

if __name__ == '__main__':
    scheduler = asyncio.get_event_loop()
    scheduler.create_task(repetitive_message('Some message', 1))
    scheduler.run_forever()