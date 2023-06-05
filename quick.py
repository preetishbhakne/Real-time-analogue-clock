filename=input("Enter file name: ")
for line in reversed(list(open(filename))):
    print(line.rstrip())

    Case
    1:
    Contents
    of
    file:
    hello
    world
    hello

    Output:
    Enter
    file
    name: read.txt
    hello
    hello
    word

    Case
    2:
    Contents
    of
    file:
    line1
    line2
    line3

    Output:
    Enter
    file
    name: read2.txt
    line3
    line2
    line1

