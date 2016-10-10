import random
import time


def events(max_delay, limit):
    while True:
        delay = random.randint(1, max_delay)
        if delay >= limit:
            time.sleep(limit)
            yield None
        else:
            time.sleep(delay)
            yield 'Event generated, awaiting %d s ' % delay