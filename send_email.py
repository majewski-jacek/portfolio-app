import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "app1generator@gmail.com"
    authentication = "qmyn irgb fvgf cnfy"

    receiver = "majewski.jacek002@gmail.com"
    my_context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, authentication)
        server.sendmail(username, receiver, message)