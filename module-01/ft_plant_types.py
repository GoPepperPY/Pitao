#!/usr/bin/env python3

class Plant:
	def __init__(self, name: str, cm: float, age_plant: int) -> None:
		self.name: str = name
		self.cm: float = cm
		self.age_plant: int = age_plant

class Flower(Plant):
	def __init__(self, name: str, height: float, age_flower: int, color: str) -> None:
		super().__init__(name, height, age_flower)
		self.color: str = color
		self.__bloom_value = False
	def	bloom(self) -> None:
		self.__bloom_value = True
	def	show(self) -> None:
		print(	f"{self.name}: {round(self.cm, 1)}cm, {self.age_plant} days old\n"
				f"Color: {self.color}")
		if self.__bloom_value == True:
			print(f"{self.name} is blooming beautifully!")
		else :
			print(f"{self.name} has not bloomed yet")

class Tree(Plant):
	def	__init__(self, name: str, height: float, age_tree: int, trunk_diameter: float):
		super().__init__(name, height, age_tree)
		self.trunk_diameter = trunk_diameter
	def	produce_shade(self) -> None:
		print(f"Tree {self.name} now produces a shade of {round(self.cm, 1)}cm long and {round(self.trunk_diameter, 1)}cm wide.")
	def	show(self) -> None:
		print(	f"{self.name}: {round(self.cm, 1)}cm, {self.age_plant} days old "
				f"Trunk Diameter: {self.trunk_diameter}\n")

class Vegetable(Plant):
	def __init__(self, name: str, cm: float, age_plant: int, harvest_season: str, nutritional_value: int):
		super().__init__(name, cm, age_plant)
		self.harvest_season = harvest_season
		self.nutritional_value = nutritional_value
	def grow(self) -> None:
		self.cm += .4
		self.nutritional_value += 1
	def age(self) -> None:
		self.age_plant += 1
	def	show(self) -> None:
		print(	f"{self.name}: {round(self.cm, 1)}cm, {self.age_plant} days old, "
				f"Harvest Season: {self.harvest_season}, Nutritional Value: {self.nutritional_value}")

def main() -> None:

	"""<------ Flowers ------>"""
	flower_data: list[Flower] = [
		Flower("Rose", 15.2, 31, "Red"),
		Flower("Flame Lily", 20.4, 10, "White")
	]

	"""<------ Trees ------>"""
	tree_data: list[Tree] = [
		Tree("Oak", 2000, 6000, 30),
		Tree("Pine", 800, 4000, 20)
	]

	"""<------ Vegetable ------>"""
	vegetable_data: list[Vegetable] = [
		Vegetable("tomato", 40, 80, "summer", 0),
        Vegetable("carrot", 60, 75, "fall", 0)
	]

	"""<------ Flowers ------>"""
	for	plant in flower_data:
		plant.show()
		plant.bloom()
		plant.show()
		print("\n")

	"""<------ Trees ------>"""
	for	plant in tree_data:
		plant.produce_shade()
		plant.show()

	"""<------ Vegetable ------>"""

	for	plant in vegetable_data:
		plant.show()
		for	x in range(1, 21):
			plant.grow()
			plant.age()
		plant.show()
		print("\n")


if __name__ == "__main__":
    main()
