# #----------excel data---------
import pandas as pd # laster in pandas
import altair as alt # laster in altair 
#Reading the Excel file
kgdata = pd.read_excel('ssb-barnehager-2015-2023-alder-1-2-aar.xlsm', sheet_name='KOSandel120000',
                       header=3,
                       names=['kom', 'y15', 'y16', 'y17', 'y18', 'y19', 'y20', 'y21', 'y22', 'y23'],
                       na_values=['.', '..'],
                       skipfooter=56
                       )
def toppgjennomsnitt():
    oppned = kgdata.sort_values(by=['y23'], ascending=False) # har valgt å sortere først, gjør det rimelig
    #enkelt å ta høyde for flere like topp-verdier.
    highest = 0
    i = 0
    while i < len(oppned):
        if kgdata.y23[i] >= highest: # Har for øvrig heller ikke kuttet bort outliers, statistikk er statistikk.
            highest = kgdata.y23[i] # om jeg skulle gjort det hadde jeg lagt til "and 40 < highest <= 100"
        i +=1
    print("topgjennomsnitt end")
    topkommunes = findkommune(highest)
    return topkommunes, int(highest)

def bunngjennomsnitt():
    templs = kgdata.y23
    lowest = min(templs)
    print("bunngjennomsnitt end")
    botkommunes = findkommune(lowest) # kaller funksjon
                                      # som finner navn på kommune med lavest gjennomsnitt.
    return botkommunes, int(lowest)
def findkommune(input):
    print("findkommune run")
    i = 0
    bufferlist = []
    while i < len(kgdata):
        if input == kgdata.y23[i]: # tar høyde for flere ekstremverdier ved å
                                    #finne like verdier som topp eller bunntall
            bufferlist.append(kgdata.kom[i]) # og så legge disse i buffert.
        i+=1
    return bufferlist
def averages(topbot):
    kommuneaverages = kgdata.iloc[:, 1:9].mean(axis=1)
    print(kommuneaverages) # tester at gjenomsnittene regnes ut korrekt.
    output = 0
    if topbot == "top":
        output = max(kommuneaverages)
        outputname = findnameaverage(output, kommuneaverages)
    elif topbot == "bot":
        output = min(kommuneaverages)
        outputname = findnameaverage(output, kommuneaverages)
    return outputname, output
def findnameaverage(inputint, inputls):
    i = 0
    for integer in inputls:
        if inputint == inputls[i]:
            return kgdata.kom[i]
        i+=1
def yearaverage():
    averagey18 = kgdata.y18.mean(axis=0) # setter her average y18 til å finne gjennomsnittet av kolonnen y18.
    return int(averagey18) # returnerer resultat.
def drawchart(): # thonny viser ikke diagrammet, desverre, så jeg får ikke testet om koden
    alt.Chart(kgdata).mark_bar().encode(
            x='0301 Oslo',
            y='y15, y16, y17, y18, y19, y20, y21, y22, y23'
        )
def drawaveragechart():
    kommuneaverages = kgdata.iloc[:, 1:9].mean(axis=1)
    alt.Chart(kgdata).mark_bar().encode(x='0301 Oslo',y='')
def testrun():
    testls = []
    testls.extend(kgdata.loc[kgdata])
    print(testls)
    
    