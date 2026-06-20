import streamlit as st
import random
import time

from medico import Medico
from paciente import Paciente
from cola import ColaConsultorio

st.set_page_config(page_title="Consultorio", page_icon="🏥", layout="wide")

st.markdown(
    "<h1 style='text-align:center;color:#2E86C1;'>🏥 Consultorio Médico</h1>",
    unsafe_allow_html=True
)

st.divider()

# -------------------------
# INICIALIZACIÓN
# -------------------------

if "cola" not in st.session_state:

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

    # control de simulación
    st.session_state.simulacion = False
    st.session_state.last_time = time.time()

# -------------------------
# BOTÓN DE INICIO
# -------------------------

if not st.session_state.simulacion:

    if st.button("▶️ Iniciar simulación"):

        st.session_state.simulacion = True
        st.rerun()

# -------------------------
# SIMULACIÓN AUTOMÁTICA
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
# DASHBOARD
# -------------------------

col1, col2, col3 = st.columns(3)

col1.metric("⏳ En espera", len(st.session_state.cola.cola))
col2.metric("✅ Atendidos", len(st.session_state.atendidos))

consultorio = "-"
if st.session_state.actual:
    consultorio = st.session_state.actual.medico.consultorio

col3.metric("🏥 Consultorio", consultorio)

st.divider()

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
        </div>
        """,
        unsafe_allow_html=True
    )

    st.success(f"📊 IMC: {round(p.calcular_imc(), 2)}")

else:
    st.info("Aún no hay paciente en atención")

# -------------------------
# SALA DE ESPERA
# -------------------------

st.subheader("🪑 Sala de espera")

for p in st.session_state.cola.cola:
    st.write(f"🧑‍⚕️ {p.get__nombre()} — {p.padecimiento}")

# -------------------------
# HISTORIAL
# -------------------------

st.subheader("📋 Atendidos")

st.write(st.session_state.atendidos)
