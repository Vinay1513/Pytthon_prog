#WAP to print all the ASCII values from a given  character range

a='A'
b='Z'



for i in range(ord(a),ord(b)):
    print("ASCII value of ",chr(i),"is",i)
