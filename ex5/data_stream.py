#!/usr/bin/env python3

print("=== Game Data Stream Processor ===")
print("Processing 1000 game events...")

players = [
    {'id': 1, 'player': 'frank', 'event_type': 'login',
     'timestamp': '2024-01-01T23:17',
     'data': {'level': 16, 'score_delta': 128, 'zone': 'pixel_zone_2'}},

    {'id': 2, 'player': 'frank', 'event_type': 'login',
     'timestamp': '2024-01-22T23:57',
     'data': {'level': 35, 'score_delta': -11, 'zone': 'pixel_zone_5'}},

    {'id': 3, 'player': 'diana', 'event_type': 'login',
     'timestamp': '2024-01-01T02:13',
     'data': {'level': 15, 'score_delta': 417, 'zone': 'pixel_zone_5'}},

    {'id': 4, 'player': 'alice', 'event_type': 'level_up',
     'timestamp': '2024-01-07T22:41',
     'data': {'level': 45, 'score_delta': 458, 'zone': 'pixel_zone_4'}},
]


def action(event_id):
    if event_id % 3 == 0:
        return "killed monster"
    if event_id % 3 == 1:
        return "found treasure"
    return "leveled up"


def game_event_stream(total_events):
    for i in range(1, total_events + 1):
        yield i


total_events = 1000
high_level_players = 0
treasure_events = 0
level_up_events = 0

stream = game_event_stream(total_events)

for event_id in stream:
    player = players[(event_id - 1) % len(players)]
    level = event_id % 15 + 1
    event_action = action(event_id)

    if event_id <= 3:
        print(
            f"Event {event_id}: Player {player['player']} "
            f"(level {level}) {event_action}"
        )

    if level >= 10:
        high_level_players += 1
    if event_action == "found treasure":
        treasure_events += 1
    if event_action == "leveled up":
        level_up_events += 1


print("=== Stream Analytics ===")
print("Total events processed:", total_events)
print("High-level players (10+):", high_level_players)
print("Treasure events:", treasure_events)
print("Level-up events:", level_up_events)
print("Memory usage: Constant (streaming)")
print("Processing time: Fast (no storage)")


print("=== Generator Demonstration ===")


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci()
print("Fibonacci sequence (first 10):", end=" ")
for i in range(10):
    print(next(fib), end=", " if i < 9 else "\n")


def primes():
    n = 2
    while True:
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            yield n
        n += 1


prime_stream = primes()
print("Prime numbers (first 5):", end=" ")
for i in range(5):
    print(next(prime_stream), end=", " if i < 4 else "\n")
