import sys


def process_scores(arguments):
    scores = []

    if len(arguments) < 2:
        print("No scores provided. Usage: python3 ft_score_analytics.py <\
score1> <score2> ...")
        sys.exit(1)

    try:
        for i in range(1, len(arguments)):
            scores.append(int(arguments[i]))
    except ValueError:
        print(f"oops, I typed {arguments[i]} instead of an integer")
        sys.exit(1)

    return scores


def analyze_scores(scores):
    if not scores:
        return

    print("Scores processed: [", end="")
    for i in range(len(scores)):
        value = scores[i]
        if i < len(scores) - 1:
            print(f"{value}, ", end="")
        else:
            print(f"{value}", end="")
    print("]")
    print(f"Total players: {i + 1}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores):.2f}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    scores = process_scores(sys.argv)
    analyze_scores(scores)
