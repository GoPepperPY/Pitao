#!/usr/bin/env python3

def main() -> None:
    try:
        import alchemy.grimoire.dark_spellbook
        print(alchemy.grimoire.dark_spellbook.dark_spell_record("Fantasy", "bats"))
    except ImportError:
        print("Your alchemist laboratory has just exploded!")


if __name__ == "__main__":
    main()