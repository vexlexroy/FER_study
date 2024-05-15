
# 1 redak: Ulazni nizovi odvojeni znakom |. Simboli svakog pojedinog niza odvojeni su zarezom.
# 2. redak: Leksikografski poredan skup stanja odvojenih zarezom.
# 3. redak: Leksikografski poredan skup simbola abecede odvojenih zarezom.
# 4. redak: Leksikografski poredan skup prihvatljivih stanja odvojenih zarezom.
# 5. redak: Početno stanje.
# 6. redak i svi ostali retci: Funkcija prijelaza u formatu


import sys


def checkGrammer(grammer, key):
    # print(key)
    tempeps = None
    exitState = []
    exitStatepom=[]
    if(key in grammer):
        exitState = exitState + list(grammer[key])
        exitStatepom = checkEpsilonFirst(grammer, exitState)
        exitState=exitStatepom
        return exitState
    else:
        exitState.append("#")
        return exitState
    
def checkEpsilonFirst(grammer, curr):
    newcurr=curr
    for x in curr:
        key=(x,"$")
        if(key in grammer):
            newcurr = newcurr + list(grammer[key])
            newcurr = list(dict.fromkeys(newcurr))
            newcurr.sort()
    if(newcurr != curr):
        return checkEpsilonFirst(grammer, newcurr)
    else:
        return curr


    
def printRez(out):
    poml = ""
    for i,line in enumerate(out):
        if(line == "|"):
            print(poml[:-1],end="")
            poml=""
            print()
            continue
        for i2,state in enumerate(line):
            if(i2<len(line)-1):
                # print(state,end=",")
                poml=poml+state+","
            else:
                # print(state,end="|")
                poml=poml+state+"|"
            



intx= list()
f = sys.stdin

for x in f:
    #print(x)
    intx.append(x.replace("\n",""))

inmsg=intx[0].split("|")
order_states=intx[1].split(",") # poredak
order_aplha=intx[2].split(",")
order_fin=intx[3].split(",")
current_state = intx[4].split(",")
gramer_dict={}

# stanje,a->b
for i,x in enumerate(intx[5:]):# postavljanje gramatike
    line =  x.split("->")
    key = tuple(line[0].split(","))
    val = tuple(line[1].split(","))
    gramer_dict[key]=val

# print (gramer_dict)
# print("---------------------")

out=[]
for i,x in enumerate(inmsg):
    curr=checkEpsilonFirst(gramer_dict, current_state)
    out.append((curr))
    msg_part=x.split(",")
    for simbol in msg_part:
        nexts = []
        for state in curr:
            fkey = (state, simbol)
            nexts=nexts+checkGrammer(gramer_dict, fkey)
            nexts = list(dict.fromkeys(nexts))
            nexts.sort()
        out.append(nexts)
        curr = nexts
    out.append("|")
    for x in out:
        if("#" in x and len(x)>1):
            x.remove("#")
printRez(out)
        

# print(out)
    



