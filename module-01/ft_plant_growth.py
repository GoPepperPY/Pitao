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
		print(f"{self.name}: {round(self.cm, 1)} cm, {self.age_plant} days old")

def main() -> None:
	plant1 =	Plant("Sunflower", 25.9, 35)
	plant2 =	Plant("Rose", 23.5, 56)
	plants:		list = [plant1, plant2]
	count:		float = 0

	initial = {plant.name: plant.cm for plant in plants}

	for days in range(1, 8):
		print(f"===Days {days}===")
		for plant in plants:
			plant.print_info()
			plant.grow()
			plant.age()
			count += .2
		print("\n")
	print(f"\nGrowth this week: {round(count, 1)}")
	for plant in plants:
		growth = round(plant.cm - initial[plant.name], 1)
		print(f" 	{plant.name}: +{growth} cm")

if __name__ == "__main__":
    main()
