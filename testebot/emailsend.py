import smtplib
import email.message

corpo_email = '''
<h1>Teste automatização com Python3</h1>

<p>aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa</p>
'''

msg = email.message.Message()
msg['Subject'] = 'Teste Automatização E-mail'
msg['From'] = 'tucoosapeca@gmail.com'
msg['To'] = 'arthurluftribeiro@gmail.com'
psw = 'arthur30488792805'
msg.add_header('Content-Type', 'text/html')
msg.set_payload(corpo_email)

s = smtplib.SMTP('smtp.gmail.com: 587')
s.starttls()

s.login(msg['From'], psw)
s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
print('E-mail sent.')