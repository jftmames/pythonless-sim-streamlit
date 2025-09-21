import streamlit as st

# --- Importar Lecciones (Asegúrate de haber creado estos archivos) ---
# Nota: Si un archivo no existe, esta línea dará error. Créalos primero.
from lessons.hash_evidence import lesson as hash_lesson
# from lessons.pow_nonce import lesson as pow_lesson
# from lessons.mempool_queue import lesson as mempool_lesson

# --- Configuración de la Página ---
st.set_page_config(layout="wide", page_title="Simulador Pythonless")

# --- Funciones para "Renderizar" Componentes ---

def render_code_view(code, active_line):
    lines = code.split('\\n')
    # Creamos un bloque de código formateado con Markdown
    formatted_code = ""
    for i, line in enumerate(lines, 1):
        if i == active_line:
            # Resalta la línea activa añadiendo un ">" y un color sutil
            formatted_code += f"{i:02d} > {line.strip()}\\n"
        else:
            formatted_code += f"{i:02d}   {line.strip()}\\n"
    st.code(formatted_code, language="python")

def render_state_view(state):
    globals_state = state.get("globals", {})
    io_state = state.get("io", {})

    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Variables")
        if globals_state:
            st.json(globals_state)
        else:
            st.write("—")
    with col2:
        st.subheader("Pila de llamadas")
        st.write("—") # Simplificado por ahora
    with col3:
        st.subheader("IO / Logs")
        if io_state:
            st.json(io_state)
        else:
            st.write("—")

def render_explain_cards(step):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.info(f"**Qué hace:**\\n{step['what']}")
    with col2:
        st.success(f"**Por qué importa:**\\n{step['why']}")
    with col3:
        st.warning(f"**Aplicación en Datos:**\\n{step['appData']}")
    with col4:
        st.error(f"**Aplicación en Derecho:**\\n{step['appLaw']}")

# --- Aplicación Principal ---

st.title("Simulador Pythonless (Versión Streamlit)")
st.markdown("Aprende qué hace Python al ejecutar código… **sin ejecutar Python**.")

# Carga las lecciones que hayas creado
lessons = {
    "Acta de Evidencia (Hash)": hash_lesson,
    # "Prueba de Trabajo (PoW)": pow_lesson,
    # "Mempool (Cola de Transacciones)": mempool_lesson,
}

# Selector para elegir la lección
selected_lesson_title = st.selectbox("Selecciona una lección:", list(lessons.keys()))
lesson = lessons[selected_lesson_title]

# Usamos el estado de la sesión para recordar el paso actual de CADA lección
session_key = f'step_{selected_lesson_title}'
if session_key not in st.session_state:
    st.session_state[session_key] = 0

step_idx = st.session_state[session_key]
current_step_data = lesson["steps"][step_idx]
total_steps = len(lesson["steps"])

st.markdown("---")

# Controles de navegación y contador
nav_cols = st.columns([1, 1, 8])
if nav_cols[0].button("⬅️ Anterior"):
    st.session_state[session_key] = max(0, step_idx - 1)
    st.experimental_rerun() # Recarga la app para reflejar el cambio

if nav_cols[1].button("Siguiente ➡️"):
    st.session_state[session_key] = min(total_steps - 1, step_idx + 1)
    st.experimental_rerun() # Recarga la app para reflejar el cambio

nav_cols[2].write(f"**Paso {step_idx + 1} de {total_steps}**")

# Renderizado de los componentes visuales
render_code_view(lesson["code"], current_step_data["highlight"]["line"])
st.markdown("---")
render_explain_cards(current_step_data)
st.markdown("---")
render_state_view(current_step_data.get("state", {}))
