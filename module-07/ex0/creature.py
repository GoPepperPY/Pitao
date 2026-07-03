#!/usr/bin/env python3

import abc

class Creature(abc.ABC):
    def __init__(self, name: str, creature_type: str) -> None:
        super().__init__()
        self._name: str = name
        self._creature_type: str = creature_type

    @abc.abstractmethod
    def attack(self) -> str:
        ...

    def describe(self) -> str:
        return f"{self._name} is a {self._creature_type} type Creature"
