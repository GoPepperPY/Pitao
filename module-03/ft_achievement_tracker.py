#!/usr/bin/env python3

import random

def gen_player_achievements() -> set[str]:
    pool = [
        'Crafting Genius', 'World Savior', 'Master Explorer',
        'Collector Supreme', 'Untouchable', 'Boss Slayer', 'Strategist',
        'Speed Runner', 'Survivor',
        'Treasure Hunter', 'First Steps', 'Sharp Mind',
        'Hidden Path Finder', 'Unstoppable'
    ]
    num_achievements = random.randint(5, 9)
    return set(random.sample(pool, num_achievements))

def main() -> None:

	Alice: str = gen_player_achievements()
	Bob: str = gen_player_achievements()
	Charlie: str = gen_player_achievements()
	Dylan: str = gen_player_achievements()

	print(f"Player Alice: {Alice}")
	print(f"Player Bob: {Bob}")
	print(f"Player Charlie: {Charlie}")
	print(f"Player Dylan: {Dylan}\n\n")

	print(f"All distinct achievements: {Alice.union(Bob).union(Charlie).union(Dylan)}")

	print(f"Common achievement: {Alice.intersection(Bob).intersection(Charlie).intersection(Dylan)}")

	print(f"Only Alice has: {Alice.difference(Bob.union(Charlie).union(Dylan))}")
	print(f"Only Bob has: {Bob.difference(Alice.union(Charlie).union(Dylan))}")
	print(f"Only Charlie has: {Charlie.difference(Bob.union(Alice).union(Dylan))}")
	print(f"Only Dylan has: {Dylan.difference(Bob.union(Charlie).union(Alice))}")

	all = Alice.union(Bob).union(Charlie).union(Dylan)

	print(f"\n\nAlice missing: {all.difference(Alice)}")
	print(f"Bob missing: {all.difference(Bob)}")
	print(f"Charlie missing: {all.difference(Charlie)}")
	print(f"Dylan missing: {all.difference(Dylan)}")
if __name__ == "__main__":
	main()