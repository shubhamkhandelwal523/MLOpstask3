# Python program for sending email
# Import the smtplib module
# The smtplib module defines an SMTP client session object
# that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon.
import smtplib
import urllib.request as urllib
# Senders email
sender_email = "shubhamkhandelwal523@gmail.com"
# Receivers email
rec_email = "shubhamkhandelwal523@gmail.com"

message = "Best Model is created... Thank You"
# Initialize the server variable
server = smtplib.SMTP('smtp.gmail.com', 587)
# Start the server connection
server.starttls()
# Login
server.login("shubhamkhandelwal523@gmail.com", "shivam1998")
print("Login Success!")
# Send Email
server.sendmail("Shubham khandelwal", "shubhamkhandelwal523@gmail.com", message)
print(f"Email has been sent successfully to {rec_email}")
