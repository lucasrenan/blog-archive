---
title: "Propriedades ACID"
date: 2010-03-28 16:11:52
categories: ["Banco de Dados"]
tags: ["acid", "atomicidade", "consistencia", "durabilidade", "isolamento", "propriedades acid"]
---

Ultimamente escrevi alguns posts sobre o [CouchDB](http://www.p3m.com.br/blog/couchdb/), um deles referente as [propriedades ACID](http://www.p3m.com.br/blog/couchdb-propriedades-acid/).  
As propriedades ACID (atomicidade, consistência, isolamento e durabilidade) são fundamentais nos bancos de dados, sejam os relacionais ou os orientados a documentos. Então, também é valido tratarmos desse assunto referente aos bancos relacionais, em um contexto geral.  
Atualmente os sistemas de informação suportam vários usuários. O banco de dados tem que garantir a confiabilidade nas transações, haja vista que muitas podem ocorrer concorrentemente.

**O que é uma transação?**

Uma transação é um programa em execução que forma uma unidade lógica de processamento no banco de dados. Uma transação inclui uma ou mais operações de acesso ao banco de dados — englobam operações de inserção, exclusão, alteração ou recuperação. \*

**Por que a Restauração (Recuperação) é Necessária?**

O sistema deverá garantir que: (1) todas as operações na transação foram com­pletadas com sucesso e seu efeito será gravado permanentemente no banco de dados ou (2) a transação não terá nenhum efei­to sobre o banco de dados ou sobre quaisquer outras transações. \*

**Atomicidade**  
A propriedade de atomicidade garante que as transações sejam atômicas (indivisíveis). A transação será executada totalmente ou não será executada.

**Consistência**  
A propriedade de consistência garante que o banco de dados passará de uma forma consistente para outra forma consistente.

**Isolamento**  
A propriedade de isolamento garante que a transação não será interferida por nenhuma outra transação concorrente.

**Durabilidade**  
A propriedade de durabilidade garante que o que foi salvo, não será mais perdido.

\* Algumas respostas foram retiradas do livro: Sistemas de banco de dados - Ramez Elmasri e Shamkant B. Navathe.
