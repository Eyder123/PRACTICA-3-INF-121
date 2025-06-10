ARCHIVO = 'productos.txt'

# Agregar un nuevo producto
def agregar_producto():
    codigo = input("Código: ")
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    with open(ARCHIVO, 'a') as file:
        file.write(f"{codigo},{nombre},{precio}\n")
    print("Producto guardado correctamente.")

# Mostrar todos los productos
def mostrar_productos():
    try:
        with open(ARCHIVO, 'r') as file:
            lineas = file.readlines()
            if not lineas:
                print("No hay productos registrados.")
                return
            for linea in lineas:
                codigo, nombre, precio = linea.strip().split(',')
                print(f"Código: {codigo} | Nombre: {nombre} | Precio: ${precio}")
    except FileNotFoundError:
        print("No hay productos registrados.")

# Menú principal
def menu():
    while True:
        print("\n1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
