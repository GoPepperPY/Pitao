#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "The tomato plant is wilting!") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Not enough water in the tank!") -> None:
        super().__init__(message)


def test_plant_error() -> None:
    print("Testing PlantError...")
    try:
        raise PlantError()
    except PlantError as e:
        print(f"Caught PlantError: {e}")


def test_water_error() -> None:
    print("Testing WaterError...")
    try:
        raise WaterError()
    except WaterError as e:
        print(f"Caught WaterError: {e}")


def test_all_garden_errors() -> None:
    print("Testing catching all garden errors...")
    for error in [PlantError(), WaterError()]:
        try:
            raise error
        except GardenError as e:
            print(f"Caught GardenError: {e}")


def main() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    test_plant_error()
    print()
    test_water_error()
    print()
    test_all_garden_errors()
    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    main()
