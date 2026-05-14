#!/usr/bin/env python3

class Plant:
	def __init__(self, name: str, cm: float, age_plant: int) -> None:
		self.name: str = name
		self.cm: float = cm
		self.age_plant: int = age_plant
		self.__age_counter = 0
		self.__show_counter = 0
		self.__grow_counter = 0
	def age(self) -> None:
		self.age_plant += 1
		self.__age_counter += 1
	def grow(self) -> None:
		self.cm += 2
		self.__grow_counter += 1
	def	show(self) -> None:
		print(f"{self.name} plant: {self.cm}, {self.age_plant} days old")
		self.__show_counter += 1
	def show_stats(self) -> None:
		print(	f"[statistics for {self.name}]\n"
				f"Stats: {self.__grow_counter} grow, {self.__age_counter} age, {self.__show_counter} show")

	@staticmethod
	def is_older_than_year(age: int) -> bool:
		return age > 365

	@classmethod
	def anonymous(self) -> "Plant":
		return self("Unknown Plant", 0.0, 0)


class Flower(Plant):
	def __init__(self, name: str, height: float, age_flower: int, color: str) -> None:
		super().__init__(name, height, age_flower)
		self.color: str = color
		self.__bloom_value = False
	def	bloom(self) -> None:
		self.__bloom_value = True
	def	show_flower(self) -> None:
		self.show()
		print(f"Color: {self.color}")
		if self.__bloom_value == True:
			print(f"{self.name} is blooming beautifully!")
		else :
			print(f"{self.name} has not bloomed yet")



class Tree(Plant):
	def	__init__(self, name: str, height: float, age_tree: int, trunk_diameter: float):
		super().__init__(name, height, age_tree)
		self.trunk_diameter = trunk_diameter
		self.__age_counter = 0
		self.__show_counter = 0
		self.__grow_counter = 0
		self.__shadow_counter = 0
	def	produce_shade(self) -> None:
		print(f"Tree {self.name} now produces a shade of {round(self.cm, 1)}cm long and {round(self.trunk_diameter, 1)}cm wide.")
		self.__shadow_counter += 1
	def	show_tree(self) -> None:
		self.show()
		print(f"Trunk Diameter: {self.trunk_diameter}cm")
		self.__show_counter += 1
	def show_stats_tree (self) -> None:
		self.show_stats()
		print(f" {self.__shadow_counter} shadow")




class Seed(Flower):
	def __init__(self, name: str, height: float, age_flower: int, color: str, seeds: int):
		super().__init__(name, height, age_flower, color)
		self.seeds = seeds
	def	show_seed(self) -> None:
		self.show_flower()
		print(f"Seeds: {round(self.seeds)}")
	def	grow_seed(self) -> None:
		self.seeds += 2.1

def main() -> None:

	"""<------ Flowers ------>"""
	flower_data: list[Flower] = [
		Flower("Rose", 15.0, 10, "Red")
	]

	"""<------ Trees ------>"""
	tree_data: list[Tree] = [
		Tree("Oak", 200.0, 365, 5.0)
	]

	"""<------ Trees ------>"""
	seed_data: list[Seed] = [
		Seed("Sunflower", 80.0, 45, "Yellow", 0)
	]


	print(f"\nIs Oak older than a year? {Plant.is_older_than_year(45)}")
	print(f"\nIs Oak older than a year? {Plant.is_older_than_year(400)}\n")

	"""<------ Flowers ------>"""
	print("=== FLOWER ===")
	for	plant in flower_data:
		plant.show_flower()
		plant.show_stats()
		print("[asking the rose to grow and bloom]")
		for x in range(1, 7):
			plant.grow()
		plant.bloom()
		plant.show_flower()
		print("[statistics for Rose]")
		plant.show_stats()
	print("\n")

	"""<------ Trees ------>"""
	print("=== TREES ===")
	for	plant in tree_data:
		plant.show()
		plant.show_stats_tree()
		print("[asking the oak to produce shade]")
		plant.produce_shade()
		plant.show_stats_tree()
	print("\n")

	"""<------ SEED ------>"""
	print("=== SEED ===")
	for	plant in seed_data:
		plant.show_seed()
		print("[make sunflower grow, age and bloom]")
	plant.bloom()
	for	x in range(1, 21):
		plant.grow_seed()
		plant.grow()
		plant.age()
	plant.show_seed()
	plant.show_stats()
	print("\n")

	# Classmethod demo
	unknown = Plant.anonymous()
	unknown.show()
	unknown.show_stats()

if __name__ == "__main__":
    main()
