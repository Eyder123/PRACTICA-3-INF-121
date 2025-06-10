import json

class Medicamento:
    def __init__(self, nombre="", codMedicamento=0, tipo="", precio=0.0):
        self.nombre = nombre
        self.codMedicamento = codMedicamento
        self.tipo = tipo
        self.precio = precio

    def getTipo(self):
        return self.tipo

    def getPrecio(self):
        return self.precio

    def getNombre(self):
        return self.nombre

    def mostrar(self):
        return f"{self.codMedicamento} - {self.nombre} ({self.tipo}) - ${self.precio:.2f}"

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "codMedicamento": self.codMedicamento,
            "tipo": self.tipo,
            "precio": self.precio
        }

    @classmethod
    def from_dict(cls, d):
        return cls(d["nombre"], d["codMedicamento"], d["tipo"], d["precio"])

class Farmacia:
    def __init__(self, nombreFarmacia="", sucursal=0, direccion="", medicamentos=None):
        self.nombreFarmacia = nombreFarmacia
        self.sucursal = sucursal
        self.direccion = direccion
        self.m = medicamentos if medicamentos else []

    def mostrar(self):
        print(f"Farmacia: {self.nombreFarmacia} | Sucursal: {self.sucursal} | Dirección: {self.direccion}")
        for med in self.m:
            print("  ", med.mostrar())

    def getDireccion(self):
        return self.direccion

    def getSucursal(self):
        return self.sucursal

    def mostrarMedicamentos(self, tipo):
        return [med.mostrar() for med in self.m if med.getTipo().lower() == tipo.lower()]

    def buscaMedicamento(self, nombre):
        return any(med.getNombre().lower() == nombre.lower() for med in self.m)

    def to_dict(self):
        return {
            "nombreFarmacia": self.nombreFarmacia,
            "sucursal": self.sucursal,
            "direccion": self.direccion,
            "medicamentos": [med.to_dict() for med in self.m]
        }

    @classmethod
    def from_dict(cls, d):
        medicamentos = [Medicamento.from_dict(m) for m in d["medicamentos"]]
        return cls(d["nombreFarmacia"], d["sucursal"], d["direccion"], medicamentos)

class ArchFarmacia:
    def __init__(self, nombreArchivo):
        self.na = nombreArchivo

    def crearArchivo(self, farmacias):
        data = [f.to_dict() for f in farmacias]
        with open(self.na, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

    def leerArchivo(self):
        with open(self.na, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return [Farmacia.from_dict(d) for d in data]

    def mostrarMedicamentosTos(self, sucursalX):
        farmacias = self.leerArchivo()
        for f in farmacias:
            if f.getSucursal() == sucursalX:
                print(f"\nMedicamentos para la tos en la sucursal {sucursalX}:")
                meds = f.mostrarMedicamentos("tos")
                for m in meds:
                    print("  ", m)

    def buscarMedicamentoGolpex(self):
        farmacias = self.leerArchivo()
        print("\nFarmacias que tienen 'Golpex':")
        for f in farmacias:
            if f.buscaMedicamento("Golpex"):
                print(f"  Sucursal {f.getSucursal()} - Dirección: {f.getDireccion()}")

# Crear instancias y probar
med1 = Medicamento("Golpex", 101, "tos", 12.5)
med2 = Medicamento("Paracetamol", 102, "resfrio", 8.0)
med3 = Medicamento("Broncure", 103, "tos", 10.0)

farm1 = Farmacia("Farmacia Central", 1, "Calle 123", [med1, med2])
farm2 = Farmacia("Farmacia Salud", 2, "Av. Siempre Viva", [med3])

archivo = ArchFarmacia("farmacias.json")
archivo.crearArchivo([farm1, farm2])  # a) Guardar en archivo JSON

archivo.mostrarMedicamentosTos(1)      # b)
archivo.buscarMedicamentoGolpex()      # c)