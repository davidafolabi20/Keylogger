import smtplib
import ssl

print()
def sendEmail(message):
    smtp_server = "smtp.gmail.com"
    port = 465
    sender_email = "example@example.com"
    password = "password"
    receiver_email = "example@example.com"

    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

    except Exception as e:
        print(e)
    finally:
        server.quit()
