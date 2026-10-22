---
title: "View Indexes"
date: 2010-01-16 16:59:07
categories: ["CouchDB"]
tags: ["CouchDB", "índices couchdb", "view indexes", "views couchdb", "views no couchdb"]
---

Antes de começar com a tradução sobre os índices de views do CouchDB, quero fazer um agradecimento especial ao [Marcos Tapajós](http://tapajos.me) pela divulgação em [CouchDB para brasileiros](http://tapajos.me/2010/01/13/couchdb-para-brasileiros). O Tapajós trabalha para o Redeparede, para a Improve It e é commiter da gem [CouchRest](http://github.com/couchrest/couchrest). Valeu Tapajós =]

**Índices de views**

As views são representações dinâmicas do conteúdo atual dos documentos de um banco de dados, e o CouchDB faz ser simples a criação de views úteis dos dados. Mas gerar uma view de um banco de dados com centenas de milhares ou milhões de documentos leva tempo e consome recursos, não é algo que o sistema deve fazer do zero toda hora.

Para manter a exibição de consultas rápida, a view engine mantém índices dessas views, e atualiza-os incrementalmente para refletir as mudanças no banco de dados. O design do core do CouchDB é largamente otimizado para criação eficiente de views e seus índices.

Visões e suas funções são definidas dentro de documentos especiais de "design" e um documento de design pode conter várias funções de views (unicamente nomeadas). Quando um usuário abre uma view e seu índice é automaticamente atualizado, todas as views no mesmo documento de design são indexadas em um único grupo.

O construtor de views usa o ID de sequência do banco de dados para determinar se um grupo de views está totalmente atualizado com o banco de dados. Se não, a view engine examina todos os documentos do banco (embalados em ordem sequencial) mudados desde a última atualização. Os documentos são lidos na ordem em que estão os arquivos no disco, reduzindo a frequência e custo de buscas no disco.

As views podem ser lidas e consultadas simultaneamente enquanto estão também sendo atualizadas. Se um cliente está recebendo o conteúdo de uma view grande, a mesma view pode ser aberta e atualizada concorrentemente por outro cliente sem bloquear o primeiro cliente. Isso é verdade para qualquer número de leituras de clientes simultâneos, que podem ler e consultar a view enquanto o índice está concorrentemente sendo atualizado por outros clientes sem causar problemas para os leitores.

Assim os documentos são examinados, os seus valores de linha anterior são removidos dos índices de views, se existirem. Se o documento for selecionado por uma função de view, os resultados da função são inseridos na view como uma nova linha.

Quando as mudanças nos índices de views são escritas no disco, as atualizações são sempre anexadas ao fim do arquivo, servindo tanto para reduzir as buscas no disco durante commits e para garantir que crashes e falhas de falta de energia não corrompam os índices. Se uma falha ocorrer durante uma atualização de um índice, a atualização incompleta do índice é simplesmente perdida e reconstruída incrementalmente a partir do seu estado anterior.

Essa é uma tradução adaptada:  
<http://couchdb.apache.org/docs/overview.html>
