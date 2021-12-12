from pathlib import Path

FILEPATH = f"{Path()}/data/day6.txt"

test = """3,4,3,1,2"""

test_data = list(map(int, test.strip().split(",")))
with open(FILEPATH, "r") as f:
    data = list(map(int, f.read().strip().split(",")))


def task_one(data, days=80):

    for _ in range(1, days+1):

        data.extend([9] * data.count(0))
        data = list(map(lambda x: 6 if x == 0 else x-1, data))

    return len(data)


def task_two(numbers, days=80):

    data = [numbers.count(i) for i in range(9)]

    for day in range(days):
        data[(day + 7) % 9] += data[day % 9]

    return sum(data)
    




if __name__ == "__main__":
    print(f"Solution to day 6 test task 1: {task_one(test_data, 80)}")
    print(f"Solution to day 6 real task 1: {task_one(data, 80)}")

    print(f"Solution to day 6 test task 2: {task_two(test_data, 256)}")
    print(f"Solution to day 6 test task 2: {task_two(data, 256)}")
    
