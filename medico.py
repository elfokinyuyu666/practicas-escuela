from persona import Persona

class Medico(Persona):

    def __init__(self, nombre, edad, sexo, telefono, correo,
                 especialidad, consultorio, num_empleado):

        super().__init__()

        self.set__nombre(nombre)
        self.set__edad(edad)
        self.set__sexo(sexo)
        self.set__telefono(telefono)
        self.set__correo(correo)

        self.especialidad = especialidad
        self.consultorio = consultorio
        self.num_empleado = num_empleado

    def mostrar_datos(self):
        print("=== MÉDICO ===")
        print(self.get__nombre(), self.especialidad, self.consultorio)
