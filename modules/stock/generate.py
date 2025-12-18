import csv
import zipfile
import os

from common.db import get_connection
from common.dates import tomorrow_str


OUTPUT_DIR = os.path.join("outputs", "stock")


def generate_stock_module():
    """
    Genera el módulo de stock y retorna la ruta del ZIP generado
    """

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    report_date = tomorrow_str()

    param1 = 0
    param2 = report_date
    param3 = 1

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "EXECUTE uspALM_ListaModuloStocksAutomatico ?, ?, ?",
        (param1, param2, param3)
    )

    results = cursor.fetchall()

    csv_filename = f"STK NORDIGESA {report_date}.csv"
    zip_filename = f"STK NORDIGESA {report_date}.zip"

    csv_path = os.path.join(OUTPUT_DIR, csv_filename)
    zip_path = os.path.join(OUTPUT_DIR, zip_filename)

    with open(csv_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([col[0] for col in cursor.description])
        writer.writerows(results)

    conn.close()

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(csv_path, arcname=csv_filename)

    os.remove(csv_path)

    return zip_path


if __name__ == "__main__":
    zip_file = generate_stock_module()
    print(f"Modulo de stock generado correctamente: {zip_file}")