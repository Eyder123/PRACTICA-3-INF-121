class Cliente:
    def __init__(self, id: int, nombre: str, telefono: int):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return f"Cliente(id={self.id}, nombre={self.nombre}, telefono={self.telefono})"

    def a_linea(self):
        return f"{self.id},{self.nombre},{self.telefono}\n"

    @staticmethod
    def desde_linea(linea: str):
        partes = linea.strip().split(',')
        return Cliente(int(partes[0]), partes[1], int(partes[2]))


class ArchivoCliente:
    def __init__(self, nomA: str):
        self.nomA = nomA
        self.crearArchivo()

    def crearArchivo(self):
        try:
            open(self.nomA, 'x').close()
        except FileExistsError:
            pass

    def guardaCliente(self, c: Cliente):
        with open(self.nomA, 'a') as f:
            f.write(c.a_linea())
        print(f"Cliente guardado: {c}")

    def buscarCliente(self, id_cliente: int) -> Cliente:
        with open(self.nomA, 'r') as f:
            for linea in f:
                cliente = Cliente.desde_linea(linea)
                if cliente.id == id_cliente:
                    return cliente
        return None

    def buscarCelularCliente(self, id_cliente: int) -> Cliente:
        cliente = self.buscarCliente(id_cliente)
        if cliente:
            print(f"Número de celular: {cliente.telefono}")
        return cliente


# Prueba
if __name__ == "__main__":
    archivo = ArchivoCliente("clientes.txt")

    archivo.guardaCliente(Cliente(1, "Juan Pérez", 555123456))
    archivo.guardaCliente(Cliente(2, "Laura Gómez", 555987654))

    resultado = archivo.buscarCliente(2)
    print(f"Cliente encontrado: {resultado}" if resultado else "Cliente no encontrado.")

    resultado_cel = archivo.buscarCelularCliente(1)
    print(f"Resultado buscarCelularCliente: {resultado_cel}" if resultado_cel else "No se encontró el cliente.")
