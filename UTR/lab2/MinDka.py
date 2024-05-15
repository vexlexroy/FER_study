# ● 1. redak: Skup stanja odvojenih zarezom, leksikografski poredana.
# ● 2. redak: Skup simbola abecede odvojenih zarezom, leksikografski poredana.
# ● 3. redak: Skup prihvatljivih stanja odvojenih zarezom, leksikografski poredana.
# ● 4. redak: Početno stanje.
# ● 5. redak i svi ostali retci: Funkcija prijelaza u formatu
import sys

def removeUnreachable(grammer):
    pass

def removeSame(grammer):
    pass


intx= list()
f = sys.stdin
for x in f:
    #print(x)
    intx.append(x.replace("\n",""))

allstates=intx[0]
allend=intx[1].split(",")
allacceptable=intx[2].split(",")
start_state=intx[3].split(",")
grammer_dict={}

for i,x in enumerate(intx[5:]):# postavljanje gramatike
    line =  x.split("->")
    key = tuple(line[0].split(","))
    val = tuple(line[1].split(","))
    grammer_dict[key]=val
