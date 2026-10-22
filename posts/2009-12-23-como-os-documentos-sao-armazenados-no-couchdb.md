---
title: "Como os documentos são armazenados no CouchDB?"
date: 2009-12-23 00:19:37
categories: ["CouchDB"]
tags: ["CouchDB", "couchdb storage", "documentos couchdb"]
---

O CouchDB armazena os dados em documentos. Cada documento tem um nome único no banco e o CouchDB provê uma API HTTP [RESTful](http://pt.wikipedia.org/wiki/REST) para ler e atualizar (adicionar, editar, excluir) os documentos do banco de dados.

Os documentos são as unidades primárias de dados, consistem em um número qualquer de campos e anexos. Os documentos também incluem metadados que são mantidos pelo sistema de banco de dados. Os campos possuem nomes únicos (por documento) e contem valores de vários tipos (texto, número, booleano, listas, etc) e não há qualquer limite definido para o tamanho do texto ou elemento.

O modelo de atualização de documentos do CouchDB é lockless (sem lock) e otimista. Edições nos documentos são feitas por aplicações clientes que carregam os documentos, aplicam as alterações e salvam de volta ao banco de dados. Se outro cliente que estiver editando o mesmo documento salvar as alterações primeiro, o cliente recebe um erro de conflito de edição. Para resolver o conflito de atualização, a versão mais recente do documento pode ser aberta, a edição é reaplicada e a atualização é tentada novamente.

As alterações nos documentos (adicionar, editar, excluir) são "tudo ou nada", tem sucesso completamente ou falha completamente. O banco nunca contem documentos salvos ou editados parcialmente.

Essa é uma tradução adaptada do início do Overview técnico do CouchDB:  
<http://couchdb.apache.org/docs/overview.html>
