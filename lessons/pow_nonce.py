lesson = {
    "title": "Prueba de Trabajo: encontrar nonce (simulado)",
    "description": "Visualiza el bucle que busca un hash con prefijo de ceros, sin SHA real.",
    "code": """dificultad = 3
nonce = 0
hash = ""
while not hash.startswith("0"*dificultad):
    nonce += 1
    # hash = sha256(cabecera + str(nonce)).hexdigest()  # simulado
    hash = "0" * (3 if nonce >= 347 else 2) + "abc"     # hack didáctico
print("Bloque minado con nonce", nonce)""",
    "steps": [
        {
            "highlight": {"line": 1},
            "what": "Fija ceros requeridos.",
            "why": "Controla el coste de minado.",
            "appData": "Regula throughput.",
            "appLaw": "Impacta en incentivos y consumo.",
            "state": {"globals": {"dificultad": "3"}}
        },
        {
            "highlight": {"line": 2},
            "what": "Inicia contador.",
            "why": "Parámetro que se prueba.",
            "appData": "Búsqueda incremental.",
            "appLaw": "Evidencia del esfuerzo realizado.",
            "state": {"globals": {"nonce": "0"}}
        },
        {
            "highlight": {"line": 4},
            "what": "Condición de salida.",
            "why": "Repetir hasta cumplir objetivo.",
            "appData": "Búsqueda en espacio grande.",
            "appLaw": "Dificultad = seguridad.",
            "state": {"globals": {"hash": "''"}}
        },
        {
            "highlight": {"line": 5},
            "what": "Prueba siguiente nonce.",
            "why": "Explorar el espacio.",
            "appData": "Iteración.",
            "appLaw": "Implicaciones energéticas.",
            "state": {"globals": {"nonce": "1"}}
        },
        {
            "highlight": {"line": 7},
            "what": "Calcula hash (simulado).",
            "why": "Evalúa objetivo.",
            "appData": "Función de coste.",
            "appLaw": "No repudio del proceso.",
            "state": {"globals": {"hash": "'00abc'"}, "io": {"log": ["hash simulado con 2 ceros"]}}
        },
        {
            "highlight": {"line": 5},
            "what": "Siguiente intento.",
            "why": "Aumenta probabilidad.",
            "appData": "Más intentos.",
            "appLaw": "Coste/beneficio.",
            "state": {"globals": {"nonce": "2"}}
        },
        {
            "highlight": {"line": 7},
            "what": "Vuelve a calcular (simulado).",
            "why": "Evaluar condición.",
            "appData": "Iteración.",
            "appLaw": "—",
            "state": {"globals": {"hash": "'000abc'"}}
        },
        {
            "highlight": {"line": 8},
            "what": "Reporta éxito.",
            "why": "Salida de estado final.",
            "appData": "Telemetría.",
            "appLaw": "Registro para auditoría.",
            "state": {"io": {"out": ["Bloque minado con nonce 347"]}}
        }
    ]
}
