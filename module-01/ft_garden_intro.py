#!/usr/bin/env python3

def info() -> None:
	name:	str = "rose"
	height:	str = "15 cm"
	age:	str = "30 Days"

	print("=== Welcome to My Garden ===")
	print("Plant: " + name)
	print("Height: " + height)
	print("Age: " + age)
	print("\n=== End of Program ===")

if __name__ == "__main__":
	info()