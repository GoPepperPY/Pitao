#!/usr/bin/env python3

from ex0 import Creature
from ex1.capabilities import HealCapability, TransformCapability

class Sproutling(Creature, HealCapability):
    def __init__(self):
        Creature.__init__(self, "Sproutling", "Grass")

    def attack(self) -> str:
        return f"{self._creature_type} uses Vine Whip!"

    def heal(self, target: str) -> str:
        return f"{self._creature_type} heals itself for a {target} amount"

class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return f"{self._creature_type} uses Petal Dance!"

    def heal(self, target: str) -> str:
        return f"{self._creature_type} heals itself and others for a {target} amount"

class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Normal")
        self._transformed = False

    def attack(self) -> str:
        if (self._transformed is True):
            return f"{self._creature_type} performs a boosted strike!"
        return f"{self._creature_type} attacks normally."

    def transform(self):
        self._transformed = True
        return f"{self._creature_type} shifts into a sharper form!"

    def revert(self):
        self._transformed = False
        return f"{self._creature_type} returns to normal"

class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        self._transformed = False

    def attack(self) -> str:
        if (self._transformed is True):
            return f"{self._creature_type} unleashes a devastating morph strike!"
        return f"{self._creature_type} attacks normally."

    def transform(self):
        self._transformed = True
        return f"{self._creature_type} morphs into a dragonic battle form!"

    def revert(self):
        self._transformed = False
        return f"{self._creature_type} stabilizes its form."
