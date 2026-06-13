from Clase_persona import Persona

class Medico(Persona):

    def __init__(self, nombre, edad, sexo, telefono, correo,
                 especialidad, consultorio, num_empleado):

        super().__init__(nombre, edad,, sexo, telefono, correo)

        self.set__nombre(nombre)
        self.set__edad(edad)
        self.set__sexo(sexo)
        self.set__telefono(telefono)
        self.set__correo(correo)

        self.especialidad = especialidad
        self.consultorio = consultorio
        self.num_empleado = num_empleado

    def mostrar_datos(self):
        print("===== DATOS DEL MÉDICO =====")
        print("Nombre:", self.get__nombre())
        print("Edad:", self.get__edad())
        print("Sexo:", self.get__sexo())
        print("Teléfono:", self.get__telefono())
        print("Correo:", self.get__correo())
        print("Especialidad:", self.especialidad)
        print("Consultorio:", self.consultorio)
        print("Número de empleado:", self.num_empleado)
