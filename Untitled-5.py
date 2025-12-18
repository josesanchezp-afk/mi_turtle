derechar = 5
izquierda = 5
escalones = 5

def derecha(n):
  global escalones
  espaciosIzquierda = " " * derechar * escalones
  print(espaciosIzquierda + "-" * n + ">")
def abajo(n):
  global escalones
  espaciosIzquierda = " " * derechar * escalones
  print((espaciosIzquierda + (" " * derechar + "|\n")) * n + (espaciosIzquierda + " " * derechar + "V"))
  escalones = escalones + 1

derecha(derechar)
abajo(izquierda)

derecha(derechar)
abajo(izquierda)

derecha(derechar)
abajo(izquierda)

derecha(derechar)
abajo(izquierda)
derecha(derechar)
abajo(izquierda)