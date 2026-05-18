#!/usr/bin/env python3

class GardenError(Exception):
	def __init__(self, message: str = "Unknown garden error") -> None:
		super().__init__(message)


class PlantError(GardenError):
	def __init__(self, message: str = "Unknown garden error") -> None:
		super().__init__(message)

def	water_plant(name: str) -> None:
	if name != name.capitalize():
		raise PlantError(f"Invalid plant name to water: {name}")
	print(f"Watering {name}: [OK]")

def test_watering_system(name: list) -> None:
	print("Opening watering system")
	try:
		water_plant(name)
	except PlantError as error:
		print(f"Caught PlantError: {error}")
	finally:
		print("Closing watering system")

def main() -> None:
	test_watering_system("Rose")
	test_watering_system("rose")

if __name__ == "__main__":
    main()