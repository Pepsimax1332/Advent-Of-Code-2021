echo ""
echo "Time taken for results for day 1 task 1:"
python -m timeit -n 1_000 -r 5 -s 'import src.Day1 as day1' 'day1.task(day1.data)'
echo "Time taken for results for day 1 task 2:"
python -m timeit -n 1_000 -r 5 -s 'import src.Day1 as day1' 'day1.task(day1.data, 3)'
echo ""


echo "Time taken for results for day 2 task 1:"
python -m timeit -n 1_000 -r 5 -s 'import src.Day2 as day2' 'day2.task_one(day2.data)'
echo "Time taken for results for day 2 task 2:"
python -m timeit -n 1_000 -r 5 -s 'import src.Day2 as day2' 'day2.task_two(day2.data)'
echo ""

echo "Time taken for results for day 3 task 1:"
python -m timeit -n 1_000 -r 5 -s 'import src.Day3 as day3' 'day3.task_one(day3.data, 12)'
echo "Time taken for results for day 2 task 2:"
python -m timeit -n 1_000 -r 5 -s 'import src.Day3 as day3' 'day3.task_two(day3.data, 12)'