file_path = "input.txt"

list1 = []
list2 = []
list3 = []

distance = 0
total = 0

with open(file_path, "r") as file:
  for line in file:
      numbers = line.split()
      list1.append(int(numbers[0]))
      list2.append(int(numbers[1]))

sorted_list1 = sorted(list1)
sorted_list2 = sorted(list2)

for num1, num2 in zip(sorted_list1, sorted_list2):
  distance = abs(num1 - num2)
  list3.append(distance)

for num3 in list3:
  total += num3

print(total)