# Objects and Classes

Ok, now I hope you understand objects. But what are classes then? We often hear classes and objects when talking about OOP. What is the distinction between these?

Classes are nothing but blueprints of objects - imagine that we have a specification that defines how objects need to be created. This becomes the class.

In some ways, classes are nothing but definitions of custom types.

When we say something like:

`int i`

we are essentially saying, i is a variable whose value is of type Integer.

Similarly, when we say something like:

`Person p`

we are saying, p is a variable whose value is of type Person.

Programmer: p is a variable whose value is of type Person.

System: Now wait a minute. I don't know what a Person is. I understand only int, float, String etc.

Now the system needs to know what Person is, because it is not a primitive type (and to begin with the Computer only understands primitive types). This is where a class comes handy and we define what this type Person is.

Programmer: Let me tell you what a Person is.

The programmer then gives the definition of the Person type:

```
class Person
 Name name
 Address address
 PhoneNumber phoneNumber
```

So when we define a class, we are indicating to the language, create a type called "Person". Variables of type Person will have 3 properties - Name, Address and Phonenumber.

System: More confusion. Now what is Name, Address or Phonenumber?

Programmer: Don't worry. Here are their definitions:

```
class Name
 String firstName
 String middleName
 String lastName

class Address
...
```

The type that we define is called the "Class", the variable of this type is called the "Object"s.

Note:

- All the things we just discussed have nothing to do with a specific language. Different languages have different ways to implement "classes/objects".
- In a language like Python, we don't explicitly specify the type of a field