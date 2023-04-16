all_line=0
count=0
talalat=True
data={}

x1=True
x2=True
x3=True
x4=True
x5=True

def all_linef():
    global all_line,count
    count=len(all_line)-18

def add(name, age):
    global data
    data[name] = age
    return data

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
        
#4197439
    valtozo1=str(int(data["x10"][:-1])-int(data["x1"][:-1]))
    valtozo2=str(int(data["x20"][:-1])-int(data["x2"][:-1]))
    valtozo3=str(int(data["x30"][:-1])-int(data["x3"][:-1]))
    valtozo4=str(int(data["x40"][:-1])-int(data["x4"][:-1]))
    valtozo5=str(int(data["x50"][:-1])-int(data["x5"][:-1]))