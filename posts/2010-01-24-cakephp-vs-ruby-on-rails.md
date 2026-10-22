---
title: "CakePHP vs Ruby on Rails"
date: 2010-01-24 20:56:30
categories: ["CakePHP"]
tags: ["CakePHP", "has and belongs to many", "php", "ruby", "Ruby on Rails"]
---

O [CakePHP](http://cakephp.org/) é um framework para desenvolvimento rápido de aplicações em PHP. Baseado no Ruby on Rails, segue o paradigma da convenção sobre configuração. Usa design patterns como [MVC](http://pt.wikipedia.org/wiki/MVC) e [ORM](http://pt.wikipedia.org/wiki/Mapeamento_objeto-relacional), reduz os custos de desenvolvimento e ajuda os desenvolvedores a escreverem menos código.

Apesar de ser um bom framework e ser baseado no Rails, a principal diferença que faz o Rails mais vantajoso (fora o nível da comunidade ruby ser maior que o nível da comunidade php) é a própria sintaxe do Ruby em relação ao PHP. Eu particularmente recomendo fortemente o desenvolvimento em PHP utilizando o CakePHP, mas na minha opinião nada supera o Rails.

Abaixo segue um exemplo de uma consulta (inner join) entre dois modelos (Agencia e Cidade que possuem um relacionamento [has\_and\_belongs\_to\_many](http://api.rubyonrails.org/classes/ActiveRecord/Associations/ClassMethods.html#M001836)) para uma consulta em que devem ser listadas as cidades (distintamente) que possuem relacionamento com agências ordenadas pelo nome:

O SQL esperado

Um possível exemplo no CakePHP (no controller agencias)

Um possível exemplo no Ruby on Rails (no controller agencias)

Esse é um exemplo bem simples, porém fica nítido a simplicidade do código, mesmo sem levar em consideração que no Rails bastaria uma linha em cada modelo para definir o relacionamento, enquanto que no Cake seria necessário mais linhas.
