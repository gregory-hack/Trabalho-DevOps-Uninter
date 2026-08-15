from datetime import datetime


def boas_vindas(nome):
    agora = datetime.now().strftime("%d/%m/%Y %H:%M")
    print(f"Olá, {nome}! Bem-vindo à CodeFactory Solutions.")
    print(f"Ambiente configurado com sucesso em {agora}.")

def despedida(nome):
    agora = datetime.now().strftime("%d/%m/%Y %H:%M")
    print(f"Olá, {nome}! Obrigado por ter feito parte do time Code Factory, desejamos boa sorte e muito sucesso em sua nova jornada.")
    print(f"Ambiente configurado com sucesso em {agora}.")

if __name__ == "__main__":
    nome = "Novo Colaborador"
    agora = boas_vindas(nome)
    despedida(nome)


def gerar_css():
    conteudo = """body {
    font-family: Arial, sans-serif;
    background-color: #f4f6f8;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
}

.card {
    background-color: #ffffff;
    padding: 40px;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    text-align: center;
}

h1 {
    color: #1a2b4c;
}

p {
    color: #555555;
}
"""
    with open("style.css", "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo)
    print("Arquivo style.css gerado com sucesso.")


def gerar_html(nome, agora):
    conteudo = f"""<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Boas-vindas - CodeFactory Solutions</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="card">
        <h1>Olá, {nome}!</h1>
        <p>Bem-vindo à CodeFactory Solutions.</p>
        <p>Ambiente configurado com sucesso em {agora}.</p>
    </div>
</body>
</html>
"""
    with open("index.html", "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo)
    print("Arquivo index.html gerado com sucesso.")


if __name__ == "__main__":
    nome = "Novo Colaborador"
    agora = boas_vindas(nome)
    despedida(nome)
