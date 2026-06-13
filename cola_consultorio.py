import time
class ColaConsultorio:


    def __init__(self):
        self.cola = []


    def agregar_paciente(self, paciente):
        self.cola.append(paciente)


    def atender_paciente(self):
        if len(self.cola) > 0:
            return self.cola.pop(0)
        return None


    # AQUÍ PEGAS LA FUNCIÓN
    def iniciar_simulacion(self):
        while len(self.cola) > 0:

            print("\n===== ATENDIENDO PACIENTE =====")

            paciente = self.atender_paciente()

            print("Paciente:", paciente.get__nombre())
            print("Padecimiento:", paciente.padecimiento)
            print("Médico asignado:", paciente.medico.get__nombre())
            print("Consultorio:", paciente.medico.consultorio)

            print("Consulta terminada...")
            print("Esperando siguiente paciente...")

            time.sleep(5)
   