I have seen quite a few students who define a class as nothing but a struct with functions in it. Then I ask them, if I put a function pointer in a struct, will it become a class?

This definition has two fundamental issues.

First of all, struct is specific to languages like C/C++ and is not universally present in every language. Java, Python for example, don't have the notion of a struct, but both these languages support Objects. Secondly, we are trying to explain the concept of a class using an implementation detail, which is not good.

Understand classes as a concept - about how it helps in reducing code complexity, how classes and objects are used to design systems. As to understanding implementation details of classes and objects - it is specific to languages and should be dealt with separately.