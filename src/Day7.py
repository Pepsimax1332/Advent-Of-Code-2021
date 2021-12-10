from pathlib import Path

FILEPATH = f"{Path()}/data/day7.txt"

test = """16,1,2,0,4,2,7,1,2,14"""

test_data = list(map(int, test.split(",")))

with open(FILEPATH, "r") as f:
    data = list(map(int, f.read().split(",")))

def task_one(data):

    distance = lambda x, p: abs(x-p)
    range_ = max(data)

    min_fuel = 2 ** 63

    for i in range(range_):
        fuel = sum(map(lambda x: distance(x, i), data))
        if fuel < min_fuel:
            min_fuel = fuel

    return min_fuel


def task_two(data):

    distance = lambda x, p: abs(x-p)*(abs(x-p) + 1)//2
    range_ = max(data)

    min_fuel = 2 ** 63

    for i in range(range_):
        fuel = sum(map(lambda x: distance(x, i), data))
        if fuel < min_fuel:
            min_fuel = fuel

    return min_fuel


if __name__ == "__main__":
    print(f"Solution to day 7 test task 1: {task_one(test_data)}")
    print(f"Solution to day 7 real task 1: {task_one(data)}")

    print(f"Solution to day 7 test task 1: {task_two(test_data)}")
    print(f"Solution to day 7 real task 1: {task_two(data)}")
