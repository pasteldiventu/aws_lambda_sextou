import boto3
import os
from datetime import datetime, timedelta

SNS_TOPIC_ARN = os.environ.get('SNS_TOPIC_ARN')

def lambda_handler(event, context):
    agora = datetime.now()
    dia_semana = agora.weekday() # 0=Segunda, 4=Sexta, 6=Domingo
    
    # Lógica da Sexta-Feira
    if dia_semana == 4: # É Sexta!
        texto = "🍻 SEXTOU! BORATOMAUMAAA!"
        assunto = "🍻 SEXTOU!"
    elif dia_semana > 4: # Sábado ou Domingo
        texto = "É fim de semana. O que você está fazendo olhando e-mails da AWS? BORATOMAUMAAA!"
        assunto = "OIIIIIIIIIIIIII"
    else: # Segunda a Quinta
        dias_faltantes = 4 - dia_semana
        texto = f"Força guerreiro(a). Ainda faltam {dias_faltantes} dias pro sextou. Continue codando."
        assunto = "Contagem regressiva pra gelada"

    send_sns(texto, assunto)
    return {"statusCode": 200, "body": "Checagem de dia feita."}

def send_sns(message, subject):
    client = boto3.client('sns')
    client.publish(TopicArn=SNS_TOPIC_ARN, Message=message, Subject=subject)
