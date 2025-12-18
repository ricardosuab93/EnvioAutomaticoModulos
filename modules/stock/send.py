import os
from typing import Optional

from common.mailer import send_email
from common.dates import tomorrow_str


OUTPUT_DIR = os.path.join("outputs", "stock")


def send_stock_module(zip_path: Optional[str] = None) -> None:
    """
    Envía el módulo de stock por correo.
    """

    report_date = tomorrow_str()

    final_zip_path: str

    if zip_path is not None:
        final_zip_path = zip_path
    else:
        zip_filename = f"STK NORDIGESA {report_date}.zip"
        final_zip_path = os.path.join(OUTPUT_DIR, zip_filename)

    if not os.path.exists(final_zip_path):
        raise FileNotFoundError(f"No se encontró el archivo: {final_zip_path}")

    subject = f"MODULO DE STOCK NORDIGESA {report_date}"
    body = f"Se envía MÓDULO DE STOCK NORDIGESA del {report_date}"

    send_email(
        subject=subject,
        body=body,
        attachment_path=final_zip_path,
        group="STOCK",
    )


if __name__ == "__main__":
    send_stock_module()
    print("Modulo de stock enviado correctamente")