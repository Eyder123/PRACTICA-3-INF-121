from typing import TypeVar, Generic

T = TypeVar('T')

class Contenedor(Generic[T]):
    def __init__(self):
        self._elemento = None  
        
    def guardar(self, elemento: T) -> None:
        """Guarda un elemento en el contenedor."""
        self._elemento = elemento

    def obtener(self) -> T:
        """Obtiene el elemento guardado. Lanza error si está vacío."""
        if self._elemento is None:
            raise ValueError("El contenedor está vacío")
        return self._elemento

    def esta_vacio(self) -> bool:
        """Verifica si el contenedor está vacío."""
        return self._elemento is None

    def limpiar(self) -> None:
        """Elimina el elemento guardado (vacía el contenedor)."""
        self._elemento = None

#Ejemplos
if __name__ == "__main__":
    print("Ejemplo 1: Contenedor de enteros")
    contenedor_int = Contenedor[int]()
    contenedor_int.guardar(100)
    print(f"Obtenido: {contenedor_int.obtener()}")  
    print(f"¿Vacío?: {contenedor_int.esta_vacio()}")  
    contenedor_int.limpiar()
    print(f"¿Vacío después de limpiar?: {contenedor_int.esta_vacio()}") 

    print("\nEjemplo 2: Contenedor de strings")
    contenedor_str = Contenedor[str]()
    contenedor_str.guardar("Programación Genérica")
    print(f"Obtenido: {contenedor_str.obtener()}") 
    print(f"¿Vacío?: {contenedor_str.esta_vacio()}")  

    print("\nEjemplo 3: Contenedor vacío (manejo de error)")
    contenedor_vacio = Contenedor[float]()
    try:
        print(contenedor_vacio.obtener())  
    except ValueError as e:
        print(f"Error: {e}") 