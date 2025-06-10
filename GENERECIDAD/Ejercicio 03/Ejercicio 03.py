from typing import Generic, TypeVar, List

T = TypeVar('T')

class Pila(Generic[T]):
    def __init__(self):
        self.elementos: List[T] = []

    def apilar(self, elemento: T):
        self.elementos.append(elemento)

    def desapilar(self) -> T:
        if not self.esta_vacia():
            return self.elementos.pop()
        raise IndexError("La pila está vacía")

    def esta_vacia(self) -> bool:
        return len(self.elementos) == 0

    def mostrar(self):
        print("Contenido de la pila (cima al final):", self.elementos)

# c) Pruebas

# Pila de enteros
pila_enteros = Pila[int]()
pila_enteros.apilar(10)
pila_enteros.apilar(20)
pila_enteros.mostrar()
print("Elemento desapilado:", pila_enteros.desapilar())
pila_enteros.mostrar()

# Pila de cadenas
pila_cadenas = Pila[str]()
pila_cadenas.apilar("Hola")
pila_cadenas.apilar("Mundo")
pila_cadenas.mostrar()
print("Elemento desapilado:", pila_cadenas.desapilar())
pila_cadenas.mostrar()