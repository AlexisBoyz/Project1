import random

list1 = [random.randint(1, 20) for _ in range(10)]
list2 = [random.randint(1, 20) for _ in range(10)]

list3 = []

for item in list1:
    if list1.count(item) == 1 and item not in list2:
        list3.append(item)

for item in list2:
    if list2.count(item) == 1 and item not in list1:
        list3.append(item)

print(list1)
print(list2)
print(list3)