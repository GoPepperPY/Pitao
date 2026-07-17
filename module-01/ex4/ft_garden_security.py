#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, cm: float, age: int) -> None:
        self._name: str = name
        self._cm: float = 0

        if cm < 0:
            self._cm = 0
            print(f"{self._name}: Error, height can't be negative")
        else:
            self._cm = cm

        if age < 0:
            self._age = 0
            print(f"{self._name}: Error, Age can't be negative")
        else:
            self._age = age

    def set_height(self, heigth: float) -> None:
        if heigth >= 0:
            self._cm = heigth
            print(f"Height updated: {self._cm}")
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected!")

    def set_age(self, age: int) -> None:
        if age >= 0:
            self._age = age
            print(f"Age updated: {self._age}")
        else:
            print(f"{self._name}: Error, Age can't be negative")
            print("Age update rejected!")

    def get_height(self) -> float:
        return self._cm

    def get_age(self) -> int:
        return self._age

    def get_info(self) -> None:
        print(f"{self._name}: {round(self.get_height(), 1)} "
              f"cm, {self.get_age()} days")


def main() -> None:
    print("=== Garden Security System ===")

    plant = Plant("rose", 15, 10)

    print("Plant created: ", end="")
    plant.get_info()

    print()

    plant.set_height(25.0)
    plant.set_age(30)

    print()

    plant.set_height(-1)
    plant.set_age(-1)

    print()

    print("Current state: ", end="")
    plant.get_info()


if __name__ == "__main__":
    main()
