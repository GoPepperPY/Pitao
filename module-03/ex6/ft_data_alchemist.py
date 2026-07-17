#!/usr/bin/env python3

import random


def main() -> None:
    names: list = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma',
                   'Gregory', 'john', 'kevin', 'Liam']
    new_list: list = []
    new_list_caps: list = []
    alchemist: dict = {}
    print(f"Initial list of players: {names}\n")
    for name in names:
        new_list.append(name.capitalize())
    print(f"New list with all names capitalize: {new_list}\n")
    for name in names:
        if name == name.capitalize():
            new_list_caps.append(name)
    print(f"New list with capitalized names: {new_list_caps}\n")
    for name in names:
        alchemist.update({name: random.randint(1, 999)})
    print(f"Score dict: {alchemist}\n")
    print(f"Score average is "
          f"{round(sum(alchemist.values()) / len(alchemist.keys()), 2)}\n")
    alchemist_high = {name: alchemist[name] for name in alchemist
                      if alchemist[name] >
                      sum(alchemist.values()) / len(alchemist.keys())}
    print(f"High scores: {alchemist_high}")


if __name__ == "__main__":
    main()
