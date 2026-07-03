#!/usr/bin/env python3

def dark_spell_allowed_ingredients() -> list:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    from .dark_validator import validate_ingredients
    if "VALID" in validate_ingredients(ingredients):
        return f"spell recorded: {spell_name} {validate_ingredients(ingredients)}"
    return f"spell rejected: {spell_name} {validate_ingredients(ingredients)}"
