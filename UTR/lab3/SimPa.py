# ● 1 redak: Ulazni nizovi odvojeni znakom |. Simboli svakog pojedinog niza odvojeni su
# zarezom.
# ● 2. redak: Skup stanja odvojenih zarezom
# ● 3. redak: Skup ulaznih znakova odvojenih zarezom
# ● 4. redak: Skup znakova stoga odvojenih zarezom
# ● 5. redak: Skup prihvatljivih stanja odvojenih zarezom
# ● 6. redak: Početno stanje
# ● 7. redak: Početni znak stoga
# ● 8. redak i svi ostali retci: Funkcija prijelaza u formatu



import sys


def checkGrammer(grammer, key, stog, last, acpt):
    rez=""
    newstog=""
    newstate=""
    if(key in grammer):
        newstate=grammer[key][0]
        if(grammer[key][1]=="$" and stog!="$"):
            newstog=stog[1:]
        elif(grammer[key][1]=="$" and stog=="$"):
            newstog=stog
        elif(grammer[key][1]!="$" and stog=="$"):
            newstog=grammer[key][1]+stog
        elif(grammer[key][1]!="$" and stog!="$"):
            newstog=grammer[key][1]+stog[1:]
        if(len(newstog)>1):
            pnewstog=newstog[:-1]
        else:
            pnewstog=newstog
        rez = rez + str(newstate + "#" + pnewstog + "|")
        if(last and rez.split("|")[-2].split("#")[0] in acpt):
            return newstog, newstate, rez
        epsrez, newstog, newstate=checkEpsilonFirst(grammer,newstate,newstog, last, acpt)
        if(len(epsrez)>0):
            rez = rez + epsrez
        return newstog, newstate, rez
    else:
        rez = rez + "fail|"
        return None, None, rez

    
def checkEpsilonFirst(grammer, curr, stog, last, acpt):
    rez=""
    newstog=stog
    newstate=curr
    fkey=(curr,"$",stog[0])

    if(fkey in grammer):
        # print(fkey)
        # print(grammer[fkey])
        if(grammer[fkey][1]=="$" and stog!="$"):
            newstog=stog[1:]
        elif(grammer[fkey][1]=="$" and stog=="$"):
            newstog=stog
        elif(grammer[fkey][1]!="$" and stog=="$"):
            newstog=grammer[fkey][1]+stog
        elif(grammer[fkey][1]!="$" and stog!="$"):
            newstog=grammer[fkey][1]+stog[1:]

        newstate=grammer[fkey][0]
        if(len(newstog)>1):
            pnewstog=newstog[:-1]
        else:
            pnewstog=newstog
        rez = rez + str(newstate + "#" + pnewstog + "|")
        if(last and rez.split("|")[-2].split("#")[0] in acpt):
            return rez, newstog, newstate
        nrez, newstog, newstate = checkEpsilonFirst(grammer, newstate, newstog, last, acpt)
        return rez + nrez, newstog, newstate
    else:
        return rez, newstog, newstate

def printRez(out, aceptable):
    for i, val in enumerate(out[1:], start=1):
        if(val!="||"):
            if(out[i-1]=="||"):
                continue
            print(out[i-1],end="")
        else:
            last = out[i-1].split("|")[-2].split("#")[0]
            if(last in aceptable):
                print(out[i-1],end="1\n")
            else:
                print(out[i-1],end="0\n")
                if(last == "fail"):
                    continue


intx= list()
f = sys.stdin
for x in f:
    #print(x)
    intx.append(x.replace("\n",""))

inmsg=intx[0].split("|")
states=intx[1].split(",")
incar=intx[2].split(",")
stogcar=intx[3].split(",")
acceptablecar=intx[4].split(",")
startstate=intx[5]
startstog=intx[6]

grammer_dict={}
for i,x in enumerate(intx[7:]):# postavljanje gramatike
    line =  x.split("->")
    key = tuple(line[0].split(",")) # (stanje, dobiveni, stog)
    val = tuple(line[1].split(","))
    grammer_dict[key]=val
# print (grammer_dict)
# print("--------------------------------")


out=[]
for i,msgs in enumerate(inmsg):# all msgs
    last=False
    stog=startstog+"$"
    out.append(str(startstate+"#"+stog[:-1]+"|"))
    eps,stog,currstate=checkEpsilonFirst(grammer_dict, startstate, stog, last, acceptablecar)
    out.append(eps)
    for i,msg in enumerate(msgs.split(",")):
        if(len(msg)-1==i):
            last=True
        fkey=(currstate, msg, stog[0])
        # print(fkey)
        stog, currstate, outpt = checkGrammer(grammer_dict, fkey, stog, last, acceptablecar)
        # print("stog: {}, out {}".format(stog,outpt))
        out.append(outpt)
        if(outpt == "fail|"):
            break
    out.append("||")
printRez(out, acceptablecar)


