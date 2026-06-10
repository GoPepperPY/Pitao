#!/usr/bin/env python3

import sys
import typing

def main() -> None:
	try :
		print(f"Accessing file '{sys.argv[1]}'")
		file: typing.IO = open(sys.argv[1])
		content = file.read()
		print(content)
		file.close()
	except FileNotFoundError as e:
		print(e)
	except PermissionError as e:
		print (e)
	print(f"File {sys.argv[1]} closed.")
if __name__ == "__main__":
	main()