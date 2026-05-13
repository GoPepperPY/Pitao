#!/usr/bin/env python3

class Plant:
	def __init__(self, name: str, cm: int, age: int) -> None:
		self.name: str = name
		self.cm: int = 0
		self.age: int = 0
		self.set_age(age)
		self.set_height(cm)

	def	set_height(self, heigth) -> None:
		if(heigth > 0) :
			self.cm = heigth
			print(f"Height updated: {self.cm}")
		else :
			print(f"{self.name}: Error, height can't be negative")
			print(f"Height update rejected!")

	def	set_age(self, age) -> None:
		if(age > 0) :
			self.age = age
			print(f"Age updated: {self.age}")
		else :
			print(f"{self.name}: Error, Age can't be negative")
			print(f"Age update rejected!")

	def get_height(self) -> int:
		return	self.cm

	def get_age(self) -> int:
		return	self.age

	def get_info(self) -> None:
		print(	f"Current plant: {self.name}"
				f" ({self.get_height()} cm, {self.get_age()} days)")

def	main() -> None:
	plants: list[tuple[str, int, int]] = [
		('Rose',		25, 37),
		('Sunflower',	-25, 37),
		('Oak',			25, 37),
		('Cactus',		25, -37),
		('Fern',		25, 37),
	]

	plants_info: list[Plant] =	[Plant(name, height, age) 
								for name, height, age in plants]

	for plant in plants_info:
		plant.get_info()

if __name__ == "__main__":
    main()
