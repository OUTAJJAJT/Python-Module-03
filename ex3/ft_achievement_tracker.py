def achievement():
    Player1 = ["first_kill", "level_10", "treasure_hunter", "speed_demon"]
    Player2 = ["first_kill", "level_10", "boss_slayer", "collector"]
    Player3 = ["level_10", "treasure_hunter", "boss_slayer", "\
speed_demon", "perfectionist"]
    print(f"Player alice achievements: {set(Player1)}")
    print(f"Player bob achievements: {set(Player2)}")
    print(f"Player charlie achievements: {set(Player3)}")


if __name__ == "__main__":
    achievement()
