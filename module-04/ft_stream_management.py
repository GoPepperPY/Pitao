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
		sys.stdout.write("Enter new file name (or empty): ")
		sys.stdout.flush()
		new_file_name = sys.stdin.readline()
		new_file_name = new_file_name.split('\n')
		if len(new_file_name[0]) == 0:
			print("Not saving data.")
			return
		try:
			print(f"Saving data to '{new_file_name[0]}'")

			new_file: typing.IO = open(new_file_name[0], "w")
			new_file.write('\n'.join(new_line))
			new_file.close()
			print(f"Data saved in file '{new_file_name[0]}'.")
		except FileNotFoundError as e:
			sys.stderr.write(e)
		except PermissionError as e:
			sys.stderr.write(e)
	except FileNotFoundError as e:
		sys.stderr.write(e)
	except PermissionError as e:
		sys.stderr.write(e)
if __name__ == "__main__":
	main()