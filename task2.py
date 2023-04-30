print("\n1) Простий калькулятор")
num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
operation = input("Введіть операцію (+, -, /, *, mod, pow, div): ")

if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '/':
    print(num1 / num2)
elif operation == '*':
    print(num1 * num2)
elif operation == 'mod':
    print(num1 % num2)
elif operation == 'pow':
    print(num1 ** num2)
elif operation == 'div':
    print(num1 // num2)
else:
    print("Неправильна операція")


print("\n2) Ділення націло двух чисел")
a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))

if a % b == 0:
    print("a ділиться на b націло")
else:
    print("a не ділиться на b націло")

if b % a == 0:
    print("b ділиться на a націло")
else:
    print("b не ділиться на a націло")


print("\n3) Однакові цифри")
number = int(input("Введіть трицифрове число: "))

digit1 = number // 100
digit2 = (number // 10) % 10
digit3 = number % 10

if digit1 == digit2 or digit1 == digit3 or digit2 == digit3:
    print("Серед цифр числа є однакові")
else:
    print("Серед цифр числа немає однакових")
