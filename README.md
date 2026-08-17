# CodeFactory Boas-Vindas

> Projeto demonstrativo desenvolvido como parte da adoção da Cultura DevOps na
> CodeFactory Solutions (Atividade Prática — DevOps e Integração Contínua, UNINTER).

## Descrição do projeto

O **CodeFactory Boas-Vindas** é um script em Python que simula a mensagem
de boas-vindas exibida aos novos funcionários da CodeFactory Solutions. É utilizado
como projeto de referência para demonstrar, na prática, a adoção da Cultura DevOps
pela equipe: versionamento com Git/GitHub, containerização com Docker e um pipeline
de Integração Contínua.

## Objetivo

Demonstrar, de forma simples e didática, como práticas e ferramentas de DevOps
(controle de versão colaborativo, containers e automação de build/testes) podem
resolver os problemas de padronização, integração e agilidade enfrentados pela
equipe de desenvolvimento da CodeFactory Solutions.

## Tecnologias utilizadas

- Python 3.11
- pytest (testes automatizados)
- Docker (containerização)
- GitHub Actions (Integração Contínua)

## Estrutura de pastas

```
codefactory-devops/
├── .github/workflows/   # Pipeline de Integração Contínua (GitHub Actions)
├── app/                  # Código-fonte do script
│   └── app.py
├── tests/                # Testes automatizados (pytest)
│   └── test_app.py
├── Dockerfile             # Imagem da aplicação
├── requirements.txt       # Dependências do projeto
├── README.md
└── LICENSE
```

## Como instalar

1. Clone o repositório: `git clone https://github.com/gregory-hack/codefactory-devops.git`
2. Entre na pasta do projeto: `cd codefactory-devops`
3. Siga as instruções da seção "Como executar" abaixo.

## Como executar

### Com Docker (recomendado)

```
docker build -t codefactory-boas-vindas .
docker run codefactory-boas-vindas
```

### Localmente, sem Docker

```
pip install -r requirements.txt
python app/app.py
```

### Rodando os testes

```
pip install -r requirements.txt
python -m pytest
```

## Licença

Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo LICENSE
para mais detalhes.
