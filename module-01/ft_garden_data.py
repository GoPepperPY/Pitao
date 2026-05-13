#!/usr/bin/env python3

class Plant:
	def __init__(self, name: str, age: int, cm: int) -> None:
		self.name:	str = name
		self.age:	int = age
		self.cm:	int = cm

def main() -> None:
	plant1 = Plant("Rose", 25, 30)
	plant2 = Plant("Sunflower", 80, 45)
	plant3 = Plant("Cactus", 15, 120)

	print(f"{plant1.name}: {plant1.cm} cm, {plant1.age} days old")
	print(f"{plant2.name}: {plant2.cm} cm, {plant2.age} days old")
	print(f"{plant3.name}: {plant3.cm} cm, {plant3.age} days old")

if __name__ == "__main__":
	main()