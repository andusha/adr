import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = "allerborn20031@gmail.com"
PASSWORD = "hjwrbhbjzhhbexvk"

def send_email(name, phone, comm):
    message = f"Имя: {name}\nНомер: {phone}\n{comm}"
    try:
        # set up the SMTP server
        s = smtplib.SMTP(host="smtp.gmail.com", port=587)
        s.starttls()
        s.login(MY_ADDRESS, PASSWORD)

        msg = MIMEMultipart()  # create a message


        # Prints out the message body for our sake
        print(message)

        # setup the parameters of the message
        msg["From"] = MY_ADDRESS
        msg["To"] = MY_ADDRESS
        msg["Subject"] = ""

        # add in the message body
        msg.attach(MIMEText(message, "plain"))

        # send the message via the server set up earlier.
        s.send_message(msg)
        del msg
    except Exception as e:
        print(f"Ошибка при отправке письма: {e}")
    finally:
        # Terminate the SMTP session and close the connection
        s.quit()
