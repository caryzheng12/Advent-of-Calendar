file_path = "input.txt"

list1 = []
list2 = []
list3 = []
similarities = {}

product = 0
result = 0

with open(file_path, "r") as file:
  for line in file:
      numbers = line.split()
      list1.append(int(numbers[0]))
      list2.append(int(numbers[1]))

for num1 in list1:
  for num2 in list2:
    if num1 == num2:
      if num1 in similarities:
        similarities[num1] += 1
      
      else:
        similarities[num1] = 1

for key, value in similarities.items():
  product = key * value
  print(key, value, product)
  list3.append(product)

for num3 in list3:
  result += num3

print(result)