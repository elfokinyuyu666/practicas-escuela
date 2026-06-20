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

col1, col2 = st.columns(2)

with col1:
    if st.button("▶️ Iniciar simulación"):
        st.session_state.simulacion = True

with col2:
    if st.button("🔄 Reiniciar simulación"):
        st.session_state.cola = inicializar()
        st.session_state.atendidos = []
        st.session_state.actual = None
        st.session_state.simulacion = False
        st.session_state.last_time = time.time()
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

st.divider()

col1, col2, col3 = st.columns(3)

col1.metric("⏳ En espera", len(st.session_state.cola.cola))
col2.metric("✅ Atendidos", len(st.session_state.atendidos))

consultorio = "-"
if st.session_state.actual:
    consultorio = st.session_state.actual.medico.consultorio

col3.metric("🏥 Consultorio", consultorio)


# -------------------------
# PACIENTE ACTUAL (MEJORADO VISUALMENTE)
# -------------------------

st.subheader("👨‍⚕️ Paciente en atención")

if st.session_state.actual:

    p = st.session_state.actual
    imc = p.calcular_imc()

    st.markdown(
        f"""
        <div style="
            background: linear-gradient(135deg, #0f172a, #1e293b);
            padding: 25px;
            border-radius: 18px;
            border-left: 6px solid #3b82f6;
            color: white;
            box-shadow: 0px 6px 18px rgba(0,0,0,0.4);
        ">

            <h2 style="margin:0; color:#60a5fa;">
                🧑‍⚕️ {p.get__nombre()}
            </h2>

            <hr style="border: 0.5px solid #334155;">

            <p>🦠 <b>Padecimiento:</b> {p.padecimiento}</p>
            <p>👨‍⚕️ <b>Médico:</b> {p.medico.get__nombre()}</p>
            <p>🏥 <b>Consultorio:</b> {p.medico.consultorio}</p>

            <div style="margin-top:10px;">
                📞 <b>Teléfono:</b> {p.get__telefono()}<br>
                📧 <b>Correo:</b> {p.get__correo()}<br>
                ⚖️ <b>Peso:</b> {p.peso} kg<br>
                📏 <b>Altura:</b> {p.altura} m
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.success(f"📊 IMC: {round(imc, 2)}")

    if imc > 30:
        st.error("⚠️ IMC alto (obesidad)")
    elif imc > 25:
        st.warning("⚠️ Sobrepeso")

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
