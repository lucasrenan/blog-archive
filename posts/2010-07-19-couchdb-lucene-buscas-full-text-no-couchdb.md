---
title: "CouchDB Lucene - Buscas Full-text no CouchDB"
date: 2010-07-19 12:07:20
categories: ["CouchDB"]
tags: ["CouchDB", "couchdb lucene", "full text", "full text couchdb", "lucene"]
---

O [CouchDB Lucene](http://github.com/rnewson/couchdb-lucene) provê a funcionalidade de realizar buscas full-text no [CouchDB](http://www.p3m.com.br/blog/couchdb/) utilizando [Lucene](http://lucene.apache.org/).

Antes de começar precisamos instalar as dependências, só lembrando que esse tutorial foi testado nas versões 10.04 e 9.10 do Ubuntu Linux, mas a princípio o procedimento de instalação para Mac deve ser parecido.  
No Ubuntu 10.04 os pacotes [sun-java6 foram removidos da seção Multiverse do Ubuntu archive](http://andrenoel.com.br/2010/04/26/cade-o-meu-plugin-do-java/), então você precisa adicionar o repositório Partner da Canonical.

Então você pode [instalar o JDK e o JRE](http://www.cyberciti.biz/faq/howto-ubuntu-linux-install-configure-jdk-jre/):

Para instalar o CouchDB Lucene é preciso que você tenha o [Git](http://git-scm.com/) e o [Maven](http://maven.apache.org/) instalados:

Finalmente para instalar o CouchDB Lucene é necessário clonar o repositório:

No caso, hoje a versão estável é a 0.5.3, então vamos dar o build:

**Configurando o CouchDB**  
Agora vamos configurar o CouchDB editando o arquivo de configuração que geralmente está localizado em */usr/local/etc/couchdb/local.ini*

Agora vamos criar uma view de exemplo, supondo que temos um **design document** de Posts

Pronto, você pode realizar buscas full-text no CouchDB utilizando Lucene:
