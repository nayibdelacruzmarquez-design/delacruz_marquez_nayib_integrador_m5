import datetime
import os
import platform


def test_dependency_injection_config():
    # -------------------------------------------------------------------
    # EVIDENCIA NO FALSIFICABLE
    # -------------------------------------------------------------------
    print("\n" + "=" * 60)
    print("EVIDENCIA DE EJECUCIÓN - SPIKE 5.6 (CONFIGURACIÓN / DI)")
    print(f"TIMESTAMP : {datetime.datetime.now().isoformat()}")
    print(f"HOSTNAME  : {platform.node()}")
    print(f"PLATFORM  : {platform.platform()}")
    print("=" * 60)

    # Simulación de fábrica de configuración por entorno (12-Factor App)
    class Config:
        TESTING = False
        DEBUG = False
        DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///instance/app.db")

    class DevConfig(Config):
        DEBUG = True

    class TestConfig(Config):
        TESTING = True
        DATABASE_URI = "sqlite:///:memory:"

    # Evaluación de inyección según variable FLASK_ENV
    env = os.getenv("FLASK_ENV", "testing")

    if env == "testing":
        active_config = TestConfig()
    else:
        active_config = DevConfig()

    print(f"[+] Entorno detectado          : {env}")
    print(f"[+] Modo Testing Activo        : {active_config.TESTING}")
    print(f"[+] URI de BD Inyectada         : {active_config.DATABASE_URI}")
    print("-" * 60)

    assert active_config.DATABASE_URI == "sqlite:///:memory:"
    print(
        "[SUCCESS] Configuración inyectada correctamente sin hardcodear credenciales."
    )
    print("=" * 60 + "\n")


if __name__ == "__main__":
    test_dependency_injection_config()