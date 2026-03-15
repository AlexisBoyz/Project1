import random

list1 = [random.randint(1,20) for _ in range(8)]
list2 = [random.randint(1,20) for _ in range(8)]

min1 = min(list1)
max1 = max(list1)
min2 = min(list2)
max2 = max(list2)

print(list1)
print(list2)
print(f"Минимальное значение списка list1 = {min1},максимальное значение списка list1 = {max1}")
print(f"Минимальное значение списка list2 = {min2},максимальное значение списка list2 = {max2}")


