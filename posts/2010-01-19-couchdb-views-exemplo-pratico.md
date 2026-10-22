---
title: "CouchDB Views - exemplo prático"
date: 2010-01-19 14:25:06
categories: ["CouchDB"]
tags: ["map", "reduce", "select couchdb", "views couchdb"]
---

O CouchDB possui uma interface web (melhor que um phpmyadmin por exemplo) para administração dos dados, chamada Futon. Para acessá-la abra em seu browser:

<http://localhost:5984/_utils/>

Vamos iniciar com um exemplo bem simples de como utilizar views.  
As [views](http://www.p3m.com.br/blog/views-no-couchdb/) são usadas para recuperar os dados do banco. De início talvez pareça um pouco complicado, a maioria de nós está completamente adaptada ao SQL, mas aos poucos vamos mudando nossa forma de pensar (até mesmo quebrando a forma "relacional" de armazenamento dos dados) e vamos aprendendo conceitos interessantes, como [Map/Reduce](http://en.wikipedia.org/wiki/MapReduce).

Vamos supor que precisamos armazenar dados de estudantes (nome e idade apenas). Nos bancos relacionais teríamos que criar uma tabela "estudantes" com os devidos campos e tipos. Isso pode não ser tão bom, já que nem todos os estudantes podem ter as mesmas informações (representação dos dados). Os documentos são bem melhores para representarmos os elementos da vida real, do que as tabelas, são extremamente flexíveis. No CouchDB o documento (JSON) ficaria mais ou menos assim:

Um detalhe para o atributo type (que eu criei) para "informar" qual o tipo de documento, no caso se refere a estudantes.

Vamos supor que teríamos outros documentos no banco (de outros "types" também) e que gostaríamos de selecionar apenas as informações de estudantes. Em SQL seria:

No CouchDB poderíamos criar uma view (em javascript) assim:

Detalhe que essa é uma função do tipo Map. Serão selecionados apenas os documentos com type igual a "Student" e a chave é o nome do estudante.

Existe uma série de vantagens em utilizar o conceito de Map/Reduce, principalmente quando se trata de aplicações que rodam em [clusters](http://pt.wikipedia.org/wiki/Cluster).  
Você também pode ler como funcionam os [índices de views](http://www.p3m.com.br/blog/view-indexes/) no Couch.
