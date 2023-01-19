for i in range(0,1000):
    string = "{0} {1}".format(chr(i), '\n' if i % 50 == 0 else '    |   ')
    print(string, end="")