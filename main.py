cantidadCreados = 0
class Auto:
    def __init__(self, modelo, precio, asiento, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asiento = asiento = []
        self.marca = marca
        self.motor = motor
        self.registro = registro
        Auto.cantidadCreados = cantidadCreados
    
    def cantidadAsientos(self):
        totalAsientos = 0
        for i in range(0, len(self.asiento)):
            if i == None:
                continue
            if isinstance(self.asiento, Asiento):
                totalAsientos += 1
        return (totalAsientos)
    
    def verificarIntegridad(self):
        switch = True
        if self.motor.registro != self.registro:
            switch = False
        for asiento in self.asiento:
            if self.asiento.registro != self.registro:
                switch = False
        if switch == True:
            return("Auto original")
        else:
            return("Las piezas no son originales")

class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self, color):
        NewColor = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if color in NewColor:
            self.color = color

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    
    def cambiarRegistro (self, registro):
        self.registro = registro
    
    def asignarTipo(self, tipo):
        tipos = ["electrico","gasolina"]
        if tipo in tipos:
            self.tipo = tipo

