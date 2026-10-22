---
title: "Autenticar usuário no CouchDB"
date: 2010-02-11 20:01:34
categories: ["CouchDB"]
tags: ["autenticar usuario couchdb", "configurar usuario couchdb", "CouchDB", "couchrest"]
---

Por padrão o CouchDB não exige que seja configurado uma conta com usuário e senha, porém criar uma conta é simples.  
Para criar uma conta edite o arquivo *local.ini*

Altere **require\_valid\_user** para true na sessão *couch\_httpd\_auth*

Acrescente o usuário e senha na sessão *admins*

Reinicie o CouchDB

O CouchDB irá criar um hash com a senha:

Se você estiver programando em ruby e utilizando a gem [couchrest](http://github.com/couchrest/couchrest), você pode fazer a conexão assim:
