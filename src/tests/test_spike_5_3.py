import datetime
import platform
import time
import json
from flask import Flask, render_template_string


def test_rendering_vs_api_performance():
    # -------------------------------------------------------------------
    # EVIDENCIA NO FALSIFICABLE (Requisito Obligatorio)
    # -------------------------------------------------------------------
    print("\n" + "=" * 60)
    print("EVIDENCIA DE EJECUCIÓN - SPIKE 5.3 (FRONT/BACK BOUNDARY)")
    print(f"TIMESTAMP : {datetime.datetime.now().isoformat()}")
    print(f"HOSTNAME  : {platform.node()}")
    print(f"PLATFORM  : {platform.platform()}")
    print("=" * 60)

    # Dataset de prueba (envíos / paquetes simulados)
    shipments = [
        {"id": i, "tracking": f"TRK-{10000 + i}", "origin": "MX", "destination": "US", "status": "IN_TRANSIT"}
        for i in range(200)
    ]

    # 1. Simulación Server-Side Rendering (SSR) con Jinja2
    app = Flask(__name__)
    template_str = """
    <html>
      <body>
        <h1>Lista de Envíos</h1>
        <ul>
        {% for s in shipments %}
          <li>{{ s.tracking }}: {{ s.origin }} -> {{ s.destination }} [{{ s.status }}]</li>
        {% endfor %}
        </ul>
      </body>
    </html>
    """

    start_ssr = time.time()
    with app.app_context():
        for _ in range(500):
            html_output = render_template_string(template_str, shipments=shipments)
    time_ssr = time.time() - start_ssr

    # 2. Simulación API REST (JSON Response Payload)
    start_api = time.time()
    for _ in range(500):
        json_output = json.dumps({"shipments": shipments, "count": len(shipments)})
    time_api = time.time() - start_api

    print(f"[+] Tiempo de renderizado SSR (Jinja2 HTML - 500 ops) : {time_ssr:.4f} s")
    print(f"[+] Tamaño de la respuesta HTML (SSR)                  : {len(html_output)} bytes")
    print("-" * 60)
    print(f"[+] Tiempo de generación API (JSON Payload - 500 ops)   : {time_api:.4f} s")
    print(f"[+] Tamaño del Payload JSON (API)                      : {len(json_output)} bytes")
    print("-" * 60)
    print(f"[=>] Reducción de overhead de CPU en Backend          : {((time_ssr - time_api) / time_ssr) * 100:.2f}%")
    print(
        f"[=>] Reducción de ancho de banda por petición         : {((len(html_output) - len(json_output)) / len(html_output)) * 100:.2f}%")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    test_rendering_vs_api_performance()