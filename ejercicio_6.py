import random
num = random.randint(1, 100)
bandera : bool = True
#print(num)
if __name__ == "__main__":
    while bandera or x != num:
        bandera = False
        x = int(input("Ingrese un numero entre 1 y 100 para tratar de adivinar: "))
        if x < num:
            print(f"el numero es mayor que {x}")
        elif x > num:
            print(f"el numero es menor que {x}")
    print(f"felicidades, el numero misterioso era: {x}")