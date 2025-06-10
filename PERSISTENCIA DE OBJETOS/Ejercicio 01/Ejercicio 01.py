class Empleado:
    def __init__(self, nombre: str, edad: int, salario: float):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def __str__(self):
        return f"{self.nombre},{self.edad},{self.salario}"  # para guardar en archivo

    @staticmethod
    def desde_linea(linea: str):
        nombre, edad, salario = linea.strip().split(",")
        return Empleado(nombre, int(edad), float(salario))


class ArchivoEmpleado:
    def __init__(self, nomA: str):
        self.nomA = nomA
        self.crearArchivo()

    def crearArchivo(self):
        try:
            open(self.nomA, 'x').close()
        except FileExistsError:
            pass  # ya existe

    def guardarEmpleado(self, e: Empleado):
        with open(self.nomA, 'a') as f:
            f.write(str(e) + '\n')
        print(f"Empleado guardado: {e}")

    def _leerEmpleados(self):
        empleados = []
        with open(self.nomA, 'r') as f:
            for linea in f:
                if linea.strip():
                    empleados.append(Empleado.desde_linea(linea))
        return empleados

    def buscaEmpleado(self, n: str):
        for e in self._leerEmpleados():
            if e.nombre == n:
                return e
        return None

    def mayorSalario(self, s: float):
        for e in self._leerEmpleados():
            if e.salario > s:
                return e
        return None


if __name__ == "__main__":
    archivo = ArchivoEmpleado("empleados.txt")

    archivo.guardarEmpleado(Empleado("Ana", 28, 3500.0))
    archivo.guardarEmpleado(Empleado("Luis", 35, 4500.0))
    archivo.guardarEmpleado(Empleado("Marta", 40, 3800.0))

    # Buscar empleado por nombre
    nombre = "Luis"
    e = archivo.buscaEmpleado(nombre)
    print(f"Empleado encontrado: {e}" if e else "Empleado no encontrado.")

    # Buscar empleado por salario
    sueldo = 3600.0
    e2 = archivo.mayorSalario(sueldo)
    print(f"Empleado con salario mayor a {sueldo}: {e2}" if e2 else "No se encontró empleado con salario mayor.")
