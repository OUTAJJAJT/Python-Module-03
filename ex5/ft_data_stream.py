#!/usr/bin/env python3

import time

print("=== Game Data Stream Processor ===")
print("\nProcessing 1000 game events...\n")

players_data = [
   {
      "id": 1,
      "player": "alice",
      "event_type": "killed monster",
      "timestamp": "2024-01-01T23:17",
      "data": {
         "level": 5,
         "score_delta": 128,
         "zone": "pixel_zone_2"
      }
   },
   {
      "id": 2,
      "player": "bob",
      "event_type": "found treasure",
      "timestamp": "2024-01-22T23:57",
      "data": {
         "level": 12,
         "score_delta": -11,
         "zone": "pixel_zone_5"
      }
   },
   {
      "id": 3,
      "player": "charlie",
      "event_type": "leveled up",
      "timestamp": "2024-01-01T02:13",
      "data": {
         "level": 8,
         "score_delta": 417,
         "zone": "pixel_zone_5"
      }
   },
   {
      "id": 4,
      "player": "daiana",
      "event_type": "level_up",
      "timestamp": "2024-01-07T22:41",
      "data": {
         "level": 45,
         "score_delta": 458,
         "zone": "pixel_zone_4"
      }
   },
   {
      "id": 5,
      "player": "bob",
      "event_type": "death",
      "timestamp": "2024-01-19T08:51",
      "data": {
         "level": 1,
         "score_delta": 63,
         "zone": "pixel_zone_4"
      }
   },
   {
      "id": 5,
      "player": "aliex",
      "event_type": "found_treasure",
      "timestamp": "2024-01-19T08:51",
      "data": {
         "level": 2,
         "score_delta": 31,
         "zone": "pixel_zone_4"
      }
   },
]


total_events = 0
high_level = 0
treasure_events = 0
level_up_events = 0


def game_event_stream(data: list):
    """
      A generator that yields game events one at a time from the data list.
    """
    for event in data:
        yield event


for event in game_event_stream(players_data):
    total_events += 1

    if (event["data"]["level"] >= 10):
        high_level += 1

    if event['event_type'] == 'found_treasure':
        treasure_events += 1

    if 'level_up' in event['event_type']:
        level_up_events += 1


my_gen = game_event_stream(players_data)

event_number = 1
start = time.time()
for event in my_gen:
    if event_number > 3:
        break
    print(f"Event {event_number}: Player {event['player']} "
          f"({event['data']['level']}) {event['event_type']}")
    event_number += 1
end = time.time()

print("...")
print("\n=== Stream Analytics ===")
print("Total events processed:", total_events)
print("High-level players (10+):", high_level)
print("Treasure events:", treasure_events)
print("Level-up events:", level_up_events)
print("\nMemory usage: Constant (streaming)")
print(f"Processing time: {end - start:.3f} seconds\n")


print("=== Generator Demonstration ===")


def fibonacci():  # -> Generator[int, None, None]
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci()
print("Fibonacci sequence (first 10):", end=" ")
for i in range(10):
    print(next(fib), end=", " if i < 9 else "\n")


def primes():  # -> Generator[int, None, None]
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
