#!/usr/bin/env python3

import abc

class HealCapability(abc.ABC):
    @abc.abstractmethod
    def heal(self, target: str) -> str:
        ...


class TransformCapability(abc.ABC):
    def __init__(self) -> None:
        self._transformed: bool = False

    @abc.abstractmethod
    def transform(self) -> str:
        ...

    @abc.abstractmethod
    def revert(self) -> str:
        ...
