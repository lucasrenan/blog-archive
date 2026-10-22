---
title: "CouchDB - Implementação"
date: 2010-02-06 00:36:08
categories: ["CouchDB"]
tags: ["banco de dados orientados a documentos", "CouchDB", "erlang", "lock free", "nosql"]
---

O [CouchDB](http://www.p3m.com.br/blog/couchdb/) é feito na [plataforma Erlang OTP](http://www.erlang.org/), uma linguagem de programação funcional, concorrente e uma plataforma de desenvolvimento. Erlang foi desenvolvida para aplicações em tempo real de telecomunicações com ênfase na extrema confiabilidade e disponibilidade.

Na sintaxe e na semântica, Erlang é muito diferente de linguagens de programação convencionais como C ou Java. Erlang usa "processos" leves e passagem de mensagem por concorrência, não tem compartilhamento de estado de thread e todos os dados são imutáveis. A natureza robusta e concorrente do Erlang é ideal para um servidor de banco de dados.

O CouchDB é projetado para concorrência livre de locks, no modelo conceitual e na implementação atual do Erlang. Reduzindo gargalos e evitando locks mantém o sistema inteiro funcionando previsivelmente sobre cargas pesadas. O CouchDB pode acomodar muitas mudanças de replicação de clientes, abrir e atualizar documentos, consultar views cujos índices estão sendo simultaneamente sendo atualizados por outros clientes, sem precisar de locks.

Para alta disponibilidade e mais usuários concorrentes, o Couchdb é projetado para um cluster "shared nothing". Em um cluster "shared nothing", cada máquina é independente e replica dados com seus companheiros de cluster, deixando falhas individuas de servidores com zero de downtime. E porque scans de consistência e consertos não são necessários no restart, se o cluster inteiro falhar - devido a uma queda de energia no datacenter, por exemplo - todo o sistema distribuído do CouchDB volta a ficar disponível depois de um restart.

O CouchDB é construído desde o início com uma visão consistente de um sistema distribuído de banco de dados orientado a documento. Ao contrário de tentativas pesadas em construir recursos distribuídos no topo da mesma herança de modelos e base de dados, ele é o resultado de um projeto, engenharia e integração cuidadosos. O documento, view, segurança e modelos de replicação, a proposta especial da linguagem de query, o layout robusto e eficiente de disco e a natureza concorrente e real da plataforma Erlang são cuidadosamente integrados para um sistema real e eficiente.

Essa é uma tradução adaptada:  
<http://couchdb.apache.org/docs/overview.html>
