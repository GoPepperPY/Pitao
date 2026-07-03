#!/usr/bin/env python3

import abc

class CreatureFactory(abc.ABC):

    @abc.abstractmethod
    def create_base(self) -> None:
        ...

    @abc.abstractmethod
    def create_evolved(self) -> None:
        ...
