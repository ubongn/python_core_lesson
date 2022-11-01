def concatenate(*args):
    a=""
    for i in args:
        if a == "":
            a = i
        else :
            a = a +('-'+i)
    return a
print(concatenate("I", "love", "Python", "!"))