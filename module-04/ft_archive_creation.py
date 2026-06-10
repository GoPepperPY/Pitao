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
		print(f"File {sys.argv[1]} closed.")
		lines = content.split('\n')
		new_line:list = []
		for line in lines:
			new_line.append(line + '#')
		new_content = '\n'.join(new_line)
		print(f"\n\n===Transformed Data: ===\n{new_content}")
		new_file_name = input("Enter new file name (or empty): ")
		if len(new_file_name) == 0:
			print("Not saving data.")
			return
		try:
			print(f"Saving data to '{new_file_name}'")

			new_file: typing.IO = open(new_file_name, "w")
			new_file.write('\n'.join(new_line))
			new_file.close()
			print(f"Data saved in file '{new_file_name}'.")
		except FileNotFoundError as e:
			print(e)
		except PermissionError as e:
			print (e)
	except FileNotFoundError as e:
		print(e)
	except PermissionError as e:
		print (e)
if __name__ == "__main__":
	main()