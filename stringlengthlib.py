Example = "Eksempelet"
Example2 = "Eksempelnummber2"
def mystrlen(*strings):
    i = 0
    result = []
    for string in strings:
        result.append(strlen(strings[i]))
        i += 1
    return result
def strlen(inputstr):
    i = int(0)
    for character in inputstr:
        print(inputstr[i])
        i += 1
    return i

print(mystrlen(Example, Example2))