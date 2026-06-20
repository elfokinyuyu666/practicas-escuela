import streamlit as st
import random
import time

from medico import Medico
from paciente import Paciente
from cola import ColaConsultorio

st.set_page_config(page_title="Consultorio", page_icon="🏥", layout="wide")

st.title("🏥 Simulación de Consultorio Médico")

# -------------------------
# FUNCION DE INICIALIZACION
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
# PACIENTE EN ATENCIÓN (CORREGIDO SIN HTML)
# -------------------------

st.subheader("👨‍⚕️ Paciente en atención")

if st.session_state.actual:

    p = st.session_state.actual
    imc = p.calcular_imc()

    colA, colB = st.columns([1, 2])

    with colA:
        st.markdown("### 🧑‍⚕️ Datos del paciente")
        st.markdown(f"**Nombre:** {p.get__nombre()}")
        st.markdown(f"**Edad:** {p.get__edad()}")
        st.markdown(f"**Sexo:** {p.get__sexo()}")

        st.metric("📊 IMC", round(imc, 2))

        if imc > 30:
            st.error("⚠️ Obesidad")
        elif imc > 25:
            st.warning("⚠️ Sobrepeso")
        else:
            st.success("✔ Normal")

    with colB:
        st.markdown("### 🏥 Información médica")
        st.markdown(f"**Padecimiento:** {p.padecimiento}")
        st.markdown(f"**Médico:** {p.medico.get__nombre()}")
        st.markdown(f"**Especialidad:** {p.medico.especialidad}")
        st.markdown(f"**Consultorio:** {p.medico.consultorio}")

        st.markdown("### 📞 Contacto")
        st.markdown(f"- Tel: {p.get__telefono()}")
        st.markdown(f"- Correo: {p.get__correo()}")

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
