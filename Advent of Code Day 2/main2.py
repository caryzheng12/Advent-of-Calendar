file_path = "input.txt"

puzzle_input = []
success = 0
failed = 0

with open(file_path, "r") as file:
  for i, line in enumerate(file, start = 1):
    numbers = list(map(int, line.split()))
    puzzle_input.append(numbers)

for report in puzzle_input:
  failed = 0
  increase = 0
  decrease = 0
  result = None

  for iterations in report:
    if result is not None:
      if (result < iterations) and increase == 0:
        decrease = 1
        if (result + 3) >= iterations:
          result = iterations

      elif (result > iterations) and decrease == 0:
        increase = 1
        if (result -3) <= iterations:
          result = iterations

      elif result == iterations and failed < 1:
        result = iterations
        failed += 1

      else:
        failed = 2
        break

    else:
      result = iterations

  if failed <= 1:
    success += 1

print(success)



