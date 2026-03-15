import random

list1 = [random.randint(1, 20) for _ in range(8)]
list2 = [random.randint(1, 20) for _ in range(8)]

list3 = list(set(list1+list2))

print(list1)
print(list2)
print(list3)