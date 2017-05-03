
def fib(n):
    f1 = 0
    f2 = 1
    i = 1
    fsu = 0
    while fsu <= n:
        print (f2)
        fsu = f1+f2
        f1 = f2
        f2 = fsu
        i += 1

n = int(input("Введите число: "))
fib (n)