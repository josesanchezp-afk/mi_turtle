Derecha = 5
izquierda = 5

def derecha(n):
  print("-" * n + ">")
def abajo(n):
  print((" " * Derecha + "|\n") * n + (" " * Derecha + "V"))

derecha(Derecha)
abajo(izquierda)