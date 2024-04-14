import smtplib

sender = "theharshithareddy@gmail.com"
receiver = "harshavardhan.vadde@gmail.com"
password = "qfmw qnbp kpdl pfix"
subject = "Python email testinguuu"
body = "Eshh aaaa..I wrote an email using python naniiiiiiii!!"

# header
message = f"""From: Harshii {sender}
To: Nanii 
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender,password)
    print("Logged in...")
    server.sendmail(sender, receiver, message)
    print("Email has been sent!")

except smtplib.SMTPAuthenticationError:
    print("unable to sign in")