---
title: "Order by no CouchDB"
date: 2010-05-25 00:23:00
categories: ["CouchDB"]
tags: ["CouchDB", "nosql", "order by", "order by couchdb", "view indexes", "views couchdb"]
---

Uma das cláusulas mais utilizadas em SQL nos bancos relacionais é a **ORDER BY**. Sempre que queremos ordenar o resultado de uma query por determinada coluna de uma tabela, utilizamos **ORDER BY nome\_da\_coluna** e recomenda-se que seja criado um índice para essa coluna, afim de otimizar a ordenação dos dados. O problema começa quando precisamos ordernar os resultados por vários campos da tabela, sendo que pode ficar inviável criar uma série de índices, já que essa tabela pode também sofrer um grande número de atualizações.

Uma das grandes vantagens do [CouchDB](http://www.p3m.com.br/blog/couchdb/) (noSQL) é o poder das [views](http://books.couchdb.org/relax/design-documents/views#What%20is%20a%20View?) (eu sempre gosto de reforçar isso). Você pode criar várias views (que resultem em várias formas) para os seus dados, sem comprometer a inserção para aquele tipo de dado (documento). Ou seja, supondo que você precise ordenar alguns documentos por 3 "campos" diferentes, basta que você crie 3 views, sendo que cada uma emita como chave o determinado "campo" em questão. Podemos exemplificar em Ruby utilizando a gem [CouchRest](http://github.com/couchrest/couchrest), vamos supor um modelo de cidades:

Vamos inserir algumas cidades para exemplificar (eu estou utilizando Rails também)

O CouchRest vai criar 3 views (by\_name, by\_state, by\_population). Ordenando as cidades pelo nome

Repare que no banco será criada a view (função map)

E o resultado será (ordenado alfabeticamente)

Ordenando as cidades pelo número da população, da maior para a menor

Até aí tudo muito simples e fácil, podemos ordenar nossos dados de forma bem **flexível**. Então, vamos complicar um pouco. Vamos supor que queremos filtrar os resultados passando como parâmetro o estado, porém que as cidades sejam ordenadas pela data de criação, de forma que as mais velhas sejam mostradas primeiro. A princípio isso parece estranho, mas é muito útil por exemplo se quisermos ordernar posts, buscando por determinada categoria (queremos que sejam listados os últimos cadastrados) e também em outras situações que se precisa ordenar os resultados de forma crescente ou decrescente.

Se utilizarmos a view que emite apenas o estado como chave (by\_state), o CouchDB vai ordenar as cidades pelo **id** (no caso o id é o nome da cidade) então teríamos as cidades do determinado estado, ordenadas alfabeticamente. Então, precisamos criar uma view que emita um array (estado e data de criação) como chave.  
Acrescente na classe

Será criada a seguinte view

Buscando as cidades (cadastradas primeiro) do estado SP

Repare que a cidade de Sorocaba vem primeiro (pois foi cadastrada primeiro), se tivéssemos utilizado a view que emite como chave apenas o estado, São Paulo viria primeiro

Podemos concluir que as views do CouchDB são **extremamente poderosas e simples**, de início parece complicado, já que estamos habituados ao SQL, porém quando se entende bem o conceito do **Map/Reduce** as coisas ficam bem mais fáceis. No próximo post pretendo escrever sobre agrupamentos ([GROUP BY](http://www.p3m.com.br/blog/group-by-no-couchdb/)).
