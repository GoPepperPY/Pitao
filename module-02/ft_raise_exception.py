#!/usr/bin/env python3

def	input_temperature(temp_str: str) -> int:
	return int(temp_str)

def	test_temperature(tmp: str) -> None:
	try:
		print(f"Temperature is now {input_temperature(tmp)}°C\n")
	except ValueError as e:
		print(f"Caught input_temperature error: invalid literal for int() with base 10: {e}\n")

def	main() -> None:
	print("=== Garden Temperature ===\n")
	print("Input data is '25'")
	test_temperature("25")
	print("Input data is 'abc'")
	test_temperature("abc")
	print("All tests completed - program didn't crash!")

if __name__ == "__main__":
    main()