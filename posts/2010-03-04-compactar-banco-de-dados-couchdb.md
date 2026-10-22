---
title: "Compactar banco de dados - CouchDB"
date: 2010-03-04 14:17:51
categories: ["CouchDB"]
tags: ["compactar couchdb", "CouchDB", "mvcc"]
---

O CouchDB assim como alguns bancos relacionais (MySQL, Postgre, Oracle etc) utiliza o modelo MVCC (Multiversion concurrency control), então quando um documento recebe uma atualização, é criada uma nova versão do documento.

Devido ao fato da criação de novas versões, seu banco de dados pode começar a crescer exponencialmente. Então você pode compactar o banco, para economizar certo espaço em disco. A compactação comprimi o arquivo de banco de dados removendo seções não utilizadas que foram criadas durante as atualizações.

A compactação pode ser feita enviando uma requisição HTTP Post para o "sub recurso" *\_compact* do seu banco. Em caso de sucesso um status HTTP 202 é retornado.

Você pode verificar informações sobre sua base (inclusive se uma compactação está ocorrendo) enviando uma requisição HTTP Get ao banco.

É recomendado que a compactação seja feita em um horário em que o CouchDB não receba muitas escritas.
