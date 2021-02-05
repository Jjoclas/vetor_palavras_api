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
