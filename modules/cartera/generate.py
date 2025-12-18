import csv
import zipfile
import os

from common.db import get_connection
from common.dates import tomorrow_str


OUTPUT_DIR = os.path.join("outputs", "cartera")


def generate_cartera_module() -> str:
    """
    Genera el módulo de CARTERA y retorna el path del ZIP generado.
    La fecha del archivo es SIEMPRE el día siguiente a la ejecución.
    """

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    report_date = tomorrow_str()

    param1 = 0
    param2 = 0
    param3 = 0

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "EXECUTE uspVEN_ListaCarteraClientesAutomatico ?, ?, ?",
        (param1, param2, param3)
    )

    results = cursor.fetchall()

    csv_filename = f"CARTERA_NORDIGESA_{report_date}.csv"
    zip_filename = f"CARTERA_NORDIGESA_{report_date}.zip"

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
    zip_file = generate_cartera_module()
    print(f"Cartera de clientes generada correctamente: {zip_file}")