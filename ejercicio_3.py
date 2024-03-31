i = 0
x =int(input("Ingrese un numero para descomponerlo en numeros pares de forma descendente:  "))
i = x + i
while i >=2 and i <= x:
    if i % 2 == 0:
        print (i)
        i = i - 1
    else:
        i = i - 1