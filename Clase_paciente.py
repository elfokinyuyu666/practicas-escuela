import time
from Clase_persona import Persona

class Paciente(Persona):

    def __init__(self, nombre, edad, sexo, telefono, correo,
                 peso, altura, padecimiento, medico=None):

        super().__init__()

        self.set_nombre(nombre)
        self.set_edad(edad)
        self.set_sexo(sexo)
        self.set_telefono(telefono)
        self.set_correo(correo)

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
        print("Nombre:", self.get_nombre())
        print("Edad:", self.get_edad())
        print("Sexo:", self.get_sexo())
        print("Teléfono:", self.get_telefono())
        print("Correo:", self.get_correo())
        print("Peso:", self.peso)
        print("Altura:", self.altura)
        print("Padecimiento:", self.padecimiento)
        print("Médico:", self.medico)

        imc = self.calcular_imc()
        print("IMC:", round(imc, 2))
