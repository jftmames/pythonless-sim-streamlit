# Copia y pega el contenido completo de la versión corregida de este archivo que te proporcioné anteriormente.
# Asegúrate de que cada 'step' dentro de la lista 'steps' tenga su correspondiente clave "state".
lesson = {
    "title": "Acta de Evidencia Digital: La Huella Hash",
    "description": "Este laboratorio simula cómo un perito informático genera un 'sello digital' (hash) para un documento, garantizando su integridad y creando una prueba admisible en un proceso judicial.",
    "code": """import hashlib, json
from pathlib import Path

archivo = Path("data/contrato_demo.pdf")
datos = archivo.read_bytes()  # Se leen los bytes reales del fichero
h = hashlib.sha256()
h.update(datos)
huella = h.hexdigest()
acta = {"sha256": huella, "custodio": "Perito Judicial X", "timestamp": "2025-09-22T10:30:00Z"}
print(json.dumps(acta))""",
    "steps": [
        {
            "highlight": {"line": 1},
            "what": "Importar 'bibliotecas' o 'códigos de leyes' para criptografía y formato de datos.",
            "why": "En lugar de inventar un método propio (lo que sería imprudente y difícil de defender), se utilizan herramientas estándar, auditadas y universalmente aceptadas. Es el equivalente a citar el Código Civil en lugar de una ley inventada.",
            "appData": "En ciencia de datos, usar librerías probadas como 'pandas' o 'numpy' garantiza que los cálculos son correctos y reproducibles por otros investigadores.",
            "appLaw": "Un perito debe fundamentar su dictamen en estándares reconocidos. Usar 'hashlib' (para el hash) y 'json' (para el acta) es una práctica aceptada que dota de rigor técnico y credibilidad a la prueba digital.",
            "state": {"globals": {"hashlib": "<module>", "json": "<module>"}}
        },
        # ... y así para todos los demás pasos ...
        {
            "highlight": {"line": 9},
            "what": "Se convierte el acta a formato JSON, un estándar universal para documentos de texto.",
            "why": "JSON es el 'PDF' de los datos. Es un formato de texto plano, legible por humanos y máquinas, que garantiza la interoperabilidad. Un sistema judicial en España podrá leer un JSON generado en EE.UU. sin problemas.",
            "appData": "Es el lenguaje universal de las APIs y los data lakes. Permite que sistemas diferentes se comuniquen de forma fiable.",
            "appLaw": "El acta en formato JSON puede ser fácilmente adjuntada a un expediente electrónico, enviada por correo seguro (LexNET) y verificada en sede judicial sin necesidad de software especializado. Garantiza la portabilidad y accesibilidad de la prueba.",
            "state": {"io": {"out": ['{"sha256": "...", "custodio": "...", "timestamp": "..."}']}}
        }
    ]
}
