lesson = {
    "title": "Mempool: El Registro de Entrada de Transacciones",
    "description": "Simulación de la 'sala de espera' (mempool) donde las transacciones aguardan antes de ser incluidas en un bloque. Veremos cómo se gestiona esta cola y cómo se priorizan unas sobre otras.",
    "code": """# Las transacciones llegan y se añaden a una lista de espera
mempool = []

# Llega una transacción con una comisión (fee) alta
mempool.append({"id": "TX_001", "fee": 150})

# Llega otra con una comisión baja
mempool.append({"id": "TX_002", "fee": 20})

# El minero ordena la cola para maximizar su beneficio
mempool.sort(key=lambda tx: tx["fee"], reverse=True)

# El minero elige la transacción con la comisión más alta
next_tx = mempool.pop(0)

print(f"Procesando transacción prioritaria: {next_tx}")""",
    "steps": [
        {
            "highlight": {"line": 2},
            "what": "Se crea el 'mempool', una lista vacía para almacenar las transacciones pendientes.",
            "why": "Es el contenedor o 'buffer' donde se acumulan las operaciones que la red ha recibido pero que aún no ha confirmado. Sin esta 'sala de espera', las transacciones se perderían.",
            "appData": "En sistemas de streaming de datos, se usan colas (como Kafka o RabbitMQ) para gestionar picos de eventos y asegurar que no se pierda información.",
            "appLaw": "Esto es análogo al 'libro de asientos' o 'registro de entrada' de un registro público. Las peticiones se reciben y se anotan, quedando pendientes de calificación y registro definitivo.",
            "state": {"globals": {"mempool": "[]"}}
        },
        {
            "highlight": {"line": 5},
            "what": "Llega una nueva transacción (urgente) y se añade a la lista de espera.",
            "why": "Este es el acto de registrar una solicitud. La transacción es ahora visible para toda la red y está a la espera de ser procesada por un minero.",
            "appData": "Es una operación de 'push' a una cola de eventos. El sistema productor añade un nuevo mensaje para que sea consumido.",
            "appLaw": "Equivale al 'asiento de presentación' en el Registro de la Propiedad. La transacción ha entrado en el sistema y ha ganado una prioridad temporal basada en su momento de llegada.",
            "state": {"globals": {"mempool": '[{"id": "TX_001", "fee": 150}]'}}
        },
        {
            "highlight": {"line": 8},
            "what": "Llega una segunda transacción, esta vez con una comisión mucho más baja (no urgente).",
            "why": "El mempool contiene transacciones con diferentes características. Las comisiones ('fees') son un incentivo económico para que los mineros las incluyan en un bloque.",
            "appData": "Los eventos en una cola pueden tener diferentes prioridades. Un sistema de procesamiento elegirá primero los de alta prioridad.",
            "appLaw": "No todas las solicitudes tienen la misma urgencia o importancia. En un sistema judicial, un auto de medidas cautelares tiene prioridad sobre un trámite ordinario. Aquí, la comisión funciona como un pago por 'tramitación urgente'.",
            "state": {"globals": {"mempool": '[{"id": "TX_001", "fee": 150}, {"id": "TX_002", "fee": 20}]'}}
        },
        {
            "highlight": {"line": 11},
            "what": "El minero, actuando por propio interés económico, ordena la lista de espera de mayor a menor comisión.",
            "why": "A diferencia de una cola simple ('primero en llegar, primero en salir'), el mempool es un mercado. Los mineros tienen libertad para elegir qué transacciones procesan, y lógicamente eligen las que mejor les pagan.",
            "appData": "Esto es un 'priority queue'. En lugar de procesar en orden de llegada (FIFO), se procesa según un criterio de prioridad, en este caso, el campo 'fee'.",
            "appLaw": "Este es un punto clave que rompe con la idea de neutralidad. El protocolo permite una discriminación por precio. Esto tiene implicaciones legales sobre el acceso equitativo a la red y posibles abusos de posición dominante por parte de los mineros.",
            "state": {"globals": {"mempool": '[{"id": "TX_001", "fee": 150}, {"id": "TX_002", "fee": 20}]'}, "io": {"log": ["Mempool ordenado por 'fee'"]}}
        },
        {
            "highlight": {"line": 14},
            "what": "El minero selecciona y retira la transacción con la comisión más alta para incluirla en su bloque.",
            "why": "Este es el acto de 'selección'. El minero construye un nuevo bloque (el equivalente a una nueva página del libro de registro) y elige las 'inscripciones' más rentables para incluir.",
            "appData": "Es una operación 'pop' de una cola de prioridad. Se extrae el elemento más importante para su procesamiento inmediato.",
            "appLaw": "Es el momento de la 'calificación y registro'. El minero, actuando como un 'registrador' descentralizado, formaliza la transacción. Una vez incluida en un bloque y añadida a la cadena, la transacción se considera confirmada e inmutable.",
            "state": {"globals": {"mempool": '[{"id": "TX_002", "fee": 20}]', "next_tx": '{"id": "TX_001", "fee": 150}'}}
        },
        {
            "highlight": {"line": 16},
            "what": "Se anuncia la transacción que ha sido procesada.",
            "why": "La inclusión de la transacción en un bloque es un evento público. Esto sirve para informar al remitente y al destinatario de que la operación ha sido confirmada.",
            "appData": "Es la generación de un 'log' o registro de auditoría que confirma que un evento ha sido procesado con éxito por el sistema.",
            "appLaw": "Es el principio de publicidad registral. El acto de inclusión en el bloque se publica en toda la red, otorgando efectos 'erga omnes' a la transacción dentro del ecosistema de la blockchain.",
            "state": {"io": {"out": ["Procesando transacción prioritaria: {'id': 'TX_001', 'fee': 150}"]}}
        }
    ]
}
