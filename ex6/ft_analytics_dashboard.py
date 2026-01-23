#!/usr/bin/env python3
# players = [
#     {
#         "name": "alice",
#         "score": 2300,
#         "achievements": ["first_kill", "level_10", "boss_slayer", "speed_demon\
# ", "collector"],
#         "active": True,
#         "region": "north"
#     },
#     {
#         "name": "bob",
#         "score": 1800,
#         "achievements": ["first_kill", "level_10", "collector"],
#         "active": True,
#         "region": "east"
#     },
#     {
#         "name": "charlie",
#         "score": 2150,
#         "achievements": ["first_kill", "level_10", "boss_slayer", "speed_demon\
# ", "perfectionist", "collector", "explorer"],
#         "active": True,
#         "region": "central"
#     },
#     {
#         "name": "diana",
#         "score": 2050,
#         "achievements": ["level_10"],
#         "active": False,
#         "region": "north"
#     }
# ]

players = {
    "alice": {
         "level": 41,
         "total_score": 2824,
         "sessions_played": 13,
         "favorite_mode": "ranked",
         "achievements_count": 5
      },
    "bob": {
         "level": 16,
         "total_score": 4657,
         "sessions_played": 27,
         "favorite_mode": "ranked",
         "achievements_count": 2
      },
    "charlie": {
         "level": 44,
         "total_score": 9935,
         "sessions_played": 21,
         "favorite_mode": "ranked",
         "achievements_count": 7
      }
}

def list_comp():
    high_scorers = [p["name"] for p in players if p["score"] > 2000]

    scores_doubled = [p["score"] * 2 for p in players]

    active_players = [p["name"] for p in players if p["active"]]
    print("\n=== List Comprehension Examples ===")
    print("High scorers (>2000):", high_scorers)
    print("Scores doubled:", scores_doubled)
    print("Active players:", active_players)


def dict_comp():
    player_scores = {p["name"]: p["score"] for p in players}

    achievement_counts = {p["name"]: len(p["achievements"]) for p in players}

    score_categories = {
        "high": len([p for p in players if p["score"] >= 2200]),
        "medium": len([p for p in players if 1800 <= p["score"] < 2200]),
        "low": len([p for p in players if p["score"] < 1800])
    }
    print("\n=== Dict Comprehension Examples ===")
    print("Player scores:", player_scores)
    print("Score categories:", score_categories)
    print("Achievement counts:", achievement_counts)


def set_comp():
    unique_players = {p["name"] for p in players}

    unique_achievements = {a for p in players for a in p["achievements"]}

    active_regions = {p["region"] for p in players if p["active"]}
    print("\n=== Set Comprehension Examples ===")
    print("Unique players:", unique_players)
    print("Unique achievements:", unique_achievements)
    print("Active regions:", active_regions)
    return unique_players, unique_achievements


def analysis(unique_players, unique_achievements):
    total_players = len(unique_players)
    total_unique_achievements = len(unique_achievements)

    scores = [p["score"] for p in players]
    average_score = sum(scores) / len(scores)

    top_player = max(players, key=lambda p: p["score"])
    print("\n=== Combined Analysis ===")
    print("Total players:", total_players)
    print("Total unique achievements:", total_unique_achievements)
    print("Average score:", average_score)
    print(
        "Top performer:",
        top_player["name"],
        "(",
        top_player["score"],
        "points,",
        len(top_player["achievements"]),
        "achievements )"
    )


print("=== Game Analytics Dashboard ===")
list_comp()
dict_comp()
unique_players, unique_achievements = set_comp()
analysis(unique_players, unique_achievements)
