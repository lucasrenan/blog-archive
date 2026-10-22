---
title: "Instalar CouchDB no Ubuntu"
date: 2009-11-29 19:38:43
categories: ["CouchDB"]
tags: ["CouchDB", "instalar couchdb", "instalar couchdb no ubuntu"]
---

Para instalar o [CouchDB](http://couchdb.apache.org/ "CouchDB") no Ubuntu você pode simplesmente rodar o seguinte comando:

**sudo apt-get install couchdb**

Se quiser ter a última versão:

**sudo apt-get build-dep couchdb**  
 **sudo apt-get install libmozjs-dev libicu-dev libcurl4-gnutls-dev libtool**

Baixe a última versão (.tar.gz)  
[http://couchdb.apache.org/downloads.html](http://couchdb.apache.org/downloads.html "CouchDB Download")

Descompacte (hoje a versão mais nova é a 0.10.1)  
 **tar -zxvf apache-couchdb-0.10.1.tar.gz**  
 **cd apache-couchdb-0.10.0**

Instale  
 **./configure**  
 **make**  
 **sudo make install**

Com o couchdb instalado, rode para testar:  
 **sudo couchdb**  
e abra no browser http://localhost:5984/\_utils

Você pode encontrar mais detalhes na [wiki do couchdb](http://wiki.apache.org/couchdb/Installing_on_Ubuntu "Wiki CouchDB").
