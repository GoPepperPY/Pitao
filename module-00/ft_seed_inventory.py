def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    word = seed_type.capitalize()

    if unit == "packets":
        print(word, "seeds:", quantity, "packets available")
    elif unit == "grams":
        print(word, "seeds:", quantity, "grams total")
    elif unit == "area":
        print(word, "seeds:", "covers", quantity, "square meters")
    else:
        print("Unknown")