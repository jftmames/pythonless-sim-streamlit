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
        {
            "highlight": {"line": 3},
            "what": "Se crea una 'referencia' o 'puntero' al documento digital que se va a peritar.",
            "why": "Se trabaja con una ruta al archivo en lugar de manipularlo directamente al principio. Es un principio de orden y buenas prácticas, similar a identificar correctamente un expediente por su número antes de abrirlo.",
            "appData": "En análisis de datos complejos, se definen rutas a los ficheros de origen para que los procesos sean automáticos y no dependan de que alguien arrastre un archivo manualmente.",
            "appLaw": "La trazabilidad es clave en la cadena de custodia. Se debe identificar sin ambigüedad la evidencia. Aquí se referencia el 'cuerpo del delito' digital (el contrato) de forma precisa.",
            "state": {"globals": {"archivo": "Path('data/contrato_demo.pdf')"}}
        },
        {
            "highlight": {"line": 4},
            "what": "Se lee el contenido exacto del archivo, bit a bit, en su forma más pura.",
            "why": "El 'sello' hash debe calcularse sobre el contenido original e inalterado. Cualquier cambio, incluso un espacio o una coma, generaría un sello completamente diferente. Es la base de la integridad de la prueba.",
            "appData": "Para verificar si un conjunto de datos no ha sido corrompido, se compara su huella hash con una huella de referencia. Si coinciden, los datos son idénticos.",
            "appLaw": "La prueba debe ser íntegra. Este paso asegura que estamos 'fotografiando' el contenido exacto del documento en un momento dado, garantizando que lo que se analiza es lo mismo que se presenta en el juicio.",
            "state": {"globals": {"datos": "b'%PDF-1.5...' (contenido simulado)"}}
        },
        {
            "highlight": {"line": 5},
            "what": "Se inicializa la 'máquina de sellado' usando el algoritmo estándar SHA-256.",
            "why": "Se elige un algoritmo criptográfico robusto y no obsoleto. SHA-256 es un estándar de la industria, como elegir una determinada norma ISO para un proceso de calidad.",
            "appData": "Se utiliza para verificar la integridad de descargas de software, en control de versiones de código y para asegurar que los datos no han sido alterados en tránsito.",
            "appLaw": "El uso de algoritmos reconocidos por instituciones como el NIST (Instituto Nacional de Estándares y Tecnología de EE.UU.) refuerza la validez de la pericial. Un juez confiará más en un método estándar que en uno propietario.",
            "state": {"globals": {"h": "<sha256 object>"}}
        },
        {
            "highlight": {"line": 6},
            "what": "Se 'alimenta' la máquina con los bytes del documento para que calcule el sello.",
            "why": "Este es el acto de 'sellar'. La función matemática del hash procesa el contenido y se prepara para generar un resultado único.",
            "appData": "En archivos muy grandes, los datos se pueden 'alimentar' por trozos (chunks), lo que es más eficiente. El resultado final del hash es el mismo.",
            "appLaw": "Este paso vincula inequívocamente el contenido del documento (la prueba) con el futuro sello (el hash). Es el momento en que se crea la conexión probatoria.",
            "state": {"io": {"log": ["h.update(datos) ejecutado"]}}
        },
        {
            "highlight": {"line": 7},
            "what": "Se obtiene la huella digital final en un formato de texto legible (hexadecimal).",
            "why": "El resultado matemático del hash se convierte a texto para poder copiarlo, pegarlo, imprimirlo e incluirlo fácilmente en un informe o acta. Es la 'materialización' del sello digital.",
            "appData": "Esta huella se almacena en catálogos de datos (data catalogs) para identificar unívocamente cada versión de un dataset.",
            "appLaw": "Esta es la huella que se incluirá en el acta pericial y se presentará ante el tribunal. Cualquier persona, en cualquier momento, podrá recalcular el hash del documento original y verificar que coincide con esta huella.",
            "state": {"globals": {"huella": "'9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08' (simulada)"}}
        },
        {
            "highlight": {"line": 8},
            "what": "Se crea un 'acta' estructurada que contiene el sello y el contexto relevante.",
            "why": "Un sello por sí solo no es suficiente. Necesita contexto: ¿quién lo generó? ¿cuándo? Un diccionario es la forma perfecta de estructurar esta información, como las secciones de un contrato.",
            "appData": "Los diccionarios (o JSON) son el formato estándar para intercambiar datos estructurados en la web, por ejemplo, en las respuestas de una API.",
            "appLaw": "Esto es la base de la cadena de custodia digital. El acta no solo contiene la prueba (el hash), sino el metadato esencial (quién, cuándo) que le da validez procesal.",
            "state": {"globals": {"acta": "{'sha256': '...', 'custodio': '...', 'timestamp': '...'}"}}
        },
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
