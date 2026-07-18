#!/usr/bin/env python3

import random
import typing


def gen_event() -> typing.Generator:
    pool_names = [
        'Johny', 'Arthur', 'Joseph',
        'Noah', 'William', 'Oliver', 'Jack',
        'Olivia', 'Amelia',
        'Emma', 'Charlotte', 'Ava',
        'Christopher', 'Sarah'
    ]
    pool_event = [
        'Sleep', 'Climb', 'Cook', 'Eat',
        'Love', 'Swim', 'Drawn', 'Drink', 'Fly'
    ]
    while True:
        yield (random.choice(pool_names), random.choice(pool_event))


def main() -> None:
    gen = gen_event()
    for x in range(0, 1000):
        name, action = next(gen)
        print(f"Event {x}: Player {name} did action {action}")
    random_list: list[tuple[str, str]] = []
    for x in range(0, 10):
        random_list.append(next(gen))
    print(f"Built list of {len(random_list)} event: {random_list}")
    while len(random_list) > 0:
        number = random.randint(0, len(random_list) - 1)
        print(f"Got event from list: {random_list[number]}")
        random_list.pop(number)
        print(f"Remains in list: {random_list}")


if __name__ == "__main__":
    main()
