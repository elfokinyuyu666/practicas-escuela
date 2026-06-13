import streamlit as st
import time
import random
import sys
import os

# Asegura que Streamlit Cloud encuentre tus archivos locales de clases
sys.path.append(os.path.dirname(os.path.abspath(_file_)))

from Clase_paciente import Paciente
from Clase_medico import Medico
from cola_consultorio import ColaConsultorio


st.set_page_config(page_title="Simulador Consultorio", layout="centered")
st.title("🏥 SIMULADOR DE CONSULTORIO EN TIEMPO REAL")


# =========================
# MÉDICOS
# =========================
medicos = [
    Medico("Dr. Carlos Hernández", 45, "Masculino", "3323675090", "hernandez@tusalud.com", "General", "1", "M001"),
    Medico("Dra. Ana López", 38, "Femenino", "3340756321", "anita@hospital.com", "Pediatría", "2", "M002"),
    Medico("Dr. Pedro Hernández", 50, "Masculino", "3315233297", "pedro@hospital.com", "Cardiología", "3", "M003")
]


# =========================
# ESTADO GLOBAL
# =========================
if "cola" not in st.session_state:
    st.session_state.cola = ColaConsultorio()

if "running" not in st.session_state:
    st.session_state.running = False


cola = st.session_state.cola


# =========================
# PACIENTES ALEATORIOS
# =========================
nombres = ["Juan", "Ana", "Luis", "María", "Pedro", "Sofía", "Carlos", "Elena"]
padecimientos = ["Gripe", "Migraña", "Dolor muscular", "Fiebre", "Infección"]


def generar_paciente():
    nombre = random.choice(nombres)
    edad = random.randint(18, 60)
    sexo = random.choice(["Masculino", "Femenino"])
    telefono = "33" + str(random.randint(10000000, 99999999))
    correo = nombre.lower() + "@mail.com"
    peso = random.randint(50, 90)
    altura = round(random.uniform(1.55, 1.85), 2)
    padecimiento = random.choice(padecimientos)
    medico = random.choice(medicos)

    return Paciente(nombre, edad, sexo, telefono, correo, peso, altura, padecimiento, medico)


# =========================
# CONTROLES
# =========================
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("▶️ Iniciar simulador"):
        st.session_state.running = True

with col2:
    if st.button("⏸️ Pausar"):
        st.session_state.running = False

with col3:
    if st.button("🔄 Reiniciar"):
        st.session_state.cola = ColaConsultorio()
        st.session_state.running = False


# =========================
# SIMULACIÓN
# =========================
st.subheader("⚙️ Estado del sistema")

placeholder = st.empty()


if st.session_state.running:

    # genera paciente nuevo aleatorio
    nuevo = generar_paciente()
    cola.agregar_paciente(nuevo)

    # atiende si hay cola
    if len(cola.cola) > 0:
        atendido = cola.atender_paciente()

        st.success(f"👤 Atendiendo: {atendido.get__nombre()}")
        st.write("🤒", atendido.padecimiento)
        st.write("👨‍⚕️", atendido.medico.get__nombre())
        st.write("🏥", atendido.medico.consultorio)
        st.write("⚖️ IMC:", round(atendido.calcular_imc(), 2))

    time.sleep(2)
    st.rerun()


# =========================
# COLA EN VIVO
# =========================
st.subheader("📊 Pacientes en espera")

if len(cola.cola) == 0:
    st.info("Sin pacientes en cola")
else:
    for i, p in enumerate(cola.cola, 1):
        st.write(f"{i}. {p.get__nombre()} - {p.padecimiento}")
    for i, p in enumerate(cola.cola, 1):
        st.write(f"{i}. {p.get__nombre()} - {p.padecimiento}")
