We have learnt how to identify entities in the system. We also know that entities are related in some way.

There are atleast 2 different ways in which entities could be related.

1. An entity or an object can contain another object
2. An entity can be like another object with some differences

The first type of relationship between 2 entities is called Association. Typically, you can identify these types of relationships using a "has-a" phrase. Eg: Car "has-a" Part, Class "has-a" Person, Profile "has-a" Experience.

There are 2 more types of has-a relationship called Aggregation and Composition. Look at more information here: [Association, Aggregation and Composition](http://ootips.org/uml-hasa.html)

My findings:

| Relationship Type | "Has-a" Meaning | Lifespan Dependency   | Example           |
| ----------------- | --------------- | --------------------- | ----------------- |
| Association       | General         | Independent           | Student ↔ Teacher |
| Aggregation       | Loosely owned   | Can be independent    | Library → Books   |
| Composition       | Strongly owned  | Cannot be independent | Human → Heart     |
