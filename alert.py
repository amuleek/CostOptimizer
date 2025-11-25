import smtplib

def send_email_alert(msg) :
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("amuleeksandhu@gmail.com", "password")
    server.sendmail("amuleeksandhu@gmail.com", "receiver@gmail.com", msg)
    server.quit()
    