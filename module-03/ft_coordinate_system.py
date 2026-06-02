#!/usr/bin/env python3

import math

def	get_player_pos() -> tuple[float, float, float]:
	while(True):
		user = input("Enter new coordinates as floats in format 'x,y,z': ")

		try:
			p1 ,p2, p3 = user.split(',')
		except ValueError:
			print("Invalid Sintax")
			continue
		try:
			x = float(p1.strip())
		except ValueError as e:
			print(e)
			continue
		try:
			y = float(p2.strip())
		except ValueError as e:
			print(e)
			continue
		try:
			z = float(p3.strip())
		except ValueError as e:
			print(e)
			continue
		return (x, y, z)

def main() -> None:
	print("=== Game Coordinate System ===")

	print("\nGet a first set of coordinates")
	pos1 = get_player_pos()

	print(f"Got a first tuple: {pos1}")
	print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
	dist_center = math.sqrt(pos1[0]**2 + pos1[1]**2 + pos1[2]**2)
	print(f"Distance to center: {round(dist_center, 4)}")

	print("\nGet a second set of coordinates")
	pos2 = get_player_pos()

	dist_2 = math.sqrt(
		(pos2[0] - pos1[0])**2 + (pos2[1] - pos1[1])**2
		+ (pos2[2] - pos1[2])**2
	)
	print(f"Distance between the 2 sets of coordinates: {round(dist_2, 4)}")

if __name__ == "__main__":
	main()