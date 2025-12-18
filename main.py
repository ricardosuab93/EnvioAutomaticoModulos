import traceback

from modules.ventas.generate import generate_ventas_module
from modules.ventas.send import send_ventas_module

from modules.stock.generate import generate_stock_module
from modules.stock.send import send_stock_module

from modules.cartera.generate import generate_cartera_module
from modules.cartera.send import send_cartera_module

def run_step(name: str, func):
    """
    Ejecuta un paso del proceso con manejo de errores.
    """
    print(f"\n▶ Iniciando: {name}")

    try:
        result = func()
        print(f"✔ Finalizado: {name}")
        return result
    except Exception as e:
        print(f"❌ Error en {name}: {e}")
        traceback.print_exc()
        return None


def main():
    print("======================================")
    print("   EJECUCIÓN DIARIA MODULOS NORDIGESA   ")
    print("======================================")

    ventas_zip = run_step(
        "Generación módulo VENTAS",
        generate_ventas_module
    )

    if ventas_zip:
        run_step(
            "Envío módulo VENTAS",
            lambda: send_ventas_module(ventas_zip)
        )

    stock_zip = run_step(
        "Generación módulo STOCK",
        generate_stock_module
    )

    if stock_zip:
        run_step(
            "Envío módulo STOCK",
            lambda: send_stock_module(stock_zip)
        )

    cartera_zip = run_step(
        "Generación módulo CARTERA",
        generate_cartera_module
    )

    if cartera_zip:
        run_step(
            "Envío módulo CARTERA",
            lambda: send_cartera_module(cartera_zip)
        )

    print("\n✅ Proceso diario finalizado.")


if __name__ == "__main__":
    main()