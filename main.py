cantidadCreados = 0
class Auto:
    def __init__(self, modelo, precio, asiento, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asiento
        self.marca = marca
        self.motor = motor
        self.registro = registro
        Auto.cantidadCreados = cantidadCreados
    
    def cantidadAsientos(self):
        totalAsientos = 0
        for asiento in self.asientos:
            if isinstance(asiento, Asiento):
                totalAsientos += 1
        return (totalAsientos)
    
    def verificarIntegridad(self):
        if self.motor.registro != self.registro:
            return("Las piezas no son originales")
        for asiento in self.asientos:
            if isinstance(asiento, Asiento):
                if asiento.registro != self.registro:
                    return("Las piezas no son originales")
        return("Auto original")


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
