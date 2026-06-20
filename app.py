import streamlit as st
import random
import time

from medico import Medico
from paciente import Paciente
from cola import ColaConsultorio

st.set_page_config(page_title="Consultorio", page_icon="🏥", layout="wide")

st.title("🏥 Simulación de Consultorio Médico")

# -------------------------
# INICIALIZACIÓN
# -------------------------

def inicializar():

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

    return cola


# -------------------------
# SESSION STATE
# -------------------------

if "cola" not in st.session_state:
    st.session_state.cola = inicializar()
    st.session_state.atendidos = []
    st.session_state.actual = None
    st.session_state.simulacion = False
    st.session_state.last_time = time.time()


# -------------------------
# BOTONES
# -------------------------

colb1, colb2 = st.columns(2)

with colb1:
    if st.button("▶️ Iniciar simulación"):
        st.session_state.simulacion = True

with colb2:
    if st.button("🔄 Reiniciar simulación"):
        st.session_state.cola = inicializar()
        st.session_state.atendidos = []
        st.session_state.actual = None
        st.session_state.simulacion = False
        st.session_state.last_time = time.time()
        st.rerun()


# -------------------------
# SIMULACIÓN AUTOMÁTICA (NO BLOQUEANTE)
# -------------------------

if st.session_state.simulacion:

    if time.time() - st.session_state.last_time > 4:

        paciente = st.session_state.cola.atender_paciente()

        if paciente:
            st.session_state.actual = paciente
            st.session_state.atendidos.append(paciente.get__nombre())

        st.session_state.last_time = time.time()
        st.rerun()


# -------------------------
# UI
# -------------------------

st.divider()

col1, col2, col3 = st.columns(3)

col1.metric("⏳ En espera", len(st.session_state.cola.cola))
col2.metric("✅ Atendidos", len(st.session_state.atendidos))

consultorio = "-"
if st.session_state.actual:
    consultorio = st.session_state.actual.medico.consultorio

col3.metric("🏥 Consultorio", consultorio)


# -------------------------
# PACIENTE ACTUAL
# -------------------------

st.subheader("👨‍⚕️ Paciente en atención")

if st.session_state.actual:

    p = st.session_state.actual

    st.markdown(
        f"""
        <div style="
            background-color:#F8F9F9;
            padding:20px;
            border-radius:15px;
            border-left:6px solid #2E86C1;
        ">
            <h3>{p.get__nombre()}</h3>
            <p><b>Padecimiento:</b> {p.padecimiento}</p>
            <p><b>Médico:</b> {p.medico.get__nombre()}</p>
            <p><b>Consultorio:</b> {p.medico.consultorio}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.success(f"📊 IMC: {round(p.calcular_imc(), 2)}")

else:
    st.info("No hay paciente en atención")


# -------------------------
# SALA DE ESPERA
# -------------------------

st.subheader("🪑 Sala de espera")

if len(st.session_state.cola.cola) > 0:
    for p in st.session_state.cola.cola:
        st.write(f"🧑‍⚕️ {p.get__nombre()} — {p.padecimiento}")
else:
    st.success("✔ Sala de espera vacía")


# -------------------------
# HISTORIAL
# -------------------------

st.subheader("📋 Historial de atención")

st.write(st.session_state.atendidos)
