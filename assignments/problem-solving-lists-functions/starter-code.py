def count_even(numbers):
    # Return how many values in the list are even.
    raise NotImplementedError("Implement count_even")


def filter_above(numbers, threshold):
    # Return a new list containing values above the threshold.
    raise NotImplementedError("Implement filter_above")


def find_max(numbers):
    # Return the largest value in the list.
    raise NotImplementedError("Implement find_max")


def average_score(numbers):
    # Stretch helper example: return the average score.
    raise NotImplementedError("Implement average_score")


def main():
    scores = [58, 72, 91, 84, 67, 75, 88, 93, 60, 79]
    target = 80

    even_count = count_even(scores)
    above_target = filter_above(scores, target)
    highest = find_max(scores)
    avg = average_score(scores)

    print("Score Analysis")
    print("--------------")
    print(f"Even score count: {even_count}")
    print(f"Scores above {target}: {above_target}")
    print(f"Highest score: {highest}")
    print(f"Average score: {avg:.2f}")


if __name__ == "__main__":
    main()
