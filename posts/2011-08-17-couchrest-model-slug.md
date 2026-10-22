---
title: "CouchRest Model Slug"
date: 2011-08-17 14:42:55
categories: ["Couchrest Model Slug"]
tags: ["CouchDB", "couchrest model", "couchrest model slug", "ruby", "Ruby on Rails"]
---

This is the first time that I blog in english, so please correct me if I write something wrong. Suggestions are welcome too =)

[CouchDB](http://couchdb.apache.org/ "CouchDB") automatically generates [UUIDs](http://en.wikipedia.org/wiki/Universally_unique_identifier "uuid") if none are provided. Usually, it's recommended because some things like replication. However, we can do better for users. UUIDs are ugly, then we can create friendly urls.  
[CouchRest Model Slug](https://github.com/lucasrenan/couchrest-model-slug "CouchRest Model Slug") is a simple gem to generate better urls using [CouchRest Model](https://github.com/couchrest/couchrest_model "CouchRest Model") in an easy way. I created this gem based on [Mongoid Slug](https://github.com/hakanensari/mongoid-slug "Mongoid Slug").

Getting Started

Add to Gemfile

A simple example

Querying

CouchRest Model Slug was made to work with or without slugged value, then it uses the id to keep things running with no problems.

See the github page for more information [https://github.com/lucasrenan/couchrest-model-slug](https://github.com/lucasrenan/couchrest-model-slug "CouchRest Model Slug")
