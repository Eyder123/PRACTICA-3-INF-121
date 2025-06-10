from typing import Generic, TypeVar

# Tipo genérico T
T = TypeVar('T')

# Clase genérica
class Caja(Generic[T]):
    def __init__(self):
        self.contenido = None

    def guardar(self, valor: T):
        self.contenido = valor

    def obtener(self) -> T:
        return self.contenido

# a)
caja_entero = Caja[int]()
caja_entero.guardar(123)
# b) 
caja_texto = Caja[str]()
caja_texto.guardar("Hola mundo")

# c) Mostramos el contenido
print("Contenido de caja_entero:", caja_entero.obtener())
print("Contenido de caja_texto:", caja_texto.obtener())