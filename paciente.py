from persona import Persona

class Paciente(Persona):

    def __init__(self, nombre, edad, sexo, telefono, correo,
                 peso, altura, padecimiento):

        super().__init__()

        self.set__nombre(nombre)
        self.set__edad(edad)
        self.set__sexo(sexo)
        self.set__telefono(telefono)
        self.set__correo(correo)

        self.peso = peso
        self.altura = altura
        self.padecimiento = padecimiento
        self.medico = None

    def calcular_imc(self):
        return self.peso / (self.altura ** 2)
