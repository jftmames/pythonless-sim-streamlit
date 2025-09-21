lesson = {
    "title": "Prueba de Trabajo (PoW): El Esfuerzo Demostrable",
    "description": "Simulación del proceso de 'minería' de criptomonedas. Veremos cómo un ordenador debe realizar un trabajo costoso (probar números al azar) para encontrar una 'solución' que es fácil de verificar, un principio clave para la seguridad de la red.",
    "code": """dificultad = 4
nonce = 0
hash_resultado = ""
while not hash_resultado.startswith("0" * dificultad):
    nonce += 1
    # En la realidad, aquí se calcularía un hash complejo
    # Nosotros lo simulamos para que sea más visual
    hash_resultado = "123" # Simula un hash incorrecto
    if nonce == 8500:
        hash_resultado = "0000_solucion_encontrada" # Simula el éxito

print(f"¡Solución encontrada! Nonce: {nonce}, Hash: {hash_resultado}")""",
    "steps": [
        {
            "highlight": {"line": 1},
            "what": "Se establece la 'dificultad' del puzzle a resolver.",
            "why": "Este número define lo costoso que será el trabajo. A mayor dificultad, más tiempo y energía se necesitarán. Es el mecanismo que tiene la red para auto-regularse.",
            "appData": "En machine learning, sería como ajustar un 'hiperparámetro' para hacer que un modelo entrene durante más o menos tiempo, buscando un equilibrio entre coste y precisión.",
            "appLaw": "La dificultad es un acto de política de red con consecuencias económicas y legales. Un aumento de la dificultad implica mayor consumo energético, lo que puede tener implicaciones regulatorias medioambientales (ej. debate sobre la minería de Bitcoin)."
        },
        {
            "highlight": {"line": 2},
            "what": "Se inicializa el 'nonce' (number once), el número que se irá probando.",
            "why": "Este es el único número que el 'minero' puede cambiar en cada intento para tratar de resolver el puzzle. Es como comprar billetes de lotería cambiando solo un número cada vez hasta que uno resulta premiado.",
            "appData": "Es una búsqueda por fuerza bruta en un espacio de soluciones. Se prueba una opción, se evalúa, se descarta y se prueba la siguiente.",
            "appLaw": "El 'nonce' final es la prueba irrefutable del esfuerzo realizado. Demuestra que el minero ha gastado tiempo y recursos, lo que le da derecho a una recompensa y legitima el bloque que ha validado."
        },
        {
            "highlight": {"line": 4},
            "what": "Se define la condición del trabajo: 'sigue intentándolo hasta que encuentres un hash que empiece por X ceros'.",
            "why": "Este es el núcleo de la Prueba de Trabajo. El bucle `while` representa el esfuerzo continuo. La condición de salida (`startswith`) es el objetivo a cumplir, que es difícil de alcanzar pero trivial de verificar.",
            "appData": "Es un bucle de optimización: iterar continuamente hasta que una métrica (en este caso, el prefijo del hash) cumpla un umbral deseado.",
            "appLaw": "Esta condición establece las 'reglas del juego' para la validación. Quien cumple esta regla, tiene derecho a añadir el siguiente bloque a la cadena. Es un mecanismo de consenso basado en reglas computacionales, no en la confianza de un tercero."
        },
        {
            "highlight": {"line": 5},
            "what": "Se incrementa el 'nonce' en uno para probar un nuevo número.",
            "why": "Cada incremento es un intento, un 'billete de lotería' nuevo. Representa un ciclo de cómputo y un gasto de energía. Millones de estos intentos ocurren cada segundo en la red Bitcoin.",
            "appData": "Es una simple iteración, el paso fundamental en cualquier proceso de búsqueda o bucle.",
            "appLaw": "El coste acumulado de estos incrementos es lo que disuade a los atacantes. Falsear la cadena de bloques requeriría realizar todo este trabajo de nuevo para cada bloque, lo que es económicamente inviable. La seguridad se basa en el coste."
        },
        {
            "highlight": {"line": 9},
            "what": "En nuestro intento número 8500, simulamos que hemos encontrado la solución.",
            "why": "Simulamos el momento de '¡Eureka!'. El hash generado finalmente cumple la condición de empezar con cuatro ceros. En la realidad, esto es un evento puramente aleatorio.",
            "appData": "En una simulación de Montecarlo, este sería el momento en que una de las miles de iteraciones aleatorias finalmente produce el resultado buscado.",
            "appLaw": "El hallazgo de este hash es un hecho generador de derechos: el derecho a proponer el nuevo bloque y a recibir la recompensa. Es un nexo causal entre el trabajo realizado (gasto energético) y el resultado obtenido (validación)."
        },
        {
            "highlight": {"line": 12},
            "what": "Se anuncia públicamente la solución encontrada.",
            "why": "Una vez encontrada la solución, el minero la comunica al resto de la red. Los demás nodos pueden verificarla instantáneamente (es muy fácil comprobar que un hash empieza por ceros) y, si es correcta, aceptan el nuevo bloque.",
            "appData": "Es la publicación de los resultados de un experimento para que otros puedan validarlo y reproducirlo (peer review).",
            "appLaw": "Es el acto de publicidad que perfecciona el proceso. La validez del bloque no depende de la autoridad del minero, sino de la verificación pública por parte de la comunidad de la red, de acuerdo con las reglas del protocolo. Es un sistema de validación sin confianza."
        }
    ]
}
