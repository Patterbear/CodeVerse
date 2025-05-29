Computers are really fast "bit processors". As far as computers are concerned, these bits don't have any meaning.

The processing is in the form of an input pattern of bits and an instruction (which is again a bit pattern) to get an output bit pattern. A CPU understands only a specific set of instructions (referred to as its instruction set). Let us say we want to add 2 numbers, 2 and 3.

A human interprets this as 2 + 3 is equal to 5.

A computer looks at this a little differently.

The computer sees the binary representation of the number 2, i.e. `010`, the binary representation of the number 3, i.e. `011` and the instruction `+`. Internally, even the instruction is represented with some binary value, let's say a binary `111`.

What the processor receives are 3 values - the 2 numbers and an instruction.

Input: First number: `010` Second number: `011` Instruction: `111`

It then "processes" these to produce a result. In this case, it produces the binary representation of the number 5, i.e `101`.

Output: `101`

Everything that a computer does can be broken down into one of the instructions in its instruction set and all input data can be converted into binary. Computers are dumb in one sense because they don't really know the difference between playing a movie v/s playing a game. As far as computers are concerned they are only doing Input -> Processing -> Output as described above.

It is now up to us humans to give the input and output bits a "meaning".

For example, when we are watching a movie in our laptop, the data representing the movie (i.e. the audio and video related information) is present as a file in our hard-disk. This file is read into the RAM a portion at a time. The computer then extracts the bits related to the audio and video (this is processing) and this processed data is then sent to the screen and to the speakers. The data is stored in the file as binary, the processing is done as binary and the output is sent to the screen and speakers as binary. When these bits reach the speakers we hear sound! When some bits reach the monitor, we see video! It is we humans who interpret it as audio and video and enjoy the movie!