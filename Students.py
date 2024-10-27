class Students:
     def __init__(student, name, age, degree):
        student.name = name
        student.age = age
        student.degree = degree
         
s1 = Students("Jonas", 28, "Bachelor")
s2 = Students("Erik", 28, "Bachelor")
s3 = Students("Muhammed", 28, "Bachelor")
s4 = Students("Stefan", 28, "PhD")
s5 = Students("Eline", 28, "Masters")
# skaper en liste av objektene jeg har definert, så det hele kan gåes over.
studentls = [s1, s2, s3, s4, s5]

def studentgroup(inputlist, inpstudent):
    i = 0
    for objects in inputlist:
        if inputlist[i].name == inpstudent:
            return inputlist[i].degree
        elif len(inputlist) == i:
            print("We can't find that student!")
        i += 1