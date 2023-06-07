import smtplib
from datetime import datetime, timedelta

def enviar_email(tag, dias_restantes):
    # Configurações do servidor SMTP
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    smtp_username = 'seu_email@example.com'
    smtp_password = 'sua_senha'

    sender = 'seu_email@example.com'
    recipient = 'destinatario@example.com'

    subject = f"Calibração da Mangueira {tag}"
    body = f"A mangueira {tag} precisa ser calibrada em {dias_restantes} dias."

    message = f"Subject: {subject}\n\n{body}"

    try:
        # Inicialização da conexão SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Envio do e-mail
        server.sendmail(sender, recipient, message)
        print("E-mail enviado com sucesso!")

    except Exception as e:
        print(f"Erro ao enviar e-mail: {str(e)}")

    finally:
        # Encerramento da conexão SMTP
        server.quit()


def calcular_dias_restantes(ultima_calibracao):
    # Converter a data de última calibração para um objeto de data
    ultima_calibracao = datetime.strptime(ultima_calibracao, '%Y-%m-%d')

    # Calcular a data de vencimento da próxima calibração
    proxima_calibracao = ultima_calibracao + timedelta(days=180)

    # Calcular a diferença entre a data atual e a data de vencimento
    dias_restantes = (proxima_calibracao - datetime.now()).days

    return dias_restantes


def verificar_calibracao(tag, ultima_calibracao):
    dias_restantes = calcular_dias_restantes(ultima_calibracao)

    # Verificar se está a 2 meses do vencimento
    if dias_restantes == 60:
        enviar_email(tag, dias_restantes)
    # Verificar se está a 1 mês do vencimento
    elif dias_restantes == 30:
        enviar_email(tag, dias_restantes)
    # Verificar se está a 15 dias do vencimento
    elif dias_restantes == 15:
        enviar_email(tag, dias_restantes)
    # Verificar se é o dia do vencimento
    elif dias_restantes == 0:
        enviar_email(tag, dias_restantes)


# Exemplo de uso
tag = input("Digite a tag da mangueira: ")
ultima_calibracao = input("Digite a data da última calibração (YYYY-MM-DD): ")

verificar_calibracao(tag, ultima_calibracao)