from typing import TypeVar, Protocol

class Comparable(Protocol):
    def __gt__(self, other: 'Comparable') -> bool: ...

T = TypeVar('T', bound=Comparable)

def obtener_mayor(a: T, b: T) -> T:
    return a if a > b else b
# Prueba
print(obtener_mayor(10, 5))           
print(obtener_mayor("zebra", "gato")) 
print(obtener_mayor(3.5, 7.1))       
