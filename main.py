from clase_paciente import Paciente
from clase_medico import Medico
from cola_consultorio import ColaConsultorio
import random


# esta es la lista de medicos recuerda que viene de la clase medico.py
medico1 = Medico(
    "Dr. Carlos hernandez",
    45,
    "Masculino",
    "3323675090",
    "hernandez@tusalud.com",
    "Medicina general",
    "Consultorio 1",
    "M001"
)

medico2 = Medico(
    "Dra. Ana Lopez",
    38,
    "Femenino",
    "3340756321",
    "anitalopez@hospital.com",
    "Pediatria",
    "Consultorio 2",
    "M002"
)

medico3 = Medico(
    "Dr. Pedro Hernandez",
    50,
    "Masculino",
    "3315233297",
    "pedrinhernandez@tusalud.com",
    "Cardiologia",
    "Consultorio 3",
    "M003"
)


# grandes los medicos
medicos = [medico1, medico2, medico3]


# los pacientes son mis compas
lista_pacientes = []


p1 = Paciente(
    "Jonathan Gutierrez",
    25,
    "Masculino",
    "3311411497",
    "jona060@gmail.com",
    80,
    1.75,
    "Gripe"
)

p2 = Paciente(
    "christian casas",
    20,
    "Femenino",
    "3355555555",
    "christiancas23@gmail.com",
    60,
    1.65,
    "Migraña"
)

p3 = Paciente(
    "alexis pimentel",
    32,
    "Masculino",
    "3366666666",
    "alexispime5@gmail.com",
    90,
    1.80,
    "Dolor muscular",
)


# el random asigna un medico aleatorio a cada paciente de la lista de medicos
p1.medico = random.choice(medicos)
p2.medico = random.choice(medicos)
p3.medico = random.choice(medicos)


# aqui se agregan los pacientes a la lista de pacientes para 
# luego pasarlos a la cola del consultorio
lista_pacientes.append(p1)
lista_pacientes.append(p2)
lista_pacientes.append(p3)


# creamos la cola del consultorio
cola = ColaConsultorio()


# Pasamos los pacientes a la cola del consultorio
for paciente in lista_pacientes:
    cola.agregar_paciente(paciente)

# aqui salen los pacientes en espera
cola.iniciar_simulacion()


# imprime el paciente que se va a atender
print("\n===== ATENDIENDO PACIENTE =====")

paciente_atendido = cola.atender_paciente()

if paciente_atendido:
    print("Paciente:", paciente_atendido.get__nombre())
    print("Padecimiento:", paciente_atendido.padecimiento)
    print("Médico asignado:",
          paciente_atendido.medico.get__nombre())
    print ("Consultorio:", paciente_atendido.medico.consultorio)


    imc = paciente_atendido.calcular_imc()

    print("IMC:", round(imc, 2))


# sale la cola actualizada despues de atender al paciente
print("\n===== COLA ACTUAL =====")
cola.iniciar_simulacion()