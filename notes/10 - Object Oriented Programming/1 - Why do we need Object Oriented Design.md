We have seen examples of representation of Primitive and Custom datatypes. We saw how a Person can be thought of as a combination of (Name, Address and PhoneNo). The human mind is good at thinking about these 'entities' or 'things'. This leads us to object oriented design.

# Why do we need Object Oriented Design?

When working on large software projects, the key thing that we need to know is, how can I deal with the system's complexity?

We already saw how we can have functions and libraries to manage complexity. But the obvious question to ask is, what if I have lots of functions, and lots of libraries?

We need other ways to deal with this complexity. Ideally, we need a solution that works no matter how complex the system. One such way is to use Object Oriented Paradigm (OO paradigm).

In order to understand the OO paradigm, let's take an example. You have to explain what GMail is to your neighbour who is not very tech-savvy. How would you explain it?

You would perhaps describe it as a way to send "Mails". There is an "Inbox" which has mails in it. You can "send" a mail, people can "send" a mail to you and you "receive" it.

In other words, you are picking entities or things or nouns that you see and describing them. You are then also describing the behavior associated with these entities.

Object oriented design is about that - about defining properties and behaviour of entities, about [encapsulating](http://en.wikipedia.org/wiki/Encapsulation_\(object-oriented_programming\)) behaviour within entities.

In Object Oriented Paradigm, we see the world in terms of objects. Each object has very distinct properties and exhibits behaviour.

But you may still think - why go with Objects? Why not just lists/maps/sets? We have seen that primitive types and collections are enough to represent anything in the real world. Isn't this sufficient? Why objects then?

The reason follows a similar explanation as to why we need functions and modules. Functions help to reduce complexity, but then after a point, we have too many functions, so we decide to group functions together into modules. Soon, you have a lot of modules. How about thinking about this problem in a slightly different way?

How do we comprehend complexity in the real world? On your way to office today, you perhaps saw many things today. You came across, literally, hundreds of objects and yet, you didn't think of it as complex. Why? Because your brain can comprehend that complexity by identifying "things".

So what you are doing in OO design is trying to comprehend the complexity by identifying entities and their behaviour because your brain works with them better. It becomes tough to do this when you are using only lists, sets and maps, because lists, sets and maps are generic containers and don't have meaning associated with it.