#!/usr/bin/env python3

from .creature import Creature
from .creatures import Aquabub, Flameling, Torragon, Pyrodon
from .factory import CreatureFactory

class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()

class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return  Aquabub()
    
    def create_evolved(self) -> Creature:
        return Torragon()
