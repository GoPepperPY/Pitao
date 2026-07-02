#!/usr/bin/env python3

from typing import Any, Protocol
import abc


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class DataProcessError(Exception):
    def __init__(self, message: str = "Unknown DataProcessor Error") -> None:
        super().__init__(message)


class NumericProcessError(DataProcessError):
    def __init__(self, message: str =
                 "Unknown NumericProcessor Error") -> None:
        super().__init__(message)


class TextProcessError(DataProcessError):
    def __init__(self, message: str = "Unknown TextProcessor Error") -> None:
        super().__init__(message)


class LogProcessError(DataProcessError):
    def __init__(self, message: str = "Unknown LogProcessor Error") -> None:
        super().__init__(message)


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
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
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(isinstance(item, (int, float)) for item in data)
        return isinstance(data, (int, float))

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise NumericProcessError()
        items = data if isinstance(data, list) else [data]
        for pos in items:
            self._data.append((self._next_rank, str(pos)))
            self._next_rank += 1


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return isinstance(data, str)

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise TextProcessError()
        items = data if isinstance(data, list) else [data]
        for pos in items:
            self._data.append((self._next_rank, pos))
            self._next_rank += 1


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        def is_log_entry(entry: Any) -> bool:
            return (
                isinstance(entry, dict)
                and all(
                    isinstance(key, str) and isinstance(val, str)
                    for key, val in entry.items()
                )
            )

        if isinstance(data, list):
            return all(is_log_entry(item) for item in data)
        return is_log_entry(data)

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise LogProcessError()
        items = data if isinstance(data, list) else [data]
        for item in items:
            try:
                entry = f"{item['log_level']}: {item['log_message']}"
            except KeyError as exc:
                raise LogProcessError() from exc
            self._data.append((self._next_rank, entry))
            self._next_rank += 1


class CSVExportPlugin:
    """Exports a batch of processed items as one CSV line."""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        print(",".join(value for _, value in data))


class JSONExportPlugin:
    """Exports a batch of processed items as a JSON object,
    keyed on each item's processing rank.
    """

    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        pairs = ", ".join(
            f'"item_{rank}": "{value}"' for rank, value in data
        )
        print("{" + pairs + "}")


class DataStream:
    def __init__(self) -> None:
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
                print(f"DataStream error - Can't process element in "
                      f"stream: {item}")

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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors:
            batch: list[tuple[int, str]] = []
            for _ in range(nb):
                try:
                    batch.append(proc.output())
                except IndexError:
                    break
            if batch:
                plugin.process_output(batch)


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===\n")

    print("Initialize Data Stream...")
    ds = DataStream()
    ds.print_processors_stats()

    print("\nRegistering Processors")
    np = NumericProcessor()
    tp = TextProcessor()
    lp = LogProcessor()
    ds.register_processor(np)
    ds.register_processor(tp)
    ds.register_processor(lp)

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

    print(f"\nSend first batch of data on stream: {batch}")
    ds.process_stream(batch)
    ds.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVExportPlugin()
    ds.output_pipeline(3, csv_plugin)
    ds.print_processors_stats()

    batch2: list[Any] = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days"
            },
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]

    print(f"\nSend another batch of data: {batch2}")
    ds.process_stream(batch2)
    ds.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONExportPlugin()
    ds.output_pipeline(5, json_plugin)
    ds.print_processors_stats()


if __name__ == "__main__":
    main()