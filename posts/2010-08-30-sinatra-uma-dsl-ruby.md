---
title: "Sinatra - Uma DSL Ruby"
date: 2010-08-30 12:37:55
categories: ["Sinatra"]
tags: ["data mapper", "MySQL", "rails", "ruby", "sinatra"]
---

Quem não está muito ligado na comunidade [Ruby](http://www.ruby-lang.org/pt/) talvez só tenha ouvido falar sobre o [Rails](http://www.rubyonrails.pro.br/). É claro que o Rails é o framework mais famoso de Ruby e vem ajudando a alavancar o crescimento da linguagem, porém existem outros frameworks e [DSLs](http://en.wikipedia.org/wiki/Domain-specific_language) em Ruby. Uma DSL muito boa é o [Sinatra](http://www.sinatrarb.com/). O Sinatra é uma DSL para se criar aplicações web de maneira rápida e com o mínimo de esforço. (eu aprendi a utilizá-lo com o [Anderson Leite](http://twitter.com/anderson_leite) da Caelum)

O Sinatra possui algumas diferenças com relação ao Rails como por exemplo, não segue o padrão [MVC](http://pt.wikipedia.org/wiki/MVC). Seu uso é recomendado para resolver problemas pequenos e é realmente bem fácil utilizá-lo.

Vamos supor que você precise fazer algo simples como criar uma listagem qualquer ou qualquer outra coisa simples não compensando o desenvolvimento em Rails. (hoje eu precisei criar um sitemap com alguns dados da minha aplicação, bem simples, algo que não seria necessário agregar ao escopo da minha aplicação Rails).

Antes de começar é necessário instalar o Sinatra

Vou utilizar também o MySQL e o [Data Mapper](http://datamapper.org/) como ORM

Supondo então que quero fazer uma simples consulta em uma tabela posteriormente criada e com dados cadastrados.  
Crie o arquivo *my\_sinatra.rb* com seu editor preferido

Crie também uma pasta chamada *views* e o arquivo *index.erb*

Para startar a aplicação

O Sinatra roda na porta 4567 (<http://localhost:4567/>)  
Repare que as urls são definidas no início do bloco: *get '/' do*...

Para complementar o post, recomendo a leitura:  
<http://www.sinatrarb.com/intro>  
<http://datamapper.org/getting-started>
