# ADR 5.5: Estrategia de Carga de Relaciones en el ORM y Prevención del Problema N+1

* **Contexto:** Al consultar listados de envíos y sus entidades asociadas (usuarios/roles), la implementación básica mediante el ORM ejecuta una consulta adicional por cada registro iterado, saturando las conexiones de la base de datos.
* **Alternativas:** 
  1. Carga diferida predeterminada (Lazy Loading) iterando objetos en bucles imperativos.
  2. Eager Loading mediante JOINs explícitos (`joinedload` / `selectinload`) o mapeo indexado en memoria.
  3. Ejecución de consultas SQL nativas sin capa de abstracción ORM.
* **Criterio de Selección:** Reducir drásticamente la latencia de respuesta y el conteo de consultas dirigidas al motor SQL manteniendo las ventajas de abstracción del ORM.
* **Evidencia Empírica:** La prueba comparativa (`src/tests/test_spike_5_5.py`) confirmó la eliminación de más de 1,000 consultas innecesarias mediante precarga eficiente de datos, reduciendo el overhead de ejecución.
* **Decisión:** Adoptar estrategias de Eager Loading y mapeos optimizados en todas las consultas de la API que involucren colecciones o relaciones entre tablas.
* **Consecuencias Positivas:** Disminución sustancial de los tiempos de respuesta del servidor en endpoints de listado y menor saturación del pool de conexiones SQL.
* **Consecuencias Negativas / Riesgos:** Incremento en la huella de memoria RAM al traer registros vinculados en una sola transacción y mayor cuidado al construir filtros complejos.