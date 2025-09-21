import streamlit as st

# --- Importar Lecciones ---
from lessons.hash_evidence import lesson as hash_lesson
from lessons.pow_nonce import lesson as pow_lesson
from lessons.mempool_queue import lesson as mempool_lesson

# --- Configuración de la Página ---
st.set_page_config(layout="wide", page_title="Simulador Pythonless")

# --- Funciones para "Renderizar" Componentes ---

def render_code_view(code, active_line):
    lines = code.split('\\n')
    formatted_code = ""
    for i, line in enumerate(lines, 1):
        if i == active_line:
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
        st.json(globals_state) if globals_state else st.write("—")
    with col2:
        st.subheader("Pila de llamadas")
        st.write("—")
    with col3:
        st.subheader("IO / Logs")
        st.json(io_state) if io_state else st.write("—")

# --- FUNCIÓN CORREGIDA ---
def render_explain_cards(step):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.info(f"**Qué hace:** {step['what']}") # Sin \\n
    with col2:
        st.success(f"**Por qué importa:** {step['why']}") # Sin \\n
    with col3:
        st.warning(f"**Aplicación en Datos:** {step['appData']}") # Sin \\n
    with col4:
        st.error(f"**Aplicación en Derecho:** {step['appLaw']}") # Sin \\n

# --- Aplicación Principal ---

st.title("Simulador Pythonless (Versión Streamlit)")
st.markdown("Aprende qué hace Python al ejecutar código… **sin ejecutar Python**.")

lessons = {
    "Acta de Evidencia (Hash)": hash_lesson,
    "Prueba de Trabajo (PoW)": pow_lesson,
    "Mempool (Cola de Transacciones)": mempool_lesson,
}

selected_lesson_title = st.selectbox("Selecciona una lección:", list(lessons.keys()))
lesson = lessons[selected_lesson_title]

session_key = f'step_{selected_lesson_title}'
if session_key not in st.session_state:
    st.session_state[session_key] = 0

step_idx = st.session_state[session_key]
current_step_data = lesson["steps"][step_idx]
total_steps = len(lesson["steps"])

st.markdown("---")

nav_cols = st.columns([1, 1, 8])
if nav_cols[0].button("⬅️ Anterior"):
    st.session_state[session_key] = max(0, step_idx - 1)
    st.rerun()

if nav_cols[1].button("Siguiente ➡️"):
    st.session_state[session_key] = min(total_steps - 1, step_idx + 1)
    st.rerun()

nav_cols[2].write(f"**Paso {step_idx + 1} de {total_steps}**")

render_code_view(lesson["code"], current_step_data["highlight"]["line"])
st.markdown("---")
render_explain_cards(current_step_data)
st.markdown("---")
render_state_view(current_step_data.get("state", {}))
