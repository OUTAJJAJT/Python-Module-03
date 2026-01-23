#!/usr/bin/env python3

import math
import sys
from typing import Tuple, Optional


def distance_3d(p1: Tuple[int, int, int], p2: Tuple[int, int, int]) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt(
        (x2 - x1) ** 2 +
        (y2 - y1) ** 2 +
        (z2 - z1) ** 2
    )


def parse_coordinates(coord_str: str) -> Optional[Tuple[int, int, int]]:
    try:
        x, y, z = coord_str.split(",")
        position = (int(x), int(y), int(z))
        print(f'Parsing coordinates: "{coord_str}"')
        print(f"Parsed position: {position}")
        return position
    except ValueError as e:
        print(f'Parsing invalid coordinates: "{coord_str}"')
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}\n")
        return None


def unpacking_demo(position: Tuple[int, int, int]) -> None:
    print("Unpacking demonstration:")
    x, y, z = position
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


def position() -> None:
    print("=== Game Coordinate System ===\n")

    origin: Tuple[int, int, int] = (0, 0, 0)
    spawn_point: Tuple[int, int, int] = (10, 20, 5)

    print(f"Position created: {spawn_point}")
    dist = distance_3d(origin, spawn_point)
    print(f"Distance between {origin} and {spawn_point}: {dist:.2f}\n")

    if len(sys.argv) > 1:
        user_coords = sys.argv[1]
        print(f"User provided coordinates: {user_coords}")
        parsed = parse_coordinates(user_coords)

        if parsed:
            dist = distance_3d(origin, parsed)
            print(f"Distance between {origin} and {parsed}: {dist:.2}\n")

        if parsed:
            unpacking_demo(parsed)


if __name__ == "__main__":
    position()
