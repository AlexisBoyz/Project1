# Задание 1
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
g = float(input("Введите третье число: "))

print("Выберите, какую операцию вы хотите совершить?")
print("1 - Cумма трёх чисел")
print("2 - Произведение трёх чисел")

choice = int(input("Введите операцию: '1' или '2': "))

if choice == 1 :
    result = a + b + g
    print(f"Сумма чисел {a}, {b} и {g} равна {result}")
elif choice == 2 :
    result = a * b * g
    print(f"Произведение чисел {a}, {b}, {g} равна {result}")
else:
    print(f"Ошибка! Выбрана неверная операция!")

# Задание 2
firstNum = float(input("Введите первое число: "))
secondNum = float(input("Введите второе число: "))
thirdNum = float(input("Введите третье число: "))

print("Какую операцию вы хотите совершить?")
print("1 - максимальное число")
print("2 - минимальное число")
print("3 - сренднеарифметическое число")

choice2 = int(input("Выберите операцию: '1', '2' или '3': "))

if choice2 == 1 :
    maximum = max(firstNum, secondNum, thirdNum)
    print(f"Максимальное число из данных чисел: {maximum}")
elif choice2 == 2 :
    minimum = min(firstNum, secondNum, thirdNum)
    print(f"Минимальное число из данных чисел: {minimum}")
elif choice2 == 3 :
    average = (firstNum + secondNum + thirdNum) / 3
    print(f"Сренднеарифметическое число из данных чисел: {average}")
else: print("Ошибка! Выбрана неверная операция!")

# Задание 3
distance = float(input("Введите количество метров: "))

print("Какую операцию вы хотите совершить?")
print("1 - перевести метры в мили")
print("2 - перевести метры в дюймы")
print("3 - перевести метры в ярды")

choice3 = int(input("Выберите операцию: '1' , '2' или '3': "))

if choice3 == 1 :
    miles = float(distance) / 1609,34
    print(f"При переводе {distance} метров в мили, получилось: {miles} миль")
elif choice3 == 2 :
    inches = float(distance) * 39.37
    print(f"При переводе {distance} метров в дюймы, получилось: {inches} дюймов")
elif choice3 == 3 :
    yards = float(distance) * 1.09
    print(f"При переводе {distance} метров в ярды, получилось: {yards} ярдов")