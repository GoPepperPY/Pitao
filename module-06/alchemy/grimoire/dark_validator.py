#!/usr/bin/env python3

def validate_ingredients(ingredients: str) -> str:
    from .dark_spellbook import dark_spell_allowed_ingredients
    allowed = dark_spell_allowed_ingredients()
    is_valid = any(word in ingredients.lower() for word in allowed)
    result = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {result}"