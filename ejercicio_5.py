i = 1
y = 1
if __name__ == "__main__":
    x = int(input("ingrese un numero para hallar su factorial: "))
    while i <= x :
        y *= i
        i += 1
    print (f"{i - 1}! = {y}")   