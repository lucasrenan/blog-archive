---
title: "Group by no Couchdb"
date: 2010-07-18 19:32:06
categories: ["CouchDB"]
tags: ["CouchDB", "group by couchdb", "group level", "nosql", "views couchdb"]
---

No post anterior sobre [Order by no CouchDB](http://www.p3m.com.br/blog/order-by-no-couchdb/) eu mencionei que o próximo post seria sobre Group by, como prometido vou tentar abordar essa questão apresentando um exemplo simples de como agrupar resultados de views.

Para facilitar (como sempre) estou utilizando **Ruby on Rails + CouchRest**, porém vou postar aqui só a parte relevante do código para entendermos o exemplo. Então vamos considerar nosso model Post:

Detalhe para a view *data* que emite como chave um array contendo o ano, mes e dia do post e para cada valor (dependendo do agrupamento) emite o valor 1 para a **função reduce** (que conta quantos valores foram emitidos para cada chave em questão).

Não vou postar o código de inserção dos posts, você pode inserir alguns posts na sua base para realizar os testes.  
Primeiro quero contar o número de posts realizados por dia (isso é possível pois a função map gera o array com dia, mês e ano, assim a função reduce soma os valores para as chaves).

Acessando a url acima você vai ver um resultado parecido com esse:

Ou seja, no dia 10/06/2010 foi cadastrado um post, assim como no dia 17/07/2010, já no dia 18/07/2010 foram cadastrados dois posts (esses são os posts que eu tenho cadastrado na minha base).

Agora vamos supor que queremos contar quantos posts foram cadastrados por ano. Isso é muito simples utilizando a view que já temos, o CouchDB aceita um parâmetro chamado **group\_level**. Cada posição do array que foi emitida é um "level", então podemos agrupar os valores por cada posição do array. Se passarmos group\_level=2 serão emitidos como chave o ano e o mês, group\_level=1 apenas o mês, etc.

A url seria parecida com essa:

E o resultado seria quatro posts para o ano de 2010

Podemos concluir que agrupar valores no CouchDB não é tão difícil quanto parece, acredito que é uma questão da modelagem dos dados e da forma como utilizamos as views.
