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
	def grow(self) -> None:
		self.cm += .2
	def age(self) -> None:
		self.age_plant += 1
	def	bloom(self) -> None:
		print(f"{self.name} is blooming beautifully!")
	def	show(self) -> None:
		print(	f"{self.name}: {round(self.cm, 1)}cm, {self.age_plant} days old\n"
				f"Color: {self.color}\n")

class Tree(Plant):
	def	__init__(self, name: str, height: float, age_tree: int, trunk_diameter: float):
		super().__init__(name, height, age_tree)
		self.trunk_diameter = trunk_diameter
	def	produce_shade(self) -> None:
		print(f"Tree {self.name} now produces a shade of {round(self.cm, 1)}cm long and {round(self.trunk_diameter, 1)}cm wide.")
	def grow(self) -> None:
		self.cm += 2.2
	def age(self) -> None:
		self.age_plant += 1
	def	show(self) -> None:
		print(	f"{self.name}: {round(self.cm, 1)}cm, {self.age_plant} days old\n"
				f"Trunk Diameter: {self.trunk_diameter}\n")

def main() -> None:

	"""<------ Flowers ------>"""
	flower_data: list[Flower] = [
		Flower("Rose", 15.2, 31, "Red")
	]

	"""<------ Trees ------>"""
	tree_data: list[Tree] = [
		Tree("Oak", 2000, 6000, 30)
	]




	"""<------ Flowers ------>"""
	print("=== FLOWER ===")
	for	plant in flower_data:
		# plant.bloom()
		plant.show()

	"""<------ Trees ------>"""
	print("=== TREES ===")
	for	plant in tree_data:
		# plant.produce_shade()
		plant.show()


if __name__ == "__main__":
    main()
