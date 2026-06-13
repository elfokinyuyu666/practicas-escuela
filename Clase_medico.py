from Clase_persona import Persona

class Medico(Persona):

    def __init__(self, nombre, edad, sexo, telefono, correo,
                 especialidad, consultorio, num_empleado):

        super().__init__()

        self.set_nombre(nombre)
        self.set_edad(edad)
        self.set_sexo(sexo)
        self.set_telefono(telefono)
        self.set_correo(correo)

        self.especialidad = especialidad
        self.consultorio = consultorio
        self.num_empleado = num_empleado

    def mostrar_datos(self):
       print("===== DATOS DEL MÉDICO =====")
       print("Nombre:", self.get_nombre())
       print("Edad:", self.get_edad())
       print("Sexo:", self.get_sexo())
       print("Teléfono:", self.get_telefono())
       print("Correo:", self.get_correo())
       print("Especialidad:", self.especialidad)
       print("Consultorio:", self.consultorio)
       print("Número de empleado:", self.num_empleado)
       print("Especialidad:", self.especialidad)
       print("Consultorio:", self.consultorio)
       print("Número de empleado:", self.num_empleado)
