---
title: "CouchDB - No Locking"
date: 2010-10-12 18:33:15
categories: ["CouchDB"]
tags: ["CouchDB", "lock", "lock free", "no locking", "rdbms"]
---

**No Locking**

Uma tabela em um banco de dados relacional é uma estrutura de dados única. Se você quer modificar uma tabela – digamos, atualizar um registro – o sistema de banco de dados deve garantir que ninguém mais esteja tentando atualizar aquela linha e que ninguém possa ler aquele registro enquanto ele esteja sendo atualizado. A forma mais comum para lidar com isso é o que conhecemos como lock. Se multiplos clientes quiserem acessar uma tabela, o primeiro cliente seta o lock, fazendo todos os outros clientes esperarem. Quando a requisição do primeiro cliente for processada, o próximo cliente terá acesso enquanto todos os outros clientes esperam e assim por diante. Essa execução de requisições seriais, mesmo quando chegam em paralelo, disperdiçam uma quantidade significativa de poder de processamento do seu servidor. Sob carga alta, um banco de dados relacional pode gastar mais tempo tentando descobrir quem é permitido fazer o que, e em que ordem, do que fazer qualquer trabalho efetivo.

Ao invés de locks, o CouchDB utiliza MVCC - Multi-Version Concurrency Control (controle de concorrência de multi versão) para gerenciar acessos ao banco. MVCC significa que o CouchDB pode ser executado a toda velocidade, todo o tempo, mesmo sob alta carga. As solicitações são executados em paralelo, fazendo um excelente uso de cada última gota do poder de processamento que seu servidor tem para oferecer.

Os documentos no CouchDB são versionados, bem como estariam em um sistema regular de controle de versões como Subversion. Se você quiser alterar um valor em um documento, você cria uma versão totalmente nova daquele documento e salva sobre o antigo.

Como isso oferece uma melhoria em relação aos locks? Considere um conjunto de requisições que querem acessar um documento. A primeira requisição lê o documento. Enquanto isso está sendo processado, a segunda requisição atualiza o documento. Desde que a segunda requisição inclua uma nova versão completa do documento, o CouchDB pode simplesmente adiciona-la ao banco sem ter que esperar pela primeira requisição de leitura terminar.

Quando uma terceira requisição quiser ler o mesmo documento, o CouchDB irá apontar para a nova versão do documento que acabou de ser escrita. Durante todo esse processo, a primeira requisição pode continuar lendo a versão original.

Uma requisição de leitura sempre verá a versão mais atualizada do seu banco no começo da requisição.

Tradução literal do livro [CouchDB the Definite Guide](http://guide.couchdb.org/).
