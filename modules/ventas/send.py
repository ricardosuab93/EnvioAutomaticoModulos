import os
from typing import Optional

from common.mailer import send_email
from common.dates import tomorrow_str

OUTPUT_DIR = os.path.join("outputs", "ventas")

def send_ventas_module(zip_path: Optional[str] = None) -> None:
    report_date = tomorrow_str()

    if zip_path:
        final_zip_path = zip_path
    else:
        zip_filename = f"NORDIGESA {report_date}.zip"
        final_zip_path = os.path.join(OUTPUT_DIR, zip_filename)

    if not os.path.exists(final_zip_path):
        raise FileNotFoundError(f"No se encontró el archivo: {zip_filename}")

    subject = f"MODULO DE VENTAS NORDIGESA {report_date}"
    body = f"Se envía MÓDULO DE VENTAS NORDIGESA del {report_date}"

    send_email(
        subject=subject,
        body=body,
        attachment_path=final_zip_path,
        group="VENTAS",
    )


if __name__ == "__main__":
    send_ventas_module()
    print("Modulo de ventas enviado correctamente")