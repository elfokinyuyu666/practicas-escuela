import streamlit as st
import random
import time

from medico import Medico
from paciente import Paciente
from cola import ColaConsultorio

st.set_page_config(page_title="Consultorio", page_icon="🏥", layout="wide")

st.title("🏥 Simulación de Consultorio Médico")

# -------------------------
# Estado inicial
# -------------------------

if "init" not in st.session_state:

    medicos = [
        Medico("Dr. Carlos Hernández", 45, "M", "3323", "a@a.com", "General", "1", "M1"),
        Medico("Dra. Ana López", 38, "F", "3340", "b@b.com", "Pediatría", "2", "M2"),
        Medico("Dr. Pedro Ramírez", 50, "M", "3315", "c@c.com", "Cardiología", "3", "M3")
    ]

    pacientes = [
        Paciente("Juan Pérez", 25, "M", "111", "j@j.com", 80, 1.75, "Gripe"),
        Paciente("María López", 20, "F", "222", "m@m.com", 60, 1.65, "Migraña"),
        Paciente("Luis Torres", 32, "M", "333", "l@l.com", 90, 1.80, "Dolor")
    ]

    for p in pacientes:
        p.medico = random.choice(medicos)

    cola = ColaConsultorio()
    for p in pacientes:
        cola.agregar_paciente(p)

    st.session_state.cola = cola
    st.session_state.actual = None
    st.session_state.atendidos = []
    st.session_state.last = time.time()
    st.session_state.init = True

# -------------------------
# AUTO SIMULACIÓN
# -------------------------

if time.time() - st.session_state.last > 4:

    paciente = st.session_state.cola.atender_paciente()

    if paciente:
        st.session_state.actual = paciente
        st.session_state.atendidos.append(paciente.get__nombre())

    st.session_state.last = time.time()
    st.rerun()

# -------------------------
# UI
# -------------------------

col1, col2, col3 = st.columns(3)

col1.metric("En espera", len(st.session_state.cola.cola))
col2.metric("Atendidos", len(st.session_state.atendidos))

if st.session_state.actual:
    col3.metric("Consultorio", st.session_state.actual.medico.consultorio)

st.divider()

# -------------------------
# Paciente actual
# -------------------------

st.subheader("👨‍⚕️ Paciente en atención")

if st.session_state.actual:

    p = st.session_state.actual

    st.info(f"""
    Nombre: {p.get__nombre()}
    Padecimiento: {p.padecimiento}
    Médico: {p.medico.get__nombre()}
    """)

    st.success(f"IMC: {round(p.calcular_imc(), 2)}")

# -------------------------
# Cola
# -------------------------

st.subheader("🪑 Sala de espera")

for p in st.session_state.cola.cola:
    st.write(f"• {p.get__nombre()} - {p.padecimiento}")

# -------------------------
# Historial
# -------------------------

st.subheader("✅ Atendidos")

st.write(st.session_state.atendidos)
