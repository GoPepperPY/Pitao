#!/usr/bin/env python3

import sys

def main() -> None:
	print(f"Program name: {sys.argv[0]}")
	if len(sys.argv) <= 1: 
		print("No arguments provided!")
	else:
		print(f"Arguments received: {len(sys.argv) - 1}")
		for n in range(1, len(sys.argv)):
			print(f"{sys.argv[n]}")
	print(f"Total arguments: {len(sys.argv)}")
if __name__ == "__main__":
    main()