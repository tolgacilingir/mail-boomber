#IMPORT LIBRARIES
#for use os commands.
from os import system, name

#for use to send e-mail.
from smtplib import SMTP_SSL as smtpserver

#for use to sleep.
from time import sleep

#for use to take password hiddenly.
from getpass import getpass

#for use to close the app. 
from sys import exit

#DEFINE CLEAR SCREEN FUNCTION
def clear():
    system("cls" if name == "nt" else "clear")

#START COLOR PROCESS
system("color")

#DEFINE COLORS
red   = '\33[31m'
green  = '\33[32m'
yellow = '\33[33m'
white = '\33[37m'

#DEFINE BANNER
def banner():
    title="""
BOOM MAIL
"""

def log():
    global input_
    email_number = 0
    email = input(red + "Email: ")
    password = getpass("Password: ")

    if input_ == 1: 
        server = smtpserver("smtp.gmail.com", 465)
    elif input_ == 2: 
        server = smtpserver("smtp.yahoo.com", 465)
    elif input_ == 3: 
        server = smtpserver('smtp-mail.outlook.com', 465)

    try:
        server.login(email, password)
        print(green + "Login done!")
        sleep(0.75)
    except Exception as e:
        print(yellow + "Something wrong!")
        sleep(0.75)
        print(yellow + "Retrying...")
        sleep(0.75)
        log()  # Tekrar deneme için log() fonksiyonunu yeniden çağırıyoruz
        return  # Ek olarak, bu hatayı işledikten sonra fonksiyondan çıkıyoruz

    to = input(white + "To: ")
    subject = input("Subject (optional): ")
    subject = f"Subject: {subject}\n"
    message = input("Message: ")
    if not subject == "":
        message = subject + message

    amount = int(input("Amount: "))

    try:
        for mail in range(amount):
            server.sendmail(email, to, message)
            email_number += 1
            print(green + "Email sent: " + str(email_number))
        print(green + "Done! Total email sent: " + str(email_number))
        sleep(0.75)
        server.quit()
    except Exception as e:
        print(yellow + "Something wrong! Error:", e)
        sleep(0.75)
        exit()


#LOOP OF TOOL
while True:
    clear()
    banner()
    print(red+"--Choose your email server--------------------")
    print(green+"""01] Gmail server
02] Yahoo server (Not tested)
03] Outlook server (Not tested)
99] Exit""")
    print(red+"----------------------------------------------\n")
    try:
        input_=int(input(white+"E-Bomber:~$ "))
        if input_ < 1 or input_ > 3 and not input_ == 99:
            raise ValueError
    except ValueError:
        print(yellow+"Command not found!")
        sleep(0.75)

    if input_ == 99:
        exit()
    
    clear()
    banner()
    log()