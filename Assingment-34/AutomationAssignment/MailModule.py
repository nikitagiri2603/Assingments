import smtplib
from email.message import EmailMessage
import os


SENDER_EMAIL = "example@gmail.com"
SENDER_PASSWORD = "password"


def SendMail(receiver, filepath):

    try:

        msg = EmailMessage()

        msg["Subject"] = "Process Log File"

        msg["From"] = SENDER_EMAIL

        msg["To"] = receiver

        msg.set_content(
            "Please find attached process log."
        )

        with open(filepath, "rb") as file:

            data = file.read()

            filename = os.path.basename(filepath)

        msg.add_attachment(
            data,
            maintype="application",
            subtype="octet-stream",
            filename=filename
        )

        smtp = smtplib.SMTP("smtp.gmail.com",587)

        smtp.starttls()

        smtp.login(
            SENDER_EMAIL,
            SENDER_PASSWORD
        )

        smtp.send_message(msg)

        smtp.quit()

        return True

    except Exception:

        return False