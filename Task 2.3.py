def opera (a, b, c):
    if c == '+':
        d = a + b
        return d
    elif c == '-':
        d = a - b
        return d
    elif c == '*':
        d = a * b
        return d 
    elif c =='/':
        d = a / b
        return d
    else:
        d = "Неизвестная операция"
        return d

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = input("Введите операцию: ")
print (opera (a, b, c))
