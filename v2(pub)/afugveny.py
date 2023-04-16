data = {}
import datetime

now = datetime.datetime.now()

x1=True
x2=True
x3=True
x4=True
x5=True
szazalekk=0
szazalek_x1=0
szazalek_x2=0
szazalek_x3=0
szazalek_x4=0
all_line=0
count=0

def add(name, age):
    global data
    data[name] = age
    return data

def szazalek(szam1,szam2):
    global szazalekk
    szam=(int(szam1))/100
    szazalekk=str(round(int(szam2)/szam)-100)+"%"
    return szazalekk

def all_linef():
    global all_line,count
    count=len(all_line)-18

with open("deletet.txt","r",encoding="utf-8") as r:
    all_line=r.readlines()
    all_linef()
with open("deletet.txt","r",encoding="utf-8") as r:
    sor=r.readline()

    for i in range(count-1):
        sor=r.readline()

    sor=r.readline()

    while sor:
        word=sor.split("=")
        #1
        if "Összes lépés"==word[0]:
            if x1:    
                add("x1",str(word[2])[:-1])
                x1=False
            else:
                add("x10",str(word[2])[:-1])
        
        #2
        if "12B"==word[0]:
            if x2:    
                add("x2",str(word[11])[:-2])
                x2=False
            else:
                add("x20",str(word[11])[:-2])

        #3
        if "11A"==word[0]:
            if x3:    
                add("x3",str(word[11])[:-2])
                x3=False
            else:
                add("x30",str(word[11])[:-2])

        #4
        if "10A"==word[0]:
            if x4:    
                add("x4",str(word[11])[:-2])
                x4=False
            else:
                add("x40",str(word[11])[:-2])
        
        #5
        if "9A"==word[0]:
            if x5:    
                add("x5",str(word[12])[:-2])
                x5=False
            else:
                add("x50",str(word[12])[:-2])
        sor=r.readline()

print(data)

valtozo1=str(int(data["x10"])-int(data["x1"]))+"K"
valtozo2=str(int(data["x20"])-int(data["x2"]))+"K"
valtozo3=str(int(data["x30"])-int(data["x3"]))+"K"
valtozo4=str(int(data["x40"])-int(data["x4"]))+"K"
valtozo5=str(int(data["x50"])-int(data["x5"]))+"K"

szazalek_x1=szazalek(data['x1'],data["x10"])
print("AZ eredmények: ",szazalek_x1,"   növekedés: ", valtozo1)
szazalek_x2=szazalek(data['x2'],data["x20"])
print("12B: ",szazalek_x2,"   növekedés: ", valtozo2)
szazalek_x3=szazalek(data['x3'],data["x30"])
print("11A: ",szazalek_x3,"   növekedés: ", valtozo3)
szazalek_x4=szazalek(data['x4'],data["x40"])
print("10A: ",szazalek_x4,"   növekedés: ", valtozo4)
szazalek_x5=szazalek(data['x5'],data["x50"])
print("9A : ",szazalek_x5,"   növekedés: ", valtozo5)
print()
print("TO THE TOP! ->",int(data["x20"])-int(data["x40"]),"K")
def kiiras():
    with open('aoutput.txt', 'a',encoding="utf-8") as f:
        f.write('\n')
        f.write('\n')
        f.write('\n')
        szazalek_x1=szazalek(data['x1'],data["x10"])
        f.write("AZ eredmények: " + str(szazalek_x1) + "   növekedés: " + str(valtozo1) + "\n")
        szazalek_x2=szazalek(data['x2'],data["x20"])
        f.write("12B: " + str(szazalek_x2) + "   növekedés: " + str(valtozo2) + "\n")
        szazalek_x3=szazalek(data['x3'],data["x30"])
        f.write("11A: " + str(szazalek_x3) + "   növekedés: " + str(valtozo3) + "\n")
        szazalek_x4=szazalek(data['x4'],data["x40"])
        f.write("10A: " + str(szazalek_x4) + "   növekedés: " + str(valtozo4) + "\n")
        szazalek_x5=szazalek(data['x5'],data["x50"])
        f.write("9A : " + str(szazalek_x5) + "   növekedés: " + str(valtozo5) + "\n")
        f.write("\nTO THE TOP! ->" + str(int(data["x20"])-int(data["x40"])) + "K\n")
        f.write("("+now.strftime("%B"))
        f.write(' ')
        f.write(now.strftime("%d")+")")
















def szokez(valtozo):
    global data
    szam10=5
    egesz_szam=szam10-len(data[valtozo])
    space=" "
    for i in range(egesz_szam):
        space+=" "
    valtozo=int(data[str(valtozo)[:-1]])-int(data[valtozo])
    
    egesz=space+"+"+str(valtozo)
    return egesz

    # word[2]


    # sor=r.readline()
    # while sor:
    #     word=sor.split("=")
    #     print(word)
    #     sor=r.readline()