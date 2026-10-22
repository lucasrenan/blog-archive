---
title: "Views no CouchDB"
date: 2010-01-10 23:31:56
categories: ["CouchDB"]
tags: ["CouchDB", "views couchdb", "views no couchdb"]
---

Views são o método de agregação e relatórios sobre os documentos em uma base de dados (os SELECTs dos bancos relacionais), e são construídas por demanda para agregar, juntar e reportar documentos. As views são construídas dinamicamente e não afetam o documento subjacente, você poder ter várias representações diferentes dos mesmos dados que desejar.

As definições de views são estritamente virtuais e somente mostram os documentos da instancia corrente do banco de dados, fazendo-os separados dos dados que eles mostram e compatíveis com replicação. As views do CouchDB são definidas dentro de documentos de design especiais e podem ser replicadas em várias instancias de bancos de dados como documentos regulares, de modo que não apenas os dados são replicados no CouchDB, mas o design da aplicação inteira também é replicado.

**Funções Javascript**

As views são definidas usando funções javascript que atuam como map em um sistema de [map-reduce](http://en.wikipedia.org/wiki/MapReduce). Uma view pega um documento do CouchDB como um argumento e então faz o cálculo que precisar fazer para determinar os dados que serão disponibilizados pela view, se houverem. É possível adicionar multiplas linhas para a view com base em um único documento.

[Índices de Views](http://www.p3m.com.br/blog/view-indexes/)

Essa é uma tradução adaptada:  
<http://couchdb.apache.org/docs/overview.html>
