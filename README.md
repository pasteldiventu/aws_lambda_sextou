# aplicacao com aviso no email de Sexta-Feira Serverless

Este projeto é uma função AWS Lambda que notifica via e-mail o status da semana (se já é sexta-feira ou não).

## 🛠 Arquitetura AWS
O projeto utiliza a seguinte stack totalmente gratuita (Free Tier):

1.  **Amazon EventBridge (Scheduler):**
    * Trigger configurado com Cron Expression `cron(0 13 * * ? *)`.
    * Dispara todos os dias às 13:00 UTC (09:00 Cuiabá).
2.  **AWS Lambda (Backend):**
    * Runtime: Python 3.12.
    * Executa a lógica de verificação de datas.
3.  **Amazon SNS (Notification):**
    * Tópico configurado para disparar e-mails para os inscritos.

## ⚙️ Variáveis de Ambiente
Para rodar, a função Lambda exige a seguinte variável:
* `SNS_TOPIC_ARN`: O ARN do tópico SNS criado na conta AWS.
