# MyCroblog

## Criando o diretório do projeto

```zsh
$ mkdir mycroblog && cd mycroblog
```

## Criando um Ambiente Virtual

```zsh
$ python3 -m venv venv
```

## Ativando o Ambiente Virtual

```zsh
$ source venv/bin/active
```

## Instalando o Flask

```zsh
$ pip3 install flask
```

## Executando a aplicação

```zsh
$ export FLASK_APP=mycroblog.py
$ flask run
```

## Utilizando Variáveis de Ambiente

```zsh
$ pip3 install python-dotenv

$ vim .flaskenv

    FLASK_APP=mycroblog.py
```

## Instalando a extensão Flask-WTF (Formulário)

```zsh
$ pip3 install flask-wtf
```

## Instalando a extensão Flask-SQLAlchemy (ORM - Manipular Banco de Dados)

```zsh
$ pip3 install flask-sqlalchemy
```

## Instalando a extensão Flask-Migrate (Atualizar estrutura do banco com mais facilidade)

```zsh
$ pip3 install flask-migrate
```

## Criando o repositório das migrations (pasta migrations)

```zsh
$ flask db init
```

## Gerando as migrations automaticamente

```zsh
$ flask db migrate -m "users table"
```

## Aplicando as alterações das migrations no banco de dados

```zsh
$ flask db upgrade
```

## Iniciando o shell do Flask

```zsh
$ flask shell
```

## Instalando a extensão Flask-Login (gerenciar usuários)

```zsh
$ pip3 install flask-login
```

## Instalando validador de email (WTFroms)

```zsh
$ pip3 install email-validator
```

## Instalando a extensão Flask-Mail

```zsh
$ pip3 install flask-mail
```

## Instalando JSON Web Token (gerar tokens para o flask-mail)

```zsh
$ pip3 install pyjwt
```
