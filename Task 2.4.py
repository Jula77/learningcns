def pryamo (a, b):
    d = 2 * (a + b)
    e = a * b
    import math
    f = math.sqrt(a**2 + b**2)
    """return d, e, f"""
    print ("Периметр:", d)
    print ("Площадь:", e)
    print ("Диагональ:", f)

a = float(input("Введите первую сторону: "))
b = float(input("Введите первую сторону: "))
"""d, e, f = 0"""
pryamo (a, b)
"""print (pryamo (a, b))"""