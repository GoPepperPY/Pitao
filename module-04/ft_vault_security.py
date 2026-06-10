#!/usr/bin/env python3

import sys
import typing

def secure_archive(name: str) -> tuple[bool, str]:
	try:
		file: typing.IO = open(name)
		content = file.read()
		return (True, content)
	except ValueError as e:
		return(False, e)
	except PermissionError as e:
		return(False, e)

def main() -> None:
	bool_value, content = secure_archive(sys.argv[1])
	print(bool_value)
	print(content)

if __name__ == "__main__":
	main()