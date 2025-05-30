# List of lists, List of maps, Map of maps

If you remember the examples on top, they are all maps:

```
person = {
	"name": {
		"first_name": "Gautham", "middle_name": "B", "last_name": "Pai" },
        "phone_number": {
	        "area_code": "080", "subscriber_number": "1234567890"
	    },
	    "address": {
		    "house_no" : "123/A", "main": "10a", "cross": "9", "city": "Bangalore", "pincode": 560038
		}
}
```

person is a map of 3 key/value pairs, where the first key value pair is:

```
Key: "name"
Value: { "first_name": "Gautham", "middle_name": "B", "last_name": "Pai" }
```

Now here is an interesting thing to note. The value is another map. This map has 3 key value pairs in them.

So what we understand is that maps can contain maps. Maps can similarly contain lists. Lists can contain maps etc.

Some examples:

`List of lists: [ 1, 2, [3, 4] ]`

The outer list has 3 items: 1, 2 and another list [3, 4].

`List of maps: [ {"name": "Deepak"}, {"name": "Gautham"}, {"name": "Kiran"} ]`

The list contains 3 maps. Each map has a key called name and different values.

Map of maps (The same example as above of person).

There is virtually no limit to how you combine these.

# More examples

Suppose I ask you to list the number of medals that each country has won in the Olympics and also tell me how many medals has it won in each category, then your map will look somewhat like this:

`{'India': {'gold': 0, 'silver': 3, 'bronze': 2}}`

See the map of maps?