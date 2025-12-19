import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv

load_dotenv()

# Grupos de destinatarios
RECIPIENT_GROUPS = {
    "VENTAS": [
        "fredy.quispe@pe.nestle.com",
        "William.Soto@pe.nestle.com",
        "miguel.sanchez1@pe.nestle.com",
        "lcabanillasc@nordigesa.com",
        "fernando.valderrama@pe.nestle.com",
        "rsuarezb@nordigesa.com",
    ],
    "STOCK": [
        "Ingrid.Egoavil@pe.nestle.com",
        "fredy.quispe@pe.nestle.com",
        "William.Soto@pe.nestle.com",
        "miguel.sanchez1@pe.nestle.com",
        "lcabanillasc@nordigesa.com",
        "fernando.valderrama@pe.nestle.com",
        "rsuarezb@nordigesa.com",
    ],
    "CARTERA": [
        "fredy.quispe@pe.nestle.com",
        "William.Soto@pe.nestle.com",
        "miguel.sanchez1@pe.nestle.com",
        "lcabanillasc@nordigesa.com",
        "rsuarezb@nordigesa.com",
    ],
    "PRUEBA": [
        "lcabanillasc@nordigesa.com",
        "rsuarezb@nordigesa.com",
        "rsuarez.briones@gmail.com"
    ],
}


def send_email(
    subject: str,
    body: str,
    attachment_path: str,
    group: str,
):
    """
    Envía un correo usando un grupo de destinatarios predefinido
    """

    if group not in RECIPIENT_GROUPS:
        raise ValueError(f"Grupo de destinatarios no definido: {group}")

    from_email = os.getenv("SMTP_USER")
    password = os.getenv("SMTP_PASSWORD")
    to_emails = RECIPIENT_GROUPS[group]

    if not from_email or not password:
        raise RuntimeError("Credenciales SMTP incompletas")

    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = ", ".join(to_emails)
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    with open(attachment_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        filename = os.path.basename(attachment_path)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename={filename}",
        )
        msg.attach(part)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(from_email, password)
        server.sendmail(from_email, to_emails, msg.as_string())