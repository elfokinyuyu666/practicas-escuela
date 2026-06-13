class Persona:

    def _init_(self):
        self.__nombre=""
        self.__edad=0
        self.__sexo=""
        self.__telefono=""
        self.__correo=""

    def set__nombre(self,no):
        self.__nombre=no
 
    def set__edad(self,e):
        self.__edad=e

    def set__sexo(self,s):
        self.__sexo=s

    def set__telefono(self,t):
        self.__telefono=t

    def set__correo(self,co):
        self.__correo=co

    def get__nombre(self):
        return self.__nombre

    def get__edad(self):
        return self.__edad

    def get__sexo(self):
        return self.__sexo

    def get__telefono(self):
        return self.__telefono
    
    def get__correo(self):
        return self.__correo
