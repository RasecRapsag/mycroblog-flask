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

## Instalando a extensão Flask-Bootstrap

```zsh
$ pip3 install flask-bootstrap
```

## Instalando a extensão Flask-Moment (Tratamento Data - Moment.js)

```zsh
$ pip3 install flask-moment
```

## Instalando a extensão Flask-Babel (Internacionalização e Localização)

```zsh
$ pip3 install flask-babel
```

## Extraindo os textos para tradução

```zsh
$ pybabel extract -F babel.cfg -k _l -o messages.pot .
```

## Gerando o catálogo do idioma para tradução

```zsh
$ pybabel init -i messages.pot -d app/translations -l pt
```

## Atualizando o catálogo do idioma para tradução

```zsh
$ pybabel update -i messages.pot -d app/translations
```

## Compilando o catálagos de idiomas

```zsh
$ pybabel compile -d app/translations
```

## Instalando biblioteca para reconhecimento de idioma

```zsh
$ pip3 install guess_language-spirit
```

## Instalando biblioteca para HTTP requests

```zsh
$ pip3 install requests
```

## Gerando/Carregando arquivo de requisitos da aplicação

```zsh
$ pip3 freeze > requirements.txt
$ pip3 install -r requirements.txt
```
