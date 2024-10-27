def moonweight(earthweight): # tar input og deler på 6, returnerer resultatet.
    moonweight = earthweight / 6
    return moonweight

numberlist = [-5, 10, 15, 17, 5, -3, 0];
print(numberlist)
def sortie(inputlist):
    i = 0 # iterator, uungåelig i array-arbeid tror jeg :)
    bufferlist = [] # skapte en container her, slipper da å overwrite noe annet. 
    if len(inputlist) != 0: # kutter av funksjonen om input-liste er tom, vil da returnere en tom liste.
        for integer in inputlist: # går bare gjennom integer i input, vil avbryte om den finner strings, men det antar jeg er ok
            if inputlist[i] > 0:
                bufferlist.append("pos")
            elif inputlist[i] < 0:
                bufferlist.append("neg")
            elif inputlist[i] == 0:
                bufferlist.append("zero")
            else: # alltid fint å kunne tåle unntaksfall,
                bufferlist.append("NaN")#fungerer også som en test, siden output vil være NaN
                                        #hvis programmet ikke leser korrekt.
            i += 1
    return bufferlist

stringlist = ["dance", "bee", "defenestration"]
def stringfive(inputlist):
    print(inputlist) # sjekker at listen har blitt lest inn korrekt.
    i = 0
    for string in inputlist:
        if len(inputlist[i]) == 5:
            return True
        i +=1
        
def tentotwenty(inputlist):
    i = 0
    bufferlist = []
    for integer in inputlist:
        if 10 < inputlist[i] < 20:
            bufferlist.append(inputlist[i])
        i += 1
    return bufferlist

# følte beste måten å løse dette på var noen objekter, definerer disse her
class Classroom:
     def __init__(room, name,seats):
         room.name = name
         room.seats = seats
c1 = Classroom("bighall", 150)
c2 = Classroom("lounge", 20)
c3 = Classroom("auditorium", 90)
c4 = Classroom("cafeteria", 450)

# skaper en liste av objektene jeg har definert, så det hele kan gåes over.
classrooms = [c1, c2, c3, c4]
def seatcheck(inputlist, inproom):
    i = 0
    for objects in inputlist:
        if inputlist[i].name == inproom: # hvis noen av objektene matcher navnet til bruker vil seteantallet deres returneres.
            return inputlist[i].seats
        elif len(inputlist) : # hvis ikke får man feilmelding.
            print("sorry, we don't know that room!")
        i +=1
def capchange(inputlist, inproom):
    i = 0
    for objects in inputlist:
        if inputlist[i].name == inproom:
            inputlist[i].seats += 10
            print("the new seating capacity is", end='')
            print(inputlist[i].seats)
        elif len(inputlist) <= i: # sjekker om hele listen er gått gjennom før det skrives ut en feilmelding
            print("sorry, we don't know that room!")
        i +=1

def plusfifty(inputlist):
    i = 0
    bufferlist = []
    for objects in inputlist:
        if inputlist[i].seats >= 50:
            bufferlist.append(inputlist[i].name) # valgte å bruke name-property som output, da bruker eller ville få ut cN, cN+1, etc.
                                                 # upraktisk for praktisk bruk, men gir lesbar output
        elif len(inputlist) <= i:
            print("There are no rooms with more than 50 seats!")
        i += 1
    return bufferlist















