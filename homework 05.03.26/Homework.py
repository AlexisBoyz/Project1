#Task 1

import random

list1 = [random.randint(1, 100) for _ in range(5)]
list2 = [random.randint(1,100) for _ in range(5)]

list3 = list2 + list1

print(list1)
print(list2)
print(list3)

