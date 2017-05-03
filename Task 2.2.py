def bank (n, m, years):
    i = 2
    bablo = n + n/10
    while i <= years:
        bablo = bablo + m
        bablo = bablo + bablo/10
        i+=1
    return bablo

n = float (input("Введите размер вклада: "))
m = float (input("Введите сумму пополнения: "))
years = int(input("Введите срок вклада в годах: "))
print (bank (n, m, years))
