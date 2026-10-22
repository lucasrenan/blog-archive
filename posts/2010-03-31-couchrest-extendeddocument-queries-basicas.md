---
title: "CouchRest ExtendedDocument - Queries Básicas"
date: 2010-03-31 00:52:43
categories: ["CouchDB"]
tags: ["CouchDB", "couchrest", "queries couchdb", "views couchdb"]
---

Em ruby temos algumas gems para serem utilizadas com o [CouchDB](http://www.p3m.com.br/blog/couchdb/). Particularmente eu prefiro a gem [CouchRest](http://github.com/couchrest/couchrest), construída pelos commiters do CouchDB ([Chris Anderson](http://twitter.com/jchris) é um deles). E um dos commiters do CouchRest (que vem fazendo um excelente trabalho) é o [Marcos Tapajos](http://tapajos.me/) da Improve IT e RedeParede.  
Para saber mais como instalar e utilizar o CouchRest acesse a [wiki](http://wiki.github.com/couchrest/couchrest/) no Github.

Vamos considerar a seguinte classe (Post) que herda **ExtendedDocument** da gem CouchRest

Carregando todos os documentos com o "couchrest-type" Post

Carregando um documento pelo ID

**Utilizando Views**

A view criada pelo CouchRest
