from pathlib import Path

FILEPATH = f"{Path()}/data/day7.txt"

test = """16,1,2,0,4,2,7,1,2,14"""

test_data = list(map(int, test.split(",")))

with open(FILEPATH, "r") as f:
    data = list(map(int, f.read().split(",")))
    

def task_one(data):

    fuel_burn = lambda x, p: abs(x-p)

    return min([sum(fuel_burn(x, i) for x in data) for i in range(max(data))])


def task_two(data):

    fuel_burn = lambda x, p: abs(x-p)*(abs(x-p) + 1)//2

    return min([sum(fuel_burn(x, i) for x in data) for i in range(max(data))])


if __name__ == "__main__":
    print(f"Solution to day 7 test task 1: {task_one(test_data)}")
    print(f"Solution to day 7 real task 1: {task_one(data)}")

    print(f"Solution to day 7 test task 1: {task_two(test_data)}")
    print(f"Solution to day 7 real task 1: {task_two(data)}")
