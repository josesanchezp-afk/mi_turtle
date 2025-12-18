# mi_turtle

Este proyecto contiene scripts simples en Python que simulan el movimiento de una tortuga en la consola. Los scripts permiten ingresar pasos y giros para representar el movimiento de la tortuga de manera textual.

## Archivos

### Untitled-1.py
Simula el movimiento horizontal de una tortuga. Pide al usuario la cantidad de pasos, imprime un mensaje y dibuja una línea de guiones seguida de una flecha (`>`) hacia la derecha.

```python
paso=int(input("Ingrese cantidad de pasos de la tortuga "))
print("La tortuga avanzará  "   + str(paso) + "pasos")
print("-"*paso +">")
```

**Ejemplo de salida (con input 5):**
```
Ingrese cantidad de pasos de la tortuga La tortuga avanzará  5pasos
----->
```

### Untitled-2.py
Simula el movimiento vertical de la tortuga. Pide pasos, imprime el mensaje y dibuja líneas verticales (`|`) con una flecha hacia abajo (`v`).

```python
paso=int(input("Ingrese cantidad de pasos de la tortuga "))
print("La tortuga avanzará  "   + str(paso) + "pasos")
print("|\n"*paso +"v")
```

**Ejemplo de salida (con input 3):**
```
Ingrese cantidad de pasos de la tortuga La tortuga avanzará  3pasos
|
|
|
v
```

### Untitled-3.py
Combina movimientos horizontal y vertical. Pide pasos horizontales y verticales, e imprime una representación en L con líneas y flecha.

```python
paso=int(input("Ingrese cantidad de pasos de la tortuga "))
print("La tortuga avanzará  "   + str(paso) + "pasos")
giro=int(input("Ingrese cantidad de pasos hacia abajo  "))
print("La tortuga avanzará  "   + str(giro) + "pasos")
print("|\n"* paso +"-"* giro +">")
```

**Ejemplo de salida (con inputs 2 y 4):**
```
Ingrese cantidad de pasos de la tortuga La tortuga avanzará  2pasos
Ingrese cantidad de pasos hacia abajo  La tortuga avanzará  4pasos
|
|
---->
```

### Untitled-4.1.py
Define funciones para movimientos derecha y abajo con valores fijos (5 pasos cada uno). Dibuja guiones para derecha y líneas verticales con espacios para abajo.

```python
Derecha = 5
izquierda = 5

def derecha(n):
  print("-" * n + ">")
def abajo(n):
  print((" " * Derecha + "|\n") * n + (" " * Derecha + "V"))

derecha(Derecha)
abajo(izquierda)
```

**Ejemplo de salida:**
```
----->
     |
     |
     |
     |
     |
     V
```

### Untitled-5.py
Similar al anterior, pero con una variable `escalones` que incrementa para simular un patrón de escalones o zigzag, ejecutando secuencias de movimientos.

```python
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
```

**Ejemplo de salida:**
```
                         ----->
                              |
                              |
                              |
                              |
                              |
                              V
                              ----->
                                   |
                                   |
                                   |
                                   |
                                   |
                                   V
                                   ----->
                                        |
                                        |
                                        |
                                        |
                                        |
                                        V
                                        ----->
                                             |
                                             |
                                             |
                                             |
                                             |
                                             V
                                             ----->
                                                  |
                                                  |
                                                  |
                                                  |
                                                  |
                                                  V
```

## Uso

Ejecuta cualquiera de los scripts con Python (ej. `python mi_turtle/Untitled-1.py`) y sigue las instrucciones en pantalla para ingresar los pasos.