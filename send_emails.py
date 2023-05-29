import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587)  # smtp address and port
conn.ehlo()  # call this to start the connection
# starts tls encryption. When we send our password it will be encrypted.
conn.starttls()  # if you get an error here, you might need to run it again
conn.login('stuartwilson94@gmail.com', 'hsqfwbrqsmthhazh')  # email, password
conn.sendmail('stuartwilson94@gmail.com', 'stuartwilson94@gmail.com',
              'Subject: So long...\n\nDear Stuart,\n\nSo long, and thanks for all the fish.\n\nSincerely,\n\nStuart')  # from, to, message
conn.quit()  # disconnect from the smtp server
# the double newline is necessary to separate the subject from the body
