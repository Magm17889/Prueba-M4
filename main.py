import csv
class Vehicle:
    def __init__(self, marca, modelo, numero_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.numero_ruedas = numero_ruedas

    def __str__(self):
        return f"Marca {self.marca}, modelo {self.modelo}, {self.numero_ruedas} ruedas"

class Automobile(Vehicle):
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, numero_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"Marca {self.marca}, modelo {self.modelo}, {self.numero_ruedas} ruedas, {self.velocidad} Km/h, {self.cilindrada} cc"

if __name__ == "__main__":
    num_vehicles = int(input("Cuantos Vehiculos desea insertar: "))
    vehicles = []

    for i in range(num_vehicles):
        print(f"\nDatos del automóvil {i + 1}")
        marca = input("Inserte la marca del automóvil: ")
        modelo = input("Inserte el modelo: ")
        numero_ruedas = int(input("Inserte el número de ruedas: "))
        velocidad = int(input("Inserte la velocidad en km/h: "))
        cilindrada = int(input("Inserte el cilindraje en cc: "))
        vehicle = Automobile(marca, modelo, numero_ruedas, velocidad, cilindrada)
        vehicles.append(vehicle)
        

    print("\nImprimiendo por pantalla los Vehículos:")
    for i, vehicle in enumerate(vehicles):
        print(f"Datos del automóvil {i + 1} : {vehicle}")

# parte N°2
print("\nImprimiendo 2 parte del ejercicio:")
    
class Particular(Automobile):
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada, asientos):
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindrada)
        self.asientos = asientos

    def __str__(self):
        return f"{super().__str__()}, {self.asientos} asientos"

class Carga(Automobile):
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada, kg_carga):
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindrada)
        self.kg_carga = kg_carga

    def __str__(self):
        return f"{super().__str__()}, {self.kg_carga} kg de carga"

class Bicycle(Vehicle):
    def __init__(self, marca, modelo, numero_ruedas, tipo_bicicleta):
        super().__init__(marca, modelo, numero_ruedas)
        self.tipo_bicicleta = tipo_bicicleta

    def __str__(self):
        return f"{super().__str__()}, Tipo {self.tipo_bicicleta}"

class Motorcycle(Bicycle):
    def __init__(self, marca, modelo, numero_ruedas, tipo_bicicleta, motor, cuadro, numero_radios):
        super().__init__(marca, modelo, numero_ruedas, tipo_bicicleta)
        self.motor = motor
        self.cuadro = cuadro
        self.numero_radios = numero_radios

    def __str__(self):
        return f"{super().__str__()}, Motor {self.motor}, Cuadro {self.cuadro}, {self.numero_radios} radios"
    
# Instancias de las clases
particular = Particular("Ford", "Fiesta", 4, 180, 500, 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, 1000, 20000)
bicicleta = Bicycle("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motorcycle("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)



# Verificación de instancias
print(f"Motocicleta es instancia con relación a Vehículo: {isinstance(motocicleta, Vehicle)}")
print(f"Motocicleta es instancia con relación a Automóvil: {isinstance(motocicleta, Automobile)}")
print(f"Motocicleta es instancia con relación a Vehículo Particular: {isinstance(motocicleta, Particular)}")
print(f"Motocicleta es instancia con relación a Vehículo de Carga: {isinstance(motocicleta, Carga)}")
print(f"Motocicleta es instancia con relación a Bicicleta: {isinstance(motocicleta, Bicycle)}")
print(f"Motocicleta es instancia con relación a Motocicleta: {isinstance(motocicleta, Motorcycle)}")

# parte N°3 del ejercicio

print("\nImprimiendo 3 parte del ejercicio:")

def guardar_datos_csv(nombre_archivo, vehiculos):
    try:
        with open(nombre_archivo, 'w', newline='') as archivo:
            archivo_csv = csv.writer(archivo)
            for vehiculo in vehiculos:
                archivo_csv.writerow([vehiculo.__class__, vehiculo.__dict__])
    except Exception as e:
        print(f"Error al guardar en archivo CSV: {e}")

def leer_datos_csv(nombre_archivo):
    vehiculos = []
    try:
        with open(nombre_archivo, 'r') as archivo:
            archivo_csv = csv.reader(archivo)
            for vehiculo in archivo_csv:
                vehiculos.append(vehiculo)
    except Exception as e:
        print(f"Error al leer archivo CSV: {e}")
    return vehiculos

if __name__ == "__main__":
    particular = Particular("Ford", "Fiesta", 4, 180, 500, 5)
    carga = Carga("Daft Trucks", "G 38", 10, 120, 1000, 20000)
    bicicleta = Bicycle("Shimano", "MT Ranger", 2, "Carrera")
    motocicleta = Motorcycle("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)    
    vehiculos = [particular, carga, bicicleta, motocicleta]
    guardar_datos_csv("vehiculos.csv", vehiculos)
    vehiculos_recuperados = leer_datos_csv("vehiculos.csv")

    print("Lista de Vehiculos")
    for vehiculo in vehiculos_recuperados:
        print(vehiculo)
### esto es una prueba de uso de getter y setter ya que en la ejecucion del codigo no es necesaria, pero para cumplir la rubrica 
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    # Métodos accesadores (getters)
    def get_nombre(self):
        return self._nombre

    def get_edad(self):
        return self._edad

    # Métodos mutadores (setters)
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_edad(self, edad):
        self._edad = edad

# Ejemplo de uso
persona = Persona("Juan", 30)

# Usando los getters
("\nImprimiendo   parte del ejercicio, para usar el setters y getters")
print(persona.get_nombre())  # Salida: Juan
print(persona.get_edad())    # Salida: 30

# Usando los setters
persona.set_nombre("Ana")
persona.set_edad(25)

# Verificando los cambios
print(persona.get_nombre())  # Salida: Ana
print(persona.get_edad())    # Salida: 25
