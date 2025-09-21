lesson = {
    "title": "Acta de evidencia: generar huella SHA-256 (simulado)",
    "description": "Paso a paso de lo que hace Python al calcular y registrar una huella, sin ejecutar Python.",
    "code": """import hashlib, json
from pathlib import Path

archivo = Path("data/contrato_demo.pdf")
datos = b"%PDF-..."  # contenido simulado
h = hashlib.sha256()
h.update(datos)
huella = h.hexdigest()
acta = {"sha256": huella, "custodio": "Perito X"}
print(json.dumps(acta))""",
    "steps": [
        {
            "highlight": {"line": 1},
            "what": "Carga las herramientas para hash y para serializar a JSON.",
            "why": "Reutilizas implementaciones probadas; menos errores críticos.",
            "appData": "Checksums reproducibles para control de integridad en datasets.",
            "appLaw": "Uso de librerías estándar aceptadas en peritajes (hash + acta JSON).",
            "state": {"globals": {"hashlib": "<module>", "json": "<module>"}, "stack": []}
        },
        {
            "highlight": {"line": 3},
            "what": "Referencia al documento a custodiar.",
            "why": "Trabajar con objetos ruta ofrece métodos seguros y claros.",
            "appData": "Rutas coherentes en pipelines de datos.",
            "appLaw": "Trazabilidad del documento en el acta.",
            "state": {"globals": {"archivo": "Path('data/contrato_demo.pdf')"}}
        },
        {
            "highlight": {"line": 4},
            "what": "Bytes del contrato (simulados).",
            "why": "El hash opera sobre bytes exactos.",
            "appData": "Reproducibilidad de huellas.",
            "appLaw": "Cualquier cambio de 1 bit altera la huella.",
            "state": {"globals": {"datos": "b'%PDF-...'"}}
        },
        {
            "highlight": {"line": 5},
            "what": "Crea el objeto de hash.",
            "why": "Permite alimentar datos por bloques y luego obtener la huella.",
            "appData": "Procesar ficheros grandes por chunks.",
            "appLaw": "Algoritmo aceptado para integridad probatoria.",
            "state": {"globals": {"h": "<sha256 object>"}}
        },
        {
            "highlight": {"line": 6},
            "what": "Introduce los bytes en el cálculo.",
            "why": "Separar carga de datos y digest facilita auditoría.",
            "appData": "Control de versiones de datos.",
            "appLaw": "Registra qué entrada exacta generó la huella.",
            "state": {"io": {"log": ["update(datos) aplicado"]}}
        },
        {
            "highlight": {"line": 7},
            "what": "Obtiene la huella en hex.",
            "why": "Formato portable y legible.",
            "appData": "Se usa en catálogos de datos.",
            "appLaw": "Se incluye en el acta para verificación.",
            "state": {"globals": {"huella": "'9f2a…' (simulada)"}}
        },
        {
            "highlight": {"line": 8},
            "what": "Construye el registro probatorio.",
            "why": "Estructurar datos evita ambigüedades.",
            "appData": "Diccionarios → registros claros.",
            "appLaw": "Base de la cadena de custodia.",
            "state": {"globals": {"acta": "{ 'sha256': '9f2a…', 'custodio': 'Perito X' }"}}
        },
        {
            "highlight": {"line": 9},
            "what": "Serializa el acta a JSON.",
            "why": "Formato interoperable para archivar/compartir.",
            "appData": "APIs y data lakes.",
            "appLaw": "Adjuntar al expediente y verificar en juicio.",
            "state": {"io": {"out": ['{"sha256": "9f2a…", "custodio": "Perito X"}']}} # <-- LÍNEA CORREGIDA
        }
    ]
}
