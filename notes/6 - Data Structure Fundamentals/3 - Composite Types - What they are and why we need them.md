# Composite Types

The world is really complex. If the world was made up of only numbers and strings, we wouldn't need special types. But unfortunately that is not the case. Primitive datatypes are not sufficient to represent all the complexity of the world. So we need "composite types". Composite types are nothing but a "bag" of values put together.

Let us look at an example:

Suppose I want to describe the name of a person. The name of a person can be represented using a "String" datatype. But then, it is composed of 3 distinct values: The "first name", the "middle name" and the "last name". Each of these - the "first name", "middle name" and "last name" are also "Strings" and we want to identify them separately. So we can think of the name being a composite type of these 3 primitive types.

Let us look at a way to represent this:

```
first_name = "Gautham"
middle_name = "B"
last_name = "Pai"
```

Now how do we represent a name as a combination of these?

Let us look at one way to describe it:

```
name = { "first_name": "Gautham", "middle_name": "B", "last_name": "Pai" }
```

What we are saying is that the name is a combination of 3 primitive types - first_name, middle_name and last_name. These types are all Strings and have values, "Gautham", "B" and "Pai" respectively.

More examples:

```
phone_number = { "area_code": "080", "subscriber_number": "1234567890" }
address = { "house_no" : "123/A", "main": "10a", "cross": "9", "city": "Bangalore", "pincode": 560038 }
```

Ok. Just to be clear, name, phone_number and address are all composite types. We can now create more composite types using these.

For example a person comprises of name, phone_number and address. So we can represent a person as:

```
person = {
	"name": {
		"first_name": "Gautham", "middle_name": "B", "last_name": "Pai"
	},
    "phone_number": {
	    "area_code": "080", "subscriber_number": "1234567890"
	},
    "address": {
	    "house_no" : "123/A", "main": "10a", "cross": "9", "city": "Bangalore", "pincode": 560038
	}
}
```

This is how you can combine primitive types to create more and more complex types.

More info:

- [http://en.wikipedia.org/wiki/Composite_type](http://en.wikipedia.org/wiki/Composite_type)

Just to be clear, what we are learning now has nothing to do with any specific language. We can create these custom types in any language - be it Python, Java or C. But the way we do it in different languages is different.

When we create these composite types, there are some patterns which emerge in how we group items together. Composite types are sometimes called collections.

There are 3 types of collections: Lists, Maps and Sets.