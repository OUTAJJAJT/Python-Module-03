#!/usr/bin/env python3

def achievement():
    Player_alice = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
    Player_bob = {"first_kill", "level_10", "boss_slayer", "collector"}
    Player_charlie = {"level_10", "treasure_hunter", "boss_slayer", "\
speed_demon", "perfectionist"}

    print("=== Achievement Tracker System ===")
    print(f"Player alice achievements: {Player_alice}")
    print(f"Player bob achievements: {Player_bob}")
    print(f"Player charlie achievements: {Player_charlie}")

    print("\n=== Achievement Analytics ===")

    print("All unique achievements: ",
          (Player_alice.union(Player_bob, Player_charlie)))
    print("Total unique achievements: ",
          len(Player_alice.union(Player_bob, Player_charlie)))

    print("\nCommon to all players: ",
          Player_alice.intersection(Player_bob, Player_charlie))

    alice_rare = Player_alice.difference(Player_bob, Player_charlie)
    bob_rare = Player_bob.difference(Player_alice, Player_charlie)
    charlie_rare = Player_charlie.difference(Player_alice, Player_bob)

    print("Rare achievements (1 player): ",
          alice_rare.union(bob_rare, charlie_rare))

    print("\nAlice vs Bob common:", Player_alice.intersection(Player_bob))
    print("Alice unique:", Player_alice.difference(Player_bob))
    print("Bob unique:", Player_bob.difference(Player_alice))


if __name__ == "__main__":
    achievement()
