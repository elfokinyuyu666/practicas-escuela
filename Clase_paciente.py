import time
from Clase_persona import Persona

class Paciente(Persona):

    def __init__(self, nombre, edad, sexo, telefono, correo,
                 peso, altura, padecimiento, medico=None):

        super().__init__()

        self.set__nombre(nombre)
        self.set__edad(edad)
        self.set__sexo(sexo)
        self.set__telefono(telefono)
        self.set__correo(correo)

        self.peso = peso
        self.altura = altura
        self.padecimiento = padecimiento
        self.medico = medico
        self.consultorio = None
        self.medico = None

    def calcular_imc(self):
            imc = self.peso / (self.altura ** 2)
            return imc

    def mostrar_datos(self):
        print("=== DATOS DEL PACIENTE ===")
        print("Nombre:", self.get__nombre())
        print("Edad:", self.get__edad())
        print("Sexo:", self.get__sexo())
        print("Teléfono:", self.get__telefono())
        print("Correo:", self.get__correo())
        print("Peso:", self.peso)
        print("Altura:", self.altura)
        print("Padecimiento:", self.padecimiento)
        print("Médico:", self.medico)

        imc = self.calcular_imc()
        print("IMC:", round(imc, 2))
