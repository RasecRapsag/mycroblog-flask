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
$ source venv/bin/activate
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

## Instalando biblioteca para trabalhar com Elasticsearch

```zsh
$ pip3 install elasticsearch
```

## Fazendo o deploy num servidor Linux (Ubuntu)

```zsh
# Instalando pacotes necessários
$ sudo apt -y update
$ sudo apt -y install python3 python3-venv python3-dev
$ sudo apt -y install mysql-server postfix supervisor nginx git

# Configurando banco de dados
$ sudo mysql -u root -p

mysql> SET GLOBAL validate_password_policy=LOW;
mysql> SET GLOBAL validate_password_length = 6;
mysql> SET GLOBAL validate_password_number_count = 0;
mysql> CREATE DATABASE mycroblog CHARACTER SET utf8 COLLATE utf8_bin;
mysql> CREATE USER 'mycroblog'@'localhost' IDENTIFIED BY '123456';
mysql> GRANT ALL PRIVILEGES ON mycroblog.* TO 'mycroblog'@'localhost';
mysql> FLUSH PRIVILEGES;
mysql> QUIT;

# Criando ambiente virtual para a aplicação
$ git clone https://github.com/RasecRapsag/mycroblog-flask mycroblog
$ cd mycroblog
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt

# Configurando a aplicação
(venv) $ pip install gunicorn pymysql
(venv) $ cp .env.example .env
(venv) $ python3 -c "import uuid; print(uuid.uuid4().hex)" # SECRET_KEY
(venv) $ vim .env

    SECRET_KEY=6c844fea0be6496b8daa6d2a407d371f
    DATABASE_URL=mysql+pymysql://mycroblog:123456@localhost:3306/mycroblog
    MAIL_SERVER=smtp.mailtrap.io
    MAIL_PORT=2525
    MAIL_USE_TLS=None
    MAIL_USERNAME=None
    MAIL_PASSWORD=None
    MS_TRANSLATOR_KEY=None
    ELASTICSEARCH_URL=None

(venv) $ vim .flaskenv

    FLASK_APP=mycroblog.py
    FLASK_ENV=prodution
    FLASK_DEBUG=0

(venv) $ flask db upgrade
(venv) $ flask translate compile

# Configurando o supervisor para aplicação
(venv) $ sudo vim /etc/supervisor/conf.d/microblog.conf

[program:mycroblog]
command=/home/ubuntu/mycroblog/venv/bin/gunicorn -b localhost:8000 -w 4 mycroblog:app
directory=/home/ubuntu/mycroblog
user=ubuntu
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true

# Configurando o supervisor para worker do redis queue
(venv) $ sudo vim /etc/supervisor/conf.d/rq.conf

[program:rq]
command=rq worker mycroblog-tasks
directory=/home/ubuntu/mycroblog
user=ubuntu
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true

(venv) $ sudo supervisorctl reload

# Configurando o NGINX
(venv) $ mkdir certs
(venv) $ openssl req -new -newkey rsa:4096 -days 365 -nodes -x509 -keyout certs/key.pem -out certs/cert.pem
(venv) $ sudo rm /etc/nginx/sites-enabled/default
(venv) $ sudo vim /etc/nginx/sites-enabled/mycroblog

server {
    # listen on port 80 (http)
    listen 80;
    server_name _;
    location / {
        # redirect any requests to the same URL but on https
        return 301 https://$host$request_uri;
    }
}
server {
    # listen on port 443 (https)
    listen 443 ssl;
    server_name _;

    # location of the self-signed SSL certificate
    ssl_certificate /home/ubuntu/mycroblog/certs/cert.pem;
    ssl_certificate_key /home/ubuntu/mycroblog/certs/key.pem;

    # write access and error logs to /var/log
    access_log /var/log/mycroblog_access.log;
    error_log /var/log/mycroblog_error.log;

    location / {
        # forward application requests to the gunicorn server
        proxy_pass http://localhost:8000;
        proxy_redirect off;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /static {
        # handle static files directly, without forwarding to the application
        alias /home/ubuntu/mycroblog/app/static;
        expires 30d;
    }
}

(venv) $ sudo systemctl reload nginx

# Deploy de updates na aplicação
(venv) $ git pull
(venv) $ sudo supervisorctl stop mycroblog
(venv) $ flask db upgrade
(venv) $ flask translate compile
(venv) $ sudo supervisorctl start mycroblog
```

## Fazendo o deploy no Heroku

```zsh
# Criando a aplicação no Heroku
$ heroku login
$ heroku apps:create flask-mycroblog
$ git remote -v

# Adicionando Postgres ao Heroku
$ heroku addons:add heroku-postgresql:hobby-dev

# Adicionando Redis ao Heroku
$ heroku addons:create heroku-redis:hobby-dev

# Setando a variável dos logs
$ heroku config:set LOG_TO_STDOUT=1

# Setando a variável FLASK_APP
$ heroku config:set FLASK_APP=mycroblog.py

# Fazendo o deploy
$ git push heroku master

# Iniciar Worker task
$ heroku ps:scale worker=1

# Remover aplicação
$ heroku apps:destroy flask-mycroblog
```

## Fazendo o deploy no Docker

```zsh
# Criando a imagem docker
$ docker build -t mycroblog:latest .

# Criando um container com Mysql
$ docker run --name mysql -d -e MYSQL_RANDOM_ROOT_PASSWORD=yes \
    -e MYSQL_DATABASE=mycroblog -e MYSQL_USER=mycroblog \
    -e MYSQL_PASSWORD=mycroblog \
    mysql/mysql-server:5.7

# Criando um container com Elasticsearch
$ docker run --name elasticsearch -d -p 9200:9200 -p 9300:9300 --rm \
    -e "discovery.type=single-node" \
    docker.elastic.co/elasticsearch/elasticsearch-oss:7.8.0

# Criando um container com Redis
$ docker run --name redis -d -p 6379:6379 redis:3-alpine

# Criando um container com o Mycroblog
$ docker run --name mycroblog -d -p 8000:5000 --rm -e SECRET_KEY=6c844fea0be6496b8daa6d2a407d371f \
    -e MAIL_SERVER=smtp.mailtrap.io -e MAIL_PORT=587 -e MAIL_USE_TLS=true \
    -e MAIL_USERNAME=username -e MAIL_PASSWORD=senha \
    --link mysql:db \
    -e DATABASE_URL=mysql+pymysql://mycroblog:mycroblog@db/mycroblog \
    --link elasticsearch:elasticsearch \
    -e ELASTICSEARCH_URL=http://elasticsearch:9200 \
    -e REDIS_URL=redis://redis-server:6379/0 \
    mycroblog:latest

# Iniciando um Worker do Radius Queue
$ docker run --name rq-worker -d --rm -e SECRET_KEY=6c844fea0be6496b8daa6d2a407d371f \
    -e MAIL_SERVER=smtp.mailtrap.io -e MAIL_PORT=587 -e MAIL_USE_TLS=true \
    -e MAIL_USERNAME=username -e MAIL_PASSWORD=senha \
    --link mysql:db --link redis:redis-server \
    -e DATABASE_URL=mysql+pymysql://mycroblog:mycroblog@db/mycroblog \
    -e REDIS_URL=redis://redis-server:6379/0 \
    --entrypoint venv/bin/rq \
    mycroblog:latest worker -u redis://redis-server:6379/0 mycroblog-tasks
```

# Instalando o RQ (Redis Queue)

```zsh
$ pip3 install rq
```

# Instalando httpie (Cliente http de linha de comando)

```zsh
$ pip3 install httpie

$ http GET http://127.0.0.1:5000/api/users/1

$ http POST http://127.0.1:5000/api/users username=glorfindel password=123456 email=glorfindel@middle.earth "about_me=Hello, my name is Glorfindel! "

http PUT http://127.0.0.1:5000/api/users/24 "about_me=They forgot me in the movie!!! "
```

# Instalando a extensão Flask-HTTPAuth (Interação cliente servidor - autenticação)

```zsh
$ pip3 install flask-httpauth
```

# Fazendo autenticação via api

```zsh
# Fazendo a autenticação
$ http --auth <username>:<password> POST http://localhost:5000/api/tokens

# Acessando api passando o token
$ http GET http://localhost:5000/api/users/1 \
    "Authorization:Bearer UNDBnKuQZrlugoflgvxGwRauE4vZ/kvU"

# Revogando o token de acesso
$ http DELETE http://localhost:5000/api/tokens \
    Authorization:"Bearer UNDBnKuQZrlugoflgvxGwRauE4vZ/kvU"
```
