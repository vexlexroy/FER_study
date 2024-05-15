# za KR_ZA
# od KR_OD
# do KR_AZ
# ( L_ZAGRADA
# ) D_ZAGRADA
# + OP_PLUS
# - OP_MINUS
# * OP_PUTA
# / OP_DIJELI
# =  OP_PRIDRUZI
# // komentare zanemaruje, idu do kraja redka (continue)
# IDN za identifikatore (varijabla pocinje slovom eng abecede)
# BROJ za konstante (cjeli brojevi paziti na -)

#treba ispisati OZN "broj radak" znak/var

#ucitavanje u listu redaka

import sys

f = sys.stdin
intx= list()
out = []
error=[]
for x in f:
    #print(x)
    intx.append(x.replace("\n"," "))
#print(intx)
line=1

comp={"za" : "KR_ZA",
       "od" : "KR_OD",
         "do" : "KR_DO", 
         "az" : "KR_AZ", 
         "(" : "L_ZAGRADA",
         ")" : "D_ZAGRADA",
         "=" : "OP_PRIDRUZI",
         "+" : "OP_PLUS",
         "-" : "OP_MINUS",
         "*" : "OP_PUTA",
         "/" : "OP_DIJELI",
         }
for x in intx:
    y=x.split(" ")
    for z in y:
        if z in comp:
            text= "{} {} {}".format(comp[z], line, z)
            out.append(text)
        elif z[0:2] == "//":
            break
        elif z.isalnum() and z[0].isalpha():
            text= "IDN {} {}".format(line, z)
            out.append(text)
        elif z.isnumeric():
            text= "BROJ {} {}".format(line, z)
            out.append(text)
        else:
            pom=""
            zc=z.split("//")
            z0=zc[0]
            z0=z0+" "
            for i in range(len(z0)):
                # if (z0[i].isalpha() and i==0) or (z0[i].isalnum() and i != 0):
                #     pom=pom+z0[i]
                # elif (z0[i].isnumeric() and i==0) or (z0[i].isnumeric() and i != 0): 
                #     pom=pom+z0[i]
                if(z0[i].isalnum()):
                    pom=pom+z0[i]
                else:
                    if pom != "":
                        if pom in comp:
                            text= "{} {} {}".format(comp[pom], line, pom)
                            out.append(text)
                        else:
                            if pom[0].isalpha() :
                                text= "IDN {} {}".format(line, pom)
                                out.append(text)
                                pom=""
                            elif pom.isnumeric():
                                text= "BROJ {} {}".format(line, pom)
                                out.append(text)
                                pom=""
                            else:
                                inx=0
                                for l in pom:
                                    if(l.isnumeric()):
                                        inx+=1
                                    else:
                                        break
                                text= "BROJ {} {}".format(line, pom[0:inx])
                                out.append(text)
                                text= "IDN {} {}".format(line, pom[inx:len(pom)])
                                out.append(text)
                                inx=0

                                # text= "ERROR {} {}".format(line, pom)
                                # error.append(text)
                                # pom=""
                        if z0[i] in comp:
                            text= "{} {} {}".format(comp[z0[i]], line, z0[i])
                            out.append(text)
                        else:
                            if z0[i] != " ":
                                text= "ERROR {} {}".format(line, z0[i])
                                error.append(text)
                    else:
                        if z0[i] in comp:
                            text= "{} {} {}".format(comp[z0[i]], line, z0[i])
                            out.append(text)
                        else:
                            text= "ERROR {} {}".format(line, z0[i])
                            error.append(text)
                    
            
    line+=1
for o in out:
     print(o)
# print (error)

