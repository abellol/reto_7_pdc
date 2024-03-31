
i : int = 1
if __name__ == "__main__":
    x = int(input("Ingrese un numero entre 2 y 50 para mostrar sus divisores:  "))
    if x <= 50 and x >= 2:
        while i <= x:
            if x % i == 0:
                print(f"{x} es divisible entre {i}")
                i += 1
            else:
                i += 1
    else:
        print("no está dentro del rango esperado...")