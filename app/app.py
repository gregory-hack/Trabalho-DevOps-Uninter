from datetime import datetime


def boas_vindas(nome):
    agora = datetime.now().strftime("%d/%m/%Y %H:%M")
    print(f"Olá, {nome}! Bem-vindo à Equipe de desenvolvimento da Code Factory.")
    print(f"Ambiente configurado com sucesso em {agora}.")


if __name__ == "__main__":
    boas_vindas("Novo Colaborador")
