# Lab-Engenharia-de-Software
```
2º entrega : https://youtu.be/NsJHofnFqr0
```
# Requisitos:

- [x] Git instalado - <a href=https://git-scm.com/downloads/>Download Git</a>

- [x] Python 3.6 ou maior - <a href=https://www.python.org/downloads/>Download Python</a>


# Para Iniciar o projeto:
Necessário clonar o repositório:

```
  git clone https://github.com/JViniciusF/Lab-Engenharia-de-Software.git
  
  git checkout Segunda-Entrega
  
```

# Ativando o Virtual Environment:

```
python -m venv env

env\Scripts\activate
```

# Instalando as bibliotecas:

```
pip install -r requirements.txt
```
```
# Primeira vez acessando o projeto:

Será necessário utilizar alguns comando para iniciar o projeto pela primeira vez, pois ainda não existe os dados no banco de dados:

```
python wsgi.py init_db
```

Caso já possua os dados no banco de dados, somente é necessário o seguinte comando para iniciar o projeto:

```
python wsgi.py
```

À partir de agora, deverá conter a seguinte mensagem no terminal:

```
Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Basta abrir a URL para acessar o projeto.