def achievement():
    Player1 = set(("first_kill", "level_10", "treasure_hunter", "speed_demon"))
    Player2 = set(("first_kill", "level_10", "boss_slayer", "collector"))
    Player3 = set(("level_10", "treasure_hunter", "boss_slayer", "\
speed_demon", "perfectionist"))
    print(f"Player alice achievements: {Player1}")
    print(f"Player bob achievements: {Player2}")
    print(f"Player charlie achievements: {Player3}")


if __name__ == "__main__":
    achievement()
