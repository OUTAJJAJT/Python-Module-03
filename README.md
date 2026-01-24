# Python Module 03

A collection of Python exercises focusing on data structures, command-line arguments, and data processing techniques.

## Project Structure

```
Python-Module-03/
├── ex0/ - Command Quest
├── ex1/ - Score Analytics
├── ex2/ - Coordinate System
├── ex3/ - Achievement Tracker
├── ex4/ - Inventory System
├── ex5/ - Data Stream
└── ex6/ - Analytics Dashboard
```

## Exercises

### ex0: Command Quest (`ft_command_quest.py`)
**Topics:** Command-line arguments, `sys.argv`

A program that demonstrates how to handle command-line arguments in Python. It displays the program name, counts arguments, and prints each argument received.

**Usage:**
```bash
python3 ft_command_quest.py arg1 arg2 arg3
```

**Features:**
- Display program name
- Count and list all arguments
- Handle zero arguments gracefully

---

### ex1: Score Analytics (`ft_score_analytics.py`)
**Topics:** Lists, error handling, statistics

Processes player scores and provides analytical insights including total score, average, high/low scores, and score range.

**Usage:**
```bash
python3 ft_score_analytics.py 85 92 78 95 88
```

**Features:**
- Input validation for integer scores
- Statistical calculations (sum, average, min, max, range)
- Error handling for invalid inputs

---

### ex2: Coordinate System (`ft_coordinate_system.py`)
**Topics:** Tuples, unpacking, 3D mathematics

Implements a 3D coordinate system for game positioning with distance calculations between points.

**Usage:**
```bash
python3 ft_coordinate_system.py "10,20,5"
```

**Features:**
- 3D distance calculation using Euclidean formula
- Coordinate parsing from strings
- Tuple unpacking demonstrations
- Error handling for invalid coordinates

---

### ex3: Achievement Tracker (`ft_achievement_tracker.py`)
**Topics:** Sets, set operations

A system to track and analyze player achievements using Python sets.

**Usage:**
```bash
python3 ft_achievement_tracker.py
```

**Features:**
- Union operations (all unique achievements)
- Intersection operations (common achievements)
- Difference operations (rare/unique achievements)
- Multi-player achievement comparison

---

### ex4: Inventory System (`ft_inventory_system.py`)
**Topics:** Dictionaries, nested data structures

Manages a game inventory system with player items and values.

**Usage:**
```bash
python3 ft_inventory_system.py
```

**Features:**
- Nested dictionary management
- Inventory analytics
- Item counting and value tracking
- Percentage calculations

---

### ex5: Data Stream (`ft_data_stream.py`)
**Topics:** List comprehensions, data filtering, performance

Processes game event data streams with various filtering and transformation operations.

**Usage:**
```bash
python3 ft_data_stream.py
```

**Features:**
- Event filtering by type, player, and zone
- Score calculations and aggregations
- Performance comparisons (comprehensions vs loops)
- Data transformation pipelines

---

### ex6: Analytics Dashboard (`ft_analytics_dashboard.py`)
**Topics:** List comprehensions, dictionary comprehensions, lambdas

Creates analytical views of player data using Python comprehensions.

**Usage:**
```bash
python3 ft_analytics_dashboard.py
```

**Features:**
- List comprehensions for data filtering
- Dictionary comprehensions for mappings
- Lambda functions for sorting
- Multiple analytical views (scores, achievements, regions)

---

## Requirements

- Python 3.10 or higher (uses modern type hints)
- No external dependencies required (uses only standard library)

## Learning Objectives

This module covers:
- **Data Structures:** Lists, tuples, sets, and dictionaries
- **Command-line Processing:** Using `sys.argv`
- **Error Handling:** Try-except blocks and validation
- **Comprehensions:** List and dictionary comprehensions
- **Set Operations:** Union, intersection, difference
- **Type Hints:** Modern Python typing
- **Mathematical Operations:** Distance calculations, statistics

## Running the Exercises

Each exercise is self-contained and can be run independently:

```bash
# Make scripts executable (optional)
chmod +x ex*/ft_*.py

# Run any exercise
python3 ex0/ft_command_quest.py [arguments]
python3 ex1/ft_score_analytics.py 85 92 78
python3 ex2/ft_coordinate_system.py "10,20,5"
python3 ex3/ft_achievement_tracker.py
python3 ex4/ft_inventory_system.py
python3 ex5/ft_data_stream.py
python3 ex6/ft_analytics_dashboard.py
```

Or use the shebang if executable:

```bash
./ex0/ft_command_quest.py [arguments]
```

## Author

OUTAJJAJT

## License

This project is part of a Python learning curriculum.
