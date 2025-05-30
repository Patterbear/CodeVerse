Let us start with Primitive Types first.

# Primitive Types

Let us first make sure we understand Primitive Datatypes.

Primitive datatypes are the basic types provided by a language. For example, we say that i is an integer, or l is a long variable. These are primitive types.

There are essentially 2 types of primitive types -> numbers and strings. There might be several number types in the language (integers, long, float etc).

We have a way to map primitive types to bits. Integers can be mapped to bits using decimal to binary conversion. Floating point numbers are mapped to bits using double-precision floating point formats. (Don't worry if you don't get it, just remember that integers, floats etc are directly mapped to bits).

Most new languages also have native support for "Strings". Strings are a sequence of characters and we have a way to map every character to bits. This is what ASCII and Unicode are all about. Why do we need UTF8? Because ASCII is only for English characters. So if we want to map characters from Hindi to bits, we need a bigger mapping table (Unicode).

Why do we need 2 primitive types? Why not just make everything as a string? Afterall, I can represent '123' as a string because there is a mapping from every character to bits.

The reason is, if we represent something as numbers, we can use a few special operators on it. For eg: we can add 2 numbers, we can multiply them etc. These are valuable operations which are performed by a computer's processor. These operations cannot be performed unless you use numbers.

More info:

- [http://en.wikipedia.org/wiki/Primitive_data_type](http://en.wikipedia.org/wiki/Primitive_data_type)
- [http://en.wikipedia.org/wiki/Unicode](http://en.wikipedia.org/wiki/Unicode)