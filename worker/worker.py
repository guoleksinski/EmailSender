import redis
import json
from time import sleep
import smtplib
from email.message import EmailMessage
from password import senha

if __name__ == '__main__':
    r = redis.Redis(host='queue', port=6379,db=0)
    while True:
        mensagem = json.loads(r.blpop('sender')[1])
        print('Mandando a mensagem', mensagem['assunto'])
        
        EMAIL_ADDRESS = 'gustavo@consultsis.com.br'
        EMAIL_PASS = senha
        
        msg = EmailMessage()
        msg['Subject'] = mensagem['assunto']
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = 'knz150904@gmail.com'
        msg.set_content(mensagem['mensagem'])
        
        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            smtp.login(EMAIL_ADDRESS,EMAIL_PASS)
            smtp.send_message(msg)
            
        print('Mensagem', mensagem['assunto'], 'enviada')