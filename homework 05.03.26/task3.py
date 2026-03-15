import random

list1 = [random.randint(1, 20) for _ in range(10)]
list2 = [random.randint(1, 20) for _ in range(10)]

list3 = []
for item in list1:
    if item in list2 and item not in list3:
        list3.append(item)

print(list1)
print(list2)
print(list3)