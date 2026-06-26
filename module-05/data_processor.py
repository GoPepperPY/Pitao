#!/usr/bin/env python3

from typing import Any
import abc

class DataProcessor(abc.ABC):
	def	__init__(self):
		self._data: list[tuple[int, str]] = []
		self._next_rank: int = 0
	@abc.abstractmethod
	def validate(self, data: Any) -> bool:
		...

	@abc.abstractmethod
	def ingest(self, data: Any) -> None:
		...

	def output(self) -> tuple[int, str]:
		return self._data.pop(0)

class NumericProcessor(DataProcessor):
	def __init__(self):
		super().__init__()

	def validate(self, data: Any) -> bool:
		if isinstance(data, list):
			return all(isinstance(item, (int, float)) for item in data)
		return isinstance(data, (int, float))

	def ingest(self, data: Any) -> None:
		if isinstance(data, list) and all(isinstance(item, (int, float)) for item in data):
			for pos in data:
				self._data.append((self._next_rank, str(pos)))
				self._next_rank += 1
		elif isinstance(data, (int, float)):
			self._data.append((self._next_rank, str(data)))
			self._next_rank += 1
		else:
			print("Got exception: Improper numeric data")

class TextProcessor(DataProcessor):
	def __init__(self):
		super().__init__()
	def validate(self, data: Any) -> bool:
		if isinstance(data, list):
			return all(isinstance(item, str) for item in data)
		return isinstance(data, str)

	def ingest(self, data: Any) -> None:
		if isinstance(data, list):
			for pos in data:
				self._data.append((self._next_rank, pos))
				self._next_rank += 1
		else:
			self._data.append((self._next_rank, data))
			self._next_rank += 1

class LogProcessor(DataProcessor):
	def __init__(self):
		super().__init__()
	def validate(self, data: Any) -> bool:
		...
	def ingest(self, data: Any) -> None:
		...

def main() -> None:
	# NumericProcessor_list: list[NumericProcessor] = [1, 2, 3, 4, 5]
	NumericProcessor_var = NumericProcessor()
	print(f"Testing Numeric Processor...")
	print(f"Trying to validate input '12, 15, 54': {NumericProcessor_var.validate([12, 15, 54])}")
	print(f"Trying to validate input 'Hello': {NumericProcessor_var.validate('Hello')}\n")
	NumericProcessor_var.ingest([12, 15, 54])
	print("Extracting 3 values...")
	rank, value = NumericProcessor_var.output()
	print(f"Numeric value {rank}: {value}")
	rank, value = NumericProcessor_var.output()
	print(f"Numeric value {rank}: {value}")
	rank, value = NumericProcessor_var.output()
	print(f"Numeric value {rank}: {value}")

	TextProcessor_var = TextProcessor()
	print(f"\nTesting Text Processor...")
	print(f"Trying to validate input '12': {TextProcessor_var.validate(12)}")
	print(f"Trying to validate input 'Hello': {TextProcessor_var.validate('Hello')}")

	# for a in NumericProcessor_list:
	# 	print(a)

if __name__ == "__main__":
    main()