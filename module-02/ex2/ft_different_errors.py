#!/usr/bin/env python3

def test_error_types(operation_number: int, error: Exception) -> None:
    if operation_number == 0:
        print(f"Caught ValueError: {error}")
    if operation_number == 1:
        print(f"Caught ZeroDivisionError: {error}")
    if operation_number == 2:
        print(f"Caught FileNotFoundError: {error}")
    if operation_number == 3:
        print(f"Caught TypeError:{error}")


def garden_operations(operation_number: int, data: str) -> None:
    if operation_number == 0:
        try:
            if int(data):
                print("Operation completed successfully")
        except ValueError as error:
            test_error_types(operation_number, error)
    if operation_number == 1:
        try:
            10 / int(data)
        except ZeroDivisionError as error:
            test_error_types(operation_number, error)
    if operation_number == 2:
        try:
            open(data)
        except FileNotFoundError as error:
            test_error_types(operation_number, error)
    if operation_number == 3:
        try:
            print("ola" + operation_number)
        except TypeError as error:
            test_error_types(operation_number, error)
    if operation_number == 4:
        print("Operation completed successfully")


def main() -> None:
    print("Testing operation 0...")
    garden_operations(0, "10")
    print("Testing operation 1...")
    garden_operations(1, "0")
    print("Testing operation 2...")
    garden_operations(2, "/non/existent/file")
    print("Testing operation 3...")
    garden_operations(3, "result.txt")
    print("Testing operation 4...")
    garden_operations(4, "")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    main()
