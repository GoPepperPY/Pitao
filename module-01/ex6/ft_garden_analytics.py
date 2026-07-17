#!/usr/bin/env python3

class Plant:
    class Stats:
        def __init__(self) -> None:
            self.__age_counter = 0
            self.__show_counter = 0
            self.__grow_counter = 0

        def age(self) -> None:
            self.__age_counter += 1

        def grow(self) -> None:
            self.__grow_counter += 1

        def show(self) -> None:
            self.__show_counter += 1

        def show_stats(self) -> None:
            print(f"Stats: {self.__grow_counter} grow, "
                  f"{self.__age_counter} age, "
                  f"{self.__show_counter} show")

    def __init__(self, name: str, cm: float, age_plant: int) -> None:
        self.name: str = name
        self.cm: float = cm
        self.age_plant: int = age_plant
        self._stats: Plant.Stats = self.Stats()

    def age(self) -> None:
        self._stats.age()
        self.age_plant += 1

    def grow(self) -> None:
        self._stats.grow()
        self.cm += 2

    def show(self) -> None:
        self._stats.show()
        print(f"{self.name} plant: {self.cm}, {self.age_plant} days old")

    def display_stats(self) -> None:
        self._stats.show_stats()

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown Plant", 0.0, 0)


def show_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.display_stats()


class Flower(Plant):
    def __init__(self, name: str, height: float, age_flower:
                 int, color: str) -> None:
        super().__init__(name, height, age_flower)
        self.color: str = color
        self.__bloom_value = False

    def bloom(self) -> None:
        self.__bloom_value = True

    def show_flower(self) -> None:
        self.show()
        print(f"Color: {self.color}")
        if self.__bloom_value is True:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    class Treestats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self.__shadow_counter = 0

        def produce_shade(self) -> None:
            self.__shadow_counter += 1

        def show_stats(self) -> None:
            super().show_stats()
            print(f" {self.__shadow_counter} shadow")

    def __init__(self, name: str, height: float, age_tree:
                 int, trunk_diameter: float) -> None:
        super().__init__(name, height, age_tree)
        self.trunk_diameter = trunk_diameter
        self._stats: Tree.Treestats = self.Treestats()

    def produce_shade(self) -> None:
        self._stats.produce_shade()
        print(f"Tree {self.name} now produces a shade of "
              f"{round(self.cm, 1)}cm long and "
              f"{round(self.trunk_diameter, 1)}cm wide.")

    def show_tree(self) -> None:
        self.show()
        print(f"Trunk Diameter: {self.trunk_diameter}cm")


class Seed(Flower):
    def __init__(self, name: str, height: float, age_flower:
                 int, color: str, seeds: float) -> None:
        super().__init__(name, height, age_flower, color)
        self.seeds = seeds

    def show_seed(self) -> None:
        self.show_flower()
        print(f"Seeds: {round(self.seeds)}")

    def grow_seed(self) -> None:
        self.seeds += 2.1


def main() -> None:
    """<------ Flowers ------>"""
    flower_data: list[Flower] = [
        Flower("Rose", 15.0, 10, "Red")
    ]
    """<------ Trees ------>"""
    tree_data: list[Tree] = [
        Tree("Oak", 200.0, 365, 5.0)
    ]
    """<------ Trees ------>"""
    seed_data: list[Seed] = [
        Seed("Sunflower", 80.0, 45, "Yellow", 0)
    ]
    print(f"\nIs Oak older than a year? {Plant.is_older_than_year(45)}")
    print(f"\nIs Oak older than a year? {Plant.is_older_than_year(400)}\n")
    """<------ Flowers ------>"""
    print("=== FLOWER ===")
    for flower in flower_data:
        flower.show_flower()
        show_statistics(flower)
        print("[asking the rose to grow and bloom]")
        for _ in range(1, 7):
            flower.grow()
        flower.bloom()
        flower.show_flower()
        show_statistics(flower)
    print("\n")
    """<------ Trees ------>"""
    print("=== TREES ===")
    for tree in tree_data:
        tree.show()
        show_statistics(tree)
        print("[asking the oak to produce shade]")
        tree.produce_shade()
        show_statistics(tree)
    print("\n")
    """<------ SEED ------>"""
    print("=== SEED ===")
    for plant in seed_data:
        plant.show_seed()
        print("[make sunflower grow, age and bloom]")
    plant.bloom()
    for _ in range(1, 21):
        plant.grow_seed()
        plant.grow()
        plant.age()
    plant.show_seed()
    show_statistics(plant)
    print("\n")
    # Classmethod demo
    unknown = Plant.anonymous()
    unknown.show()
    show_statistics(unknown)


if __name__ == "__main__":
    main()
