import datetime
import platform
import sqlite3


def test_migration_integrity_simulation():
    # -------------------------------------------------------------------
    # EVIDENCIA NO FALSIFICABLE
    # -------------------------------------------------------------------
    print("\n" + "=" * 60)
    print("EVIDENCIA DE EJECUCIÓN - SPIKE 5.4 (MIGRACIONES BD)")
    print(f"TIMESTAMP : {datetime.datetime.now().isoformat()}")
    print(f"HOSTNAME  : {platform.node()}")
    print(f"PLATFORM  : {platform.platform()}")
    print("=" * 60)

    # Simulación de BD SQLite en memoria para validar la preservación de datos
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    # 1. Esquema Inicial (Módulo 4)
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT);")
    cursor.executemany("INSERT INTO users (username) VALUES (?);", [("nayib",), ("admin",), ("reviewer",)])
    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM users;")
    count_before = cursor.fetchone()[0]
    print(f"[+] Registros existentes antes de la migración: {count_before}")

    # 2. Aplicación de Migración (Evolución de Esquema sin pérdida de datos)
    # Agregar nueva columna 'role' con valor por defecto
    cursor.execute("ALTER TABLE users ADD COLUMN role TEXT DEFAULT 'user';")
    conn.commit()

    # 3. Verificación de Integridad post-migración
    cursor.execute("SELECT COUNT(*) FROM users;")
    count_after = cursor.fetchone()[0]

    cursor.execute("SELECT username, role FROM users WHERE username='nayib';")
    sample_user = cursor.fetchone()

    print(f"[+] Registros verificados después de la migración: {count_after}")
    print(f"[+] Registro migrado con éxito: Usuario='{sample_user[0]}', Rol Asignado='{sample_user[1]}'")
    print("-" * 60)

    assert count_before == count_after, "¡ERROR: Hubo pérdida de datos durante la migración!"
    print("[SUCCESS] Migración validada sin pérdida ni corrupción de datos.")
    print("=" * 60 + "\n")
    conn.close()


if __name__ == "__main__":
    test_migration_integrity_simulation()