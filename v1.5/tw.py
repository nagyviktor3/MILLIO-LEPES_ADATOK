import datetime

now = datetime.datetime.now()
print()

x=int(input("SZÁM: "))
b12=int(input("A 12B oszály: "))
a11=int(input("AZ 11A oszály: "))
a10=int(input("AZ 10A oszály: "))
a9=int(input("AZ 9A oszály: "))

szam10=13
def szokez(osztaly,valtozo):
    global szam10
    egesz_szam=szam10-len(osztaly)
    space="="
    for i in range(egesz_szam):
        space+="="
    valtozo=(int(round(x*(valtozo/100),-1)))/1000
    
    egesz=str(osztaly)+space+str(valtozo)+"K"
    return egesz
        
    
with open("deletet.txt", "a",encoding="utf-8") as f:
    f.write("Összes lépés==")
    f.write(f"{x:_}")
    f.write('\n')
    f.write(szokez("12B",b12))
    f.write('\n')
    f.write(szokez("11A",a11))
    f.write('\n')
    f.write(szokez("10A",a10))
    f.write('\n')
    f.write(szokez("9A",a9))
    f.write('\n')
    f.write(now.strftime("%B"))
    f.write(' ')
    f.write(now.strftime("%d"))
    f.write('\n')
    f.write('\n')
    f.write('\n')
    # kiiras="12B"+szokez(a)+str(x*(b12/100))
    