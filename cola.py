class ColaConsultorio:

    def __init__(self):
        self.cola = []

    def agregar_paciente(self, paciente):
        self.cola.append(paciente)

    def atender_paciente(self):
        if self.cola:
            return self.cola.pop(0)
        return None
