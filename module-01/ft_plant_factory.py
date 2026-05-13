#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, cm: int, age: int) -> None:
        self.name: str = name
        self.cm: int = cm
        self.age: int = age

    def print_info(self) -> None:
        print(f"Created: {self.name}: {self.cm} cm, {self.age} days old")

def main() -> None:
    plants: list[Plant] = [
        Plant("Sunflower", 30, 10),
        Plant("Rose",      15, 5),
        Plant("Cactus",    10, 100),
        Plant("Tulip",     20, 7),
        Plant("Fern",      25, 14),
    ]

    print("=== Plant Factory ===")
    for plant in plants:
        plant.print_info()

if __name__ == "__main__":
    main()