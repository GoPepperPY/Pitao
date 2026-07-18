#!/usr/bin/env python3

import sys


def main() -> None:
    if len(sys.argv) == 1:
        print("No valid items provided!")
        return
    inventory: dict = {}
    for arg in sys.argv[1:]:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue
        parts = arg.split(":")
        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue
        name = parts[0]
        quantity_str = parts[1]
        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue
        try:
            quantity = int(quantity_str)
        except ValueError as e:
            print(f"Quantity error for '{name}': {e}")
            continue
        inventory.update({name: quantity})

    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    print(f"Total quantity of the {len(inventory.keys())} items:"
          f" {sum(inventory.values())}")
    for argv in inventory.keys():
        res = round((inventory[argv] / sum(inventory.values())) * 100, 1)
        print(f"Item {argv} represents {res}%")
    most = list(inventory.keys())[0]
    least = list(inventory.keys())[0]
    for item in inventory.keys():
        if inventory[item] > inventory[most]:
            most = item
        if inventory[item] < inventory[least]:
            least = item
    print(f"Item most abundant: {most} with quantity {inventory[most]}")
    print(f"Item least abundant: {least} with quantity {inventory[least]}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
