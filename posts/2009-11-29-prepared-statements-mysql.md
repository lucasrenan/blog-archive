---
title: "Prepared Statements MySQL"
date: 2009-11-29 19:35:10
categories: ["MySQL"]
tags: ["Banco de Dados", "MySQL", "prepared statments", "prepared statments mysql"]
---

**O que são prepared statements?**

Prepared statment serve para setar uma consulta e executá-la várias vezes com parâmetros diferentes. São desenvolvidos para queries ad hoc, são mais seguros e mais eficientes. Segue um exemplo simples:

O ? (ponto de interrogação) é chamado de placeholder. Quando a consulta acima for executada é necessário passar um valor, que será substituído pelo ? na consulta.

**Por que usar prepared statements?**

Existem numerosas vantagens em usar prepared statements em suas aplicações, por duas razões: segurança e performance.

Os prepared statements podem ajudar a aumentar a segurança, pois separam SQL lógico dos dados fornecidos pela aplicação. Essa separação ajuda a previnir uma série de vulnerabilidades conhecidas como Ataques de SQL Injection. Normalmente quando se recebe valores de uma aplicação em uma query ad hoc, você precisa ter muito cuidado com o dado recebido, para isso é necessário utilizar algumas funções de escape de caracteres, como escape de aspas simples, aspas duplas, barras, etc para garantir que nenhum usuário malicioso consiga injetar código na sua query. Quando se está utilizando prepared statments isso não é necessário, a separação dos dados permite que o MySQL automaticamente leve em conta esses caracteres e eles não precisam ser escapados por nenhuma função especial.

O crescimento de performance nos prepared statements podem vir de algumas características diferentes. Primeiro é a necessidade de parsear a consulta apenas uma vez. O MySQL vai parsear a consulta na primeira vez para checar a sintaxe e setar a consulta para ser executada. Então, se você executar a consulta várias vezes, ele não vai precisar ter esse trabalho novamente. Esse pre-parsing pode causar um aumento de velocidade se você precisar executar a consulta várias vezes, como por exemplo quando se precisa fazer vários INSERTs.  
A segunda coisa que pode ser mais rápida é que os prepared statments podem utilizar um protocolo binário. O protocolo tradicional utilizado pelo MySQL sempre converte tudo em strings antes de mandar pela rede. O protocolo binário resolve esse problema, todos os tipos são enviados na sua forma binária nativa, o que economiza tempo de conversão da CPU e pode diminuir o tráfego na rede.

**Quando você deve utilizar prepared statments?**

Os prepared statements podem ser utilizados para uma infinidade de razões, mas não devem ser utilizados em toda sua aplicação. Algumas vezes podem ser mais lentos que uma consulta normal. A razão é que existem dois round-trips ("idas") para o servidor, o que pode comprometer a performance para consultas que são executadas apenas uma vez. Cabe ao desenvolvedor decidir se compensará ter impacto na performance para ganhar mais segurança.

**Considerações finais**

Prepared statments são recursos muito bons de banco de dados quando utilizados adequadamente, podem aumentar performance e segurança.  
Esse texto é uma tradução adaptada do texto de Harrison Fisk.  
O artigo original pode ser encontrado em  
[http://dev.mysql.com/tech-resources/articles/4.1/prepared-statements.html](http://dev.mysql.com/tech-resources/articles/4.1/prepared-statements.html "MySQL Harrison Fisk")
