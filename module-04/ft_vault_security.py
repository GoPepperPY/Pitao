#!/usr/bin/env python3

import sys
import typing

def secure_archive(name: str) -> tuple[bool, str]:
	try:
		with open(name) as f:
			content = f.read()
			return(True, content)
	except FileNotFoundError as e:
		return(False, str(e))
	except PermissionError as e:
		return(False, str(e))

def main() -> None:
	bool_value, content = secure_archive(sys.argv[1])
	print(bool_value)
	print(content)

if __name__ == "__main__":
	main()