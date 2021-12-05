from pathlib import Path

FILEPATH = f"{Path()}/data/day2.txt"

test = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

test_data = test.splitlines()
with open(FILEPATH, "r") as f:
    data = list(f.readlines()).copy()

def task_one(data):
    dic = {}
    for d, v in map(lambda d : d.strip().split(" "), data):
        dic[d] = dic.get(d, 0) +  int(v)

    return dic.get("forward") * (dic.get("down") - dic.get("up"))

def task_two(data):
    list = [0, 0, 0]
    for d, v in map(lambda d : d.strip().split(" "), data):
        if d == "forward":
            list[0] += int(v)
            list[1] += list[2] * int(v)
        elif d == "down":
            list[2] += int(v)
        elif d == "up":
            list[2] -= int(v)

    return list[0] * list[1]


if __name__ == "__main__":
    print(f"Solution to day 2 test task 1: {task_one(test_data)}")
    print(f"Solution to day 2 real task 1: {task_one(data)}")

    print(f"Solution to day 2 test task 2: {task_two(test_data)}")
    print(f"Solution to day 2 real task 2: {task_two(data)}")