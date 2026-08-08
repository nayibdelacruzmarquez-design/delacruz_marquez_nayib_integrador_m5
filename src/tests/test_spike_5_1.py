import datetime
import platform
import time
import concurrent.futures
import requests


def test_benchmark_execution():
    # -------------------------------------------------------------------
    # EVIDENCIA NO FALSIFICABLE (Timestamp + Hostname + Platform)
    # -------------------------------------------------------------------
    print("\n" + "=" * 60)
    print("EVIDENCIA DE EJECUCIÓN - SPIKE 5.1")
    print(f"TIMESTAMP : {datetime.datetime.now().isoformat()}")
    print(f"HOSTNAME  : {platform.node()}")
    print(f"PLATFORM  : {platform.platform()}")
    print("=" * 60)

    # URL local del servidor en ejecución
    BASE_URL = "http://127.0.0.1:5000"

    def make_request(req_id):
        start = time.time()
        try:
            res = requests.get(BASE_URL, timeout=5)
            return req_id, res.status_code, time.time() - start
        except Exception:
            return req_id, None, time.time() - start

    concurrent_requests = 10
    print(f"\n[+] Ejecutando {concurrent_requests} peticiones concurrentes a {BASE_URL}...")

    start_total = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrent_requests) as executor:
        futures = [executor.submit(make_request, i) for i in range(concurrent_requests)]
        results = [f.result() for f in concurrent.futures.as_completed(futures)]
    total_time = time.time() - start_total

    latencies = [r[2] for r in results]
    avg_latency = sum(latencies) / len(latencies)
    success_count = sum(1 for r in results if r[1] == 200)

    print("-" * 60)
    print(f"Peticiones exitosas (HTTP 200) : {success_count}/{concurrent_requests}")
    print(f"Tiempo total de ráfaga         : {total_time:.4f} s")
    print(f"Latencia promedio              : {avg_latency:.4f} s")
    print(f"Throughput estimado            : {concurrent_requests / total_time:.2f} req/s")
    print("-" * 60 + "\n")


if __name__ == "__main__":
    test_benchmark_execution()