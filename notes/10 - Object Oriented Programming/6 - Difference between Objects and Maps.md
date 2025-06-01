# Difference between Objects and Maps

Now, in a different place, we had represented person using a map as follows:

```
person = {
	"name": {
		"first_name": "Gautham",
		"middle_name": "B",
		"last_name": "Pai"
	},
    "phone_number": {
	    "area_code": "080",
	    "subscriber_number": "1234567890"
	},
    "address": {
	    "house_no" : "123/A",
	    "main": "10a",
	    "cross": "9",
	    "city": "Bangalore",
	    "pincode": 560038
    }
}
```


Are these different? Well, yes and no.

There are 2 major differences between the 2:

- When you create classes and objects of that class, the way the memory is allocated to store the fields in the object may be packed next to each other. (This is what you may have learned as 'struct's in C).
- A second difference is about being able to extend the definition. If I define a class called Person and say that it has 3 properties, Name, Address and PhoneNumber, I won't be able to change this definition at run-time. On the other hand, if I define this as a map, I can always add more properties to the object. For eg: I can say, `person['email'] = someone@example.com`, while I may not be able to do it if I had defined it as a class.

So you use a class when you know the structure before-hand. If you expect that there are properties of the object that could be defined at runtime, it's better to go with a map.