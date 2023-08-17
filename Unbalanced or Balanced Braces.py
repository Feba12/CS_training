#Checking whether the string has balanced or unbalanced braces

open_braces = ['(','{','[']
close_braces = [')','}',']']

def check(string):
    a = []
    for i in string:
        if i in open_braces:
            a.append(i)
        elif i in close_braces:
            pos = close_braces.index(i)
            if (len(a) > 0) and (open_braces[pos] == a [len(a)-1]):
                a.pop()
            else:
                return "Unbalanced"
    if len(a) == 0:
        return "Balanced"
    else:
        return "Unbalanced"



string = input("Enter a string that is a combination of braces: ")
print("String is - ", check(string))
