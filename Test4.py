Create an HTML table with borders
table_with_borders = f'<table border="1">{styled_df.render()}</table>'
msg.attach(MIMEText(table_with_borders, 'html'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_address, password)
server.sendmail(email_address, email_address, msg.as_string())
server.quit()
