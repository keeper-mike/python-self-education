
print("\nУровень1 \n 1)")
a = int(input("Введите число: "))
b = int(input("Введите степень: "))
print(a ** b)

print("\n2)")
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if a > b:
    print(a, "больше", b)
else:
    print(b, "больше", a)

print("\n3)")
sum_uah = float(input("Введите сумму в гривнах: "))
rate_usd = float(input("Введите курс доллара: "))
sum_usd = sum_uah / rate_usd
print("Сумма в долларах: ", sum_usd)

print("\n4)")
day = int(input("Введите число от 1 до 7: "))
if day == 1:
    print("Понедельник")
elif day == 2:
    print("Вторник")
elif day == 3:
    print("Среда")
elif day == 4:
    print("Четверг")
elif day == 5:
    print("Пятница")
elif day == 6:
    print("Суббота")
elif day == 7:
    print("Воскресенье")
else:
    print("Ошибка ввода")

print("\nУровень 2 \n 1)")
a = int(input("Введите число: "))
if a % 2 == 0:
    print("четное")
else:
    print("нечетное")

print("\n2)")
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
min_number = a
if b < min_number:
    min_number = b
if c < min_number:
    min_number = c
print("Наименьшее число: ", min_number)

print("\n3)")
a = int(input("Рекомендуется спать хотя бы столько часов: "))
b = int(input("Не стоит спать более столько часов: "))
n = int(input("Сколько часов Аня спит в сутки: "))
if n >= a and n <= b:
    print("Это нормально")
elif n < a:
    print("Недосып")
else:
    print("Пересып")
