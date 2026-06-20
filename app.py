import streamlit as st
from streamlit_autorefresh import st_autorefresh
import random
import pandas as pd

from Clase_paciente import Paciente
from Clase_medico import Medico

st.set_page_config(
    page_title="Consultorio Médico",
    page_icon="🏥",
    layout="wide"
)

# Actualizar cada 5 segundos
contador = st_autorefresh(interval=5000, key="consultorio")

st.title("🏥 Sistema de Atención Médica")

# ==========================
# Inicializar datos
# ==========================

if "iniciado" not in st.session_state:

    medico1 = Medico(
        "Dr. Carlos Hernandez",
        45,
        "Masculino",
        "3323675090",
        "hernandez@tusalud.com",
        "Medicina General",
        "Consultorio 1",
        "M001"
    )

    medico2 = Medico(
        "Dra. Ana Lopez",
        38,
        "Femenino",
        "3340756321",
        "anitalopez@hospital.com",
        "Pediatría",
        "Consultorio 2",
        "M002"
    )

    medico3 = Medico(
        "Dr. Pedro Hernandez",
        50,
        "Masculino",
        "3315233297",
        "pedrinhernandez@tusalud.com",
        "Cardiología",
        "Consultorio 3",
        "M003"
    )

    medicos = [medico1, medico2, medico3]

    pacientes = [

        Paciente(
            "Jonathan Gutierrez",
            25,
            "Masculino",
            "3311411497",
            "jona060@gmail.com",
            80,
            1.75,
            "Gripe"
        ),

        Paciente(
            "Christian Casas",
            20,
            "Masculino",
            "3355555555",
            "christian@gmail.com",
            60,
            1.65,
            "Migraña"
        ),

        Paciente(
            "Alexis Pimentel",
            32,
            "Masculino",
            "3366666666",
            "alexis@gmail.com",
            90,
            1.80,
            "Dolor muscular"
        )
    ]

    for paciente in pacientes:
        paciente.medico = random.choice(medicos)

    st.session_state.cola = pacientes
    st.session_state.atendidos = []
    st.session_state.paciente_actual = None
    st.session_state.iniciado = True

# ==========================
# Atención automática
# ==========================

if len(st.session_state.cola) > 0:

    paciente = st.session_state.cola.pop(0)

    st.session_state.paciente_actual = paciente

    st.session_state.atendidos.append(
        paciente.get__nombre()
    )

# ==========================
# Indicadores
# ==========================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Pacientes en espera",
        len(st.session_state.cola)
    )

with col2:
    st.metric(
        "Pacientes atendidos",
        len(st.session_state.atendidos)
    )

with col3:
    if st.session_state.paciente_actual:
        st.metric(
            "Consultorio",
            st.session_state.paciente_actual.medico.consultorio
        )

# ==========================
# Paciente actual
# ==========================

st.subheader("👨‍⚕️ Paciente en Atención")

if st.session_state.paciente_actual:

    paciente = st.session_state.paciente_actual

    c1, c2 = st.columns(2)

    with c1:

        st.info(
            f"""
            Nombre: {paciente.get__nombre()}

            Edad: {paciente.get__edad()}

            Padecimiento: {paciente.padecimiento}
            """
        )

    with c2:

        st.success(
            f"""
            Médico: {paciente.medico.get__nombre()}

            Especialidad: {paciente.medico.especialidad}

            {paciente.medico.consultorio}
            """
        )

        st.metric(
            "IMC",
            round(
                paciente.calcular_imc(),
                2
            )
        )

# ==========================
# Sala de espera
# ==========================

st.subheader("🪑 Sala de Espera")

if len(st.session_state.cola) > 0:

    datos = []

    for paciente in st.session_state.cola:

        datos.append({
            "Paciente": paciente.get__nombre(),
            "Padecimiento": paciente.padecimiento,
            "Médico": paciente.medico.get__nombre()
        })

    st.dataframe(
        pd.DataFrame(datos),
        use_container_width=True
    )

else:

    st.success(
        "Todos los pacientes fueron atendidos."
    )

# ==========================
# Historial
# ==========================

st.subheader("✅ Historial de Atención")

st.write(st.session_state.atendidos)
