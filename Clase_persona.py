class Persona:

    def __init__(self):
        self.__nombre = ""
        self.__edad = 0
        self.__sexo = ""
        self.__telefono = ""
        self.__correo = ""

    def set_nombre(self, no):
        self.__nombre = no

    def set_edad(self, e):
        self.__edad = e

    def set_sexo(self, s):
        self.__sexo = s

    def set_telefono(self, t):
        self.__telefono = t

    def set_correo(self, co):
        self.__correo = co

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_sexo(self):
        return self.__sexo

    def get_telefono(self):
        return self.__telefono

    def get_correo(self):
        return self.__correo
