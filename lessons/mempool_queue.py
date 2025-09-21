lesson = {
    "title": "Mempool: cola de transacciones (simulado)",
    "description": "Visualiza llegada y selección de transacciones sin estructuras complejas.",
    "code": """mempool = []
mempool.append({"id":1,"fee":120})
mempool.append({"id":2,"fee":80})
# prioridad por fee (simulada)
next_tx = mempool.pop(0)
print(next_tx)""",
    "steps": [
        {
            "highlight": {"line": 1},
            "what": "Crea cola vacía.",
            "why": "Acumular transacciones.",
            "appData": "Buffer de eventos.",
            "appLaw": "Orden de llegada afecta al bloque.",
            "state": {"globals": {"mempool": "[]"}}
        },
        {
            "highlight": {"line": 2},
            "what": "Encola tx1.",
            "why": "Registrar pendiente.",
            "appData": "Back-pressure.",
            "appLaw": "Trazabilidad de entrada.",
            "state": {"globals": {"mempool": '[{"id":1,"fee":120}]'}}
        },
        {
            "highlight": {"line": 3},
            "what": "Encola tx2.",
            "why": "—",
            "appData": "—",
            "appLaw": "—",
            "state": {"globals": {"mempool": '[{"id":1,"fee":120}, {"id":2,"fee":80}]'}}
        },
        {
            "highlight": {"line": 5},
            "what": "Selecciona siguiente.",
            "why": "Política de prioridad.",
            "appData": "Scheduling.",
            "appLaw": "Incentivos/minería.",
            "state": {"globals": {"next_tx": '{"id":1,"fee":120}', "mempool": '[{"id":2,"fee":80}]'}}
        },
        {
            "highlight": {"line": 6},
            "what": "Publica elección.",
            "why": "Salida auditada.",
            "appData": "Logs.",
            "appLaw": "Transparencia de mempool.",
            "state": {"io": {"out": ['{"id":1, "fee":120}']}}
        }
    ]
}
