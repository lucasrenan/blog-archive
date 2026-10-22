---
title: "Bugs que o sistema apresentou no fim do sprint"
date: 2011-02-27 16:48:49
categories: ["Desenvolvimento Ágil"]
tags: ["desenvolvimento ágil", "Ruby on Rails", "scrum"]
---

Ano passado meu último post foi ["Erros que cometi nesse sprint"](http://www.p3m.com.br/blog/erros-que-cometi-nesse-sprint/), tratava-se de alguns erros que tinha cometido em um projeto, principalmente por não ouvir as pessoas. Outra vez vou contar um pouco da experiência que eu tive e que está totalmente relacionada aos [princípios ágeis](http://pt.wikipedia.org/wiki/Desenvolvimento_%C3%A1gil_de_software).

A grosso modo, o princípio básico das metodologias ágeis de desenvolvimento de software é: **entregar software de qualidade e funcional o mais rápido possível para garantir o ROI (retorno sobre investimento)**. Esse é um assunto que já se tornou clichê no mundo do desenvolvimento de software, porém no dia a dia de um projeto seguir esse princípio não é tão fácil como parece. Então, seguindo essa linha de pensamento, quando vamos iniciar um sprint devemos priorizar quais tarefas serão executadas primeiro afim de entregar o quanto antes as funcionalidades que tem mais valor (ROI).

Muitas vezes o objetivo principal do projeto não fica claro em um primeiro momento, no caso o projeto tratava-se de um loja virtual de cursos, porém esse conceito só ficou realmente claro para a equipe depois que o projeto foi "finalizado". Isso foi um grande problema, eu particularmente acabei me concentrando em vários detalhes que não estavam diretamente relacionados com o objetivo principal, ou seja, o usuário poder comprar e se matricular em um curso.

Depois do "fim" do projeto foram encontrados vários bugzinhos no sistema e várias coisas que não tinham sido implementadas ou que poderiam ser melhoradas. Eu fiquei encarregado de arrumar esses bugs para então o site ser finalmente concluído e entrar em produção. No fim da segunda semana que estava arrumando os erros percebemos que o processo de compra de um curso simplesmente não estava funcionando...

**É aí que PAGAMOS O PREÇO por NÃO ser ÁGEIS**

Não entregamos software funcionando incrementalmente, fizemos incrementalmente, mas não entregamos, dessa forma é muito mais difícil descobrir bugs e possíveis mudanças. Adiar mudanças significa aumentar o custo delas. E o pior é entregar software que não cumpre com seu principal objetivo.

Se o software apresenta muitos bugs e precisa de muitas correções, você estará perdendo dinheiro, afinal o cliente não vai pagar para arrumar erros de desenvolvimento.

Poderíamos ficar procurando N motivos para dizer o porque cometemos erros (acharíamos vários e achamos), principalmente pelo projeto ser de escopo fechado, mas era melhor salvar o projeto, não acha? =p

**Salve o projeto, seja ÁGIL**

Utilizando três técnicas ágeis, conseguimos em poucos dias, corrigir os bugs e tornar o sistema totalmente funcional.

- Testes Automatizados  
- Programação em Par  
- Refatoração

O sistema tinha/tem testes automatizados, isso nos proporcionou fazer uma refatoração no código programando em par, com a segurança de que não iríamos quebrar outras partes do sistema. Dessa forma conseguimos rapidamente corrigir os bugs e o processo de compra, tornando o sistema totalmente funcional.

E você? está utilizando desenvolvimento ágil nos seus projetos?
