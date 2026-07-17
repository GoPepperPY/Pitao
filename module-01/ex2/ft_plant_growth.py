#!/usr/bin/env python3

class Plant:

    def __init__(self, name: str, cm: float, age_plant: int) -> None:
        self.name:		str = name
        self.age_plant:	int = age_plant
        self.cm:		float = cm

    def grow(self) -> None:
        self.cm += .2

    def age(self) -> None:
        self.age_plant += 1

    def print_info(self) -> None:
        print(f"{self.name}: {round(self.cm, 1)} cm, "
              f"{self.age_plant} days old")


def main() -> None:
    plant1 = Plant("Sunflower", 25.9, 35)
    count = plant1.cm
    plant1.print_info()
    for days in range(1, 8):
        print(f"===Days {days}===")
        plant1.print_info()
        plant1.grow()
        plant1.age()
    print(f"\nGrowth this week: {round(plant1.cm - count, 1)}cm")


if __name__ == "__main__":
    main()
