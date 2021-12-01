echo "Time taken for results for day1 task 1:"
python -m timeit -n 1_000 -s 'import src.Day1 as day1' 'day1.task(day1.data)'

echo "\nTime taken for results for day1 task 2:"
python -m timeit -n 1_000 -s 'import src.Day1 as day1' 'day1.task(day1.data, 3)'