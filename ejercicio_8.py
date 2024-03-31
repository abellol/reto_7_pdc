def es_primo(x:int) -> bool:
  if x <= 1:
    return False
  i = 2
  while i <= (x ** 0.5):
    if x % i == 0:
      return False
    i += 1
  return True
if __name__ == "__main__":
  max_prim : int = 100
  x : int = 2
  print("Numeros primos de 1 a 100:")
  while x <= max_prim:
    if es_primo(x) == True:
      print (x)
    x += 1