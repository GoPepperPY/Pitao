#!/usr/bin/env python3

def	input_temperature(temp_str: str) -> int:
	return int(temp_str)

def	test_temperature(tmp: str) -> None:
	try:
		if input_temperature(tmp) >= 0 and input_temperature(tmp) <= 40:
			print(f"Temperature is now {input_temperature(tmp)}°C\n")
		if input_temperature(tmp) > 40:
			print(f"Caught input_temperature error: {tmp} is too hot for plants (max 40°C)\n")
		if input_temperature(tmp) < 0:
			print(f"Caught input_temperature error: {tmp} is too cold for plants (min 0°C)\n")
	except ValueError as e:
		print(f"Caught input_temperature error: invalid literal for int() with base 10: {e}\n")

def	main() -> None:
	print("=== Garden Temperature ===\n")
	print("Input data is '25'")
	test_temperature("25")
	print("Input data is 'abc'")
	test_temperature("abc")
	print("Input data is '100'")
	test_temperature("100")
	print("Input data is '-50'")
	test_temperature("-50")
	print("All tests completed - program didn't crash!")

if __name__ == "__main__":
    main()