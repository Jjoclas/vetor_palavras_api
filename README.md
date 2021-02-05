# Documentação:
Como realizar uma chamada:
Methodo 'POST'.
Body:
```
     {
        'files[]': (arquivos a serem enviados),
        'n_gram': Numero de conjunto de palavras no vocabulario; default=1.
     }
```
Response:
No caso de n_gram = 1:
```
{
    "vocabulario": [
        "falar",
        "fácil",
        "mostreme",
        "código",
        "falar",
        "fácil",
        "mostreme",
        "código",
        "fácil",
        "escrever",
        "código",
        "difícil",
        "escrever",
        "código",
        "funcione"
    ],
    "vetores": {
        "texto1.txt": [
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            0,
            1,
            0,
            0,
            1,
            0
        ],
        "texto2.txt": [
            0,
            1,
            0,
            2,
            0,
            1,
            0,
            2,
            1,
            2,
            2,
            1,
            2,
            2,
            1
        ]
    }
}
```
No caso de n_gram = 2:
```
{
    "vocabulario": [
        "código fácil",
        "fácil escrever",
        "código difícil",
        "mostreme código",
        "código falar",
        "falar fácil",
        "fácil mostreme",
        "escrever código",
        "difícil escrever",
        "código funcione"
    ],
    "vetores": {
        "texto1.txt": [
            0,
            0,
            0,
            1,
            0,
            1,
            1,
            0,
            0,
            0
        ],
        "texto2.txt": [
            0,
            1,
            1,
            0,
            0,
            0,
            0,
            1,
            1,
            1
        ]
    }
}
```
# Tecnologias:
## API:
Foi utilizado o Flask na criação da API, a escolha foi dada pela facilidade e agilidade no desenvolvimento com essa tecnologia.

Hospedado na AWS utilizando o ElastickBeanStalk [link]

## Banco de dados:
Foi utilizado o PostgreSQl hospedado no [elephantSQL](https://www.elephantsql.com/)

# Rodando teste unitario:
## Foi implementado o teste unitario para a função monta_vetor.
Para realizar o teste basta executar o comando:

```
python -m unittest test.py
```


# Como Instalar o projeto:
### Requerimentos:  
Versão do Python: 3.7  
Framework: Flask  
Ambiente: VirtualEnv


### Passos
#### 1 - Clonando o projeto
Primeiramente, clone o projeto para sua máquina:

```
git clone [https://github.com/Jjoclas/vetor_palavras_api.git]
```

#### 3 - Instalação do VirtualEnv
Utilizar o pip (Gerenciador de pacotes do Python) para realizar a instalação do virtualenv:
```
pip install virtualenv
```

#### 4 - Criando o ambiente virtual do projeto
Na pasta raiz de seu projeto, execute os seguintes comandos para criar o ambiente virtual.

Para linux:
```
virtualenv-3.6 venv
```
Para windows:
```
virtualenv venv
```

Logo em seguida, é necessário ativar o ambiente virtual criado:

Para linux:
```
. venv/bin/activate
```
Para windows:
```
venv\Scripts\activate
```

**- Intalando os pacotes da aplicação:**

Caso exista apenas 1 versão do Python instalada no computador, utilizar o comando abaixo:
```
pip install -r requirements.txt
```
