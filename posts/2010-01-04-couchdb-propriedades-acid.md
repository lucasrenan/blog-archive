---
title: "CouchDB - Propriedades ACID"
date: 2010-01-04 18:56:28
categories: ["CouchDB"]
tags: ["acid", "CouchDB", "couchdb acid", "documentos couchdb", "mvcc"]
---

O CouchDB possui totais características das propriedades [ACID](http://pt.wikipedia.org/wiki/ACID) (atomicidade, consistencia, isolamento e durabilidade). Em disco, o CouchDB nunca sobrescreve dados salvos ou estruturas associadas, assegurando que os dados estejam sempre em um estado consistente. Trata-se de um design "crash-only" aonde o servidor CouchDB não passa por um processo de shut down, ele é simplesmente terminado.

Alterações nos documentos (adicionar, editar, deletar) são serializadas, exceto os blobs binários que são escritos concorrentemente. Leituras no banco nunca são bloqueadas (lock) e nunca tem que esperar por escritas ou outras leituras. Qualquer número de clientes podem ler documentos sem serem bloqueados ou interrompidos por atualizações concorrentes, mesmo no mesmo documento. O CouchDB lê operações utilizando o modelo [MVCC](http://en.wikipedia.org/wiki/Multiversion_concurrency_control) (Multiversion concurrency control) aonde cada cliente ve uma cópia consistente do banco de dados desde o início até o fim da operação de leitura.

Os documentos são indexados em b-trees pelo seu nome (DocID) e um ID de sequência. Cada atualização para uma instância de banco de dados gera um novo número sequencial. IDs de sequência são usados depois para encontrar as mudanças de forma incremental em uma base de dados. Esses índices b-trees (árvores B) são atualizados simultaneamente quando os documentos são salvos ou deletados. A atualização dos índices sempre ocorre no final do arquivo (append-only updates).

Os documentos têm a vantagem dos dados serem convenientemente "embalados" para armazenamento em vez de dividir em numerosas tabelas e linhas como na maioria dos bancos de dados. Quando os documentos são salvos em disco, os campos dos documentos e metadados são colocados em buffers, sequencialmente um documento depois do outro (depois isso é útil para construção de views).

Quando os documentos do CouchDB são atualizados, todos os dados e índices associados são "descarregados" (flushed) no disco e o commit transacional sempre deixa o banco em um estado completamente consistente. Commits ocorrem em dois passos:

1 - Todos os dados dos documentos e atualizações em índices associados são "esvaziados" (flushed) no disco de maneira síncrona.  
2 - O cabeçalho do banco de dados atualizados é escrito em dois pedaços consecutivos e idênticos para compor os primeiros 4k do arquivo, então é "esvaziados" (flushed) no disco de maneira síncrona.

No caso do sistema operacional dar "crash" ou uma falta de energia no passo 1, as atualizações parcialmente liberadas são simplesmente esquecidas ao reiniciar. Se acontecer algum acidente no passo 2 (commitando o cabeçalho), uma cópia sobrevivente idêntica aos cabeçalhos anteriores permanecerão, garantido a coerência de todos os dados previamente salvos. Exceto a área de cabeçalho, checagens de consistencia ou consertos depois de um crash ou falta de energia, nunca são necessários.

Essa é uma tradução adaptada:  
<http://couchdb.apache.org/docs/overview.html>
