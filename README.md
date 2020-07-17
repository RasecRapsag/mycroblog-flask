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
