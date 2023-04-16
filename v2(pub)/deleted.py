import datetime

now = datetime.datetime.now()

x=int(input("SZÁM: "))
print("A következőket százaléban kell megadni!!(%)")
b12=int(input("12B:"))
a11=int(input("11A: "))
a10=int(input("10A: "))
a9=int(input("9A : "))

szam10=13
def szokez(osztaly,valtozo):
    global szam10
    egesz_szam=szam10-len(osztaly)
    space="="
    for i in range(egesz_szam):
        space+="="
    valtozo=(int(str(int(round(x*(valtozo/100),-3)))[:-3]))
    
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
import afugveny
afugveny.kiiras()