# Remove all the spaces from the given string

def remove_space(s):
    ls = s.split()
    result = ""
    for i in ls:
        if i != " ":
            result += i
    print(result)


# Input
s = str(input("Enter a string: "))
remove_space(s)
