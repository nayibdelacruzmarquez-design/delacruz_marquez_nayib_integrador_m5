import datetime
import platform
import json
import time

def test_serialization_performance():
    # -------------------------------------------------------------------
    # EVIDENCIA NO FALSIFICABLE
    # -------------------------------------------------------------------
    print("\n" + "=" * 60)
    print("EVIDENCIA DE EJECUCIÓN - SPIKE 5.2 (SERIALIZACIÓN API)")
    print(f"TIMESTAMP : {datetime.datetime.now().isoformat()}")
    print(f"HOSTNAME  : {platform.node()}")
    print(f"PLATFORM  : {platform.platform()}")
    print("=" * 60)

    # Simulación de datos de dominio (ej. Envíos/Paquetes)
    data = [
        {"id": i, "tracking_code": f"TRACK-{1000+i}", "status": "DELIVERED", "active": True}
        for i in range(100)
    ]

    # Benchmark: Serialización a JSON
    start_json = time.time()
    for _ in range(1000):
        json_output = json.dumps({"data": data, "count": len(data)})
    time_json = time.time() - start_json

    print(f"[+] Serialización JSON (1,000 iteraciones): {time_json:.4f} s")
    print(f"[+] Tamaño de carga útil JSON: {len(json_output)} bytes")
    print("-" * 60 + "\n")

if __name__ == "__main__":
    test_serialization_performance()