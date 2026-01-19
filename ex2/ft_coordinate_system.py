#!/usr/bin/env python3

import math


def distance_3d(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt(
        (x2 - x1) ** 2 +
        (y2 - y1) ** 2 +
        (z2 - z1) ** 2
    )


def parse_coordinates(coord_str):
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


def unpacking_demo(position):
    print("Unpacking demonstration:")
    x, y, z = position
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


def position():
    print("=== Game Coordinate System ===\n")

    origin = (0, 0, 0)
    spawn_point = (10, 20, 5)

    print(f"Position created: {spawn_point}")
    dist = distance_3d(origin, spawn_point)
    print(f"Distance between {origin} and {spawn_point}: {dist:.2f}\n")

    parsed = parse_coordinates("3,4,0")
    if parsed:
        dist = distance_3d(origin, parsed)
        print(f"Distance between {origin} and {parsed}: {dist}\n")

    parse_coordinates("abc,def,ghi")

    if parsed:
        unpacking_demo(parsed)


if __name__ == "__main__":
    position()
