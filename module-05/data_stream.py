#!/usr/bin/env python3

from typing import Any
import abc


class DataProcessError(Exception):
    def __init__(self, message: str = "Unknown DataProcessor Error") -> None:
        super().__init__(message)
        return


class NumericProcessError(DataProcessError):
    def __init__(self, message: str =
                 "Unknown NumericProcessor Error") -> None:
        super().__init__(message)
        return


class TextProcessError(DataProcessError):
    def __init__(self, message: str = "Unknown TextProcessor Error") -> None:
        super().__init__(message)
        return


class LogProcessError(DataProcessError):
    def __init__(self, message: str = "Unknown LogProcessor Error") -> None:
        super().__init__(message)
        return


class DataProcessor(abc.ABC):
    def __init__(self):
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
            raise NumericProcessError()


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
            elif isinstance(data, str):
                self._data.append((self._next_rank, data))
                self._next_rank += 1
            else:
                raise TextProcessError()


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return all(
                isinstance(item, dict)
                and all(
                    isinstance(x1, str) and isinstance(x2, str)
                    for x1, x2 in item.items()
                )
                for item in data
            )
        return all(
                isinstance(item, dict)
                and all(
                    isinstance(x1, str) and isinstance(x2, str)
                    for x1, x2 in item.items()
                )
                for item in data
            )

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise LogProcessError()
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._data.append(
                (self._next_rank, f"{item['log_level']}: {item['log_message']}")
            )
            self._next_rank += 1


class DataStream:
    def __init__(self):
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            flag = False
            for proc in self._processors:
                if proc.validate(item):
                    proc.ingest(item)
                    flag = True
                    break
            if not flag:
                print("DataStream Error")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            name = proc.__class__.__name__
            total = proc._next_rank
            remaining = len(proc._data)
            print(
                f"{name}: total {total} items processed, "
                f"remaining {remaining} on processor"
            )

def main() -> None:
    print("=== Code Nexus - Data Stream ===\n")

    print("Initialize Data Stream...")
    ds = DataStream()
    ds.print_processors_stats()

    print("Registering Numeric Processor")
    np = NumericProcessor()
    ds.register_processor(np)

    batch: list[Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead"
            },
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]
    print(f"Send first batch of data on stream: {batch}")
    ds.process_stream(batch)
    ds.print_processors_stats()

    print("Registering other data processors")
    tp = TextProcessor()
    lp = LogProcessor()
    ds.register_processor(tp)
    ds.register_processor(lp)

    print("Send the same batch again")
    ds.process_stream(batch)
    ds.print_processors_stats()

    print(
        "Consume some elements from the data processors:"
        " Numeric 3, Text 2, Log 1"
    )
    for _ in range(3):
        np.output()
    for _ in range(2):
        tp.output()
    lp.output()
    ds.print_processors_stats()
    return


if __name__ == "__main__":
    main()
