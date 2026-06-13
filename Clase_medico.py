from Clase_persona import Persona

class Medico(Persona):

    def _init_(self, nombre, edad, sexo, telefono, correo,
                 especialidad, consultorio, num_empleado):

        super()._init_()

        self.set__nombre(nombre)
        self.set__edad(edad)
        self.set__sexo(sexo)
        self.set__telefono(telefono)
        self.set__correo(correo)

        self.especialidad = especialidad
        self.consultorio = consultorio
        self.num_empleado = num_empleado

    def mostrar_datos(self):
        return {
            "Nombre": self.get__nombre(),
            "Edad": self.get__edad(),
            "Sexo": self.get__sexo(),
            "Telefono": self.get__telefono(),
            "Correo": self.get__correo(),
            "Especialidad": self.especialidad,
            "Consultorio": self.consultorio,
            "Numero Empleado": self.num_empleado
        }
