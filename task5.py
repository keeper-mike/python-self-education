print("\nЗадача 1.1:")
number = int(input("Введите число: "))

if 1 <= number <= 100 or 200 <= number <= 300:
    print("Число попадает в заданный диапазон")
else:
    print("Число не попадает в заданный диапазон")

print("\nЗадача 1.2:")
temperature = int(input("Начальная темтература воды: "))
time = 0

while temperature < 100:
    temperature += 1
    time += 2

print("Вода закипит через", time, "минут")

print("\nЗадача 1.3:")
x = int(input("Введите количество строк: "))
for i in range(1, x+1):
    print("{0}. 000".format(i))

print("\nЗадача 1.4:")
height = int(input("Введите высоту треугольника: "))

for i in range(1, height+1):
    for j in range(1, i+1):
        print("*", end="")
    print()

print("\nЗадача 2.1:")
A = float(input("Введите длину коробки: "))
B = float(input("Введите ширину коробки: "))
C = float(input("Введите высоту коробки: "))
M = float(input("Введите ширину двери: "))
K = float(input("Введите высоту двери: "))

if A <= M and B <= K or A <= K and B <= M or B <= M and C <= K or B <= K and C <= M or A <= M and C <= K or A <= K and C <= M:
    print("Коробка поместится в дверь")
else:
    print("Коробка не поместится в дверь")

print("\nЗадача 2.2:")
height = int(input("Введите высоту треугольника: "))

for i in range(height):
    print(' '*(height-i-1) + '*'*(2*i+1))

print("\nЗадача 2.3:")
N = int(input("Введите число N: "))
i = 1
while i ** 2 < N:
    print(i ** 2)
    i += 1

print("\nЗадача 3.1:")
n = int(input("Введите количество шариков мороженого: "))
can_buy = False

for i in range(n // 3 + 1):
    for j in range(n // 5 + 1):
        if i * 3 + j * 5 == n:
            can_buy = True
            break

if can_buy:
    print("Можно купить", n, "шариков мороженого")
else:
    print("Нельзя купить", n, "шариков мороженого")

print("\nЗадача 3.2:")
import math

X = float(input("Введите начальную сумму вклада в тысячах гривен: "))
Y = float(input("Введите годовую процентную ставку: "))
E = float(input("Введите желаемую конечную сумму вклада в тысячах гривен: "))

F = E * 1000
P = X * 1000
r = Y
t = math.log(F/P) / math.log(1 + r/100)

print("Сумма вклада превысит", E, "тысяч гривен через", round(t, 2), "лет")

print("\nЗадача 3.3:")
n = int(input("Введите число: "))
sum_digits = 0

while n > 0:
    digit = n % 10
    sum_digits += digit
    n = n // 10

print("Сумма цифр:", sum_digits)

