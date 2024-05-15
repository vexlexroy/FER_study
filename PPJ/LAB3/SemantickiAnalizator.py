
import sys


def removeShalow(defined, depth): # removes al variables with greate depth
    x = {key: value for key, value in defined.items() if key[1] <= depth}
    # print("remove")
    # print(x)
    return x

def isDefined(defined, depth, name): # 
    if(depth > 0):
        for i in range(0,depth+1):
            if((name, depth-i) in defined):
                return True
        return False
    else:
        return (name, depth) in defined
    
def getLowest(defined, depth, name):
    rez = [False]
    if(depth >0):
        for i in range(0,depth+1):
            if((name, depth-i) in defined):
                rez = defined[(name, depth-i)]
                if(defined[(name, depth-i)][1] == 2):
                    return rez
    return rez
    
    
def getDefined(defined, depth, name, line, from_state):
    rez = None
    if(depth >0):
        for i in range(0,depth+1):
            if((name, depth-i) in defined):
                if(defined[(name, depth-i)][0] == line):
                    if(defined[(name, depth-i)][1]==2):
                       return False
                    else:
                        continue
                else:
                    return getLowest(defined, depth, name)[0]
        return False
    else:
        if(defined[(name, depth)][0] == line):
            return False
        else:
            return defined[(name, depth)][0]
    



f = sys.stdin
intx= list()
out = []
dataLines = []
blockDepth=0
for x in f:
    intx.append(x.replace("\n","").lstrip())
#print(intx)

for i, x in enumerate(intx[1:], start=1):
    line = x.split(" ")
    data=[]
    if("KR_ZA" in line):
        blockDepth+=1
    elif("KR_AZ" in line):
        blockDepth-=1
    elif("IDN" in line):
        if("<naredba_pridruzivanja>" in intx[i-1]):
            data.append(1)
        elif("KR_ZA" in intx[i-1].split(" ")):
            data.append(2)
        else:
            data.append(0)
        data.append(int(line[1]))
        data.append(line[2])
        data.append(blockDepth)
        dataLines.append(data)
# print(dataLines)
# print("_________________________________________________")

defined = {}
lastDp = None
for x in dataLines:#[def, line, name, depth]
    curdDp = x[3]
    if(x[0] > 0 and (x[2],curdDp) not in defined):
        defined[(x[2],curdDp)] = (x[1], x[0])
    elif(x[0] > 0 and (x[2],curdDp) in defined):
        continue
    elif(x[0] == 0):
        # print("*")
        # print(isDefined(defined, curdDp, x[2]))
        # print(defined, curdDp, x[2])
        # print("*")
        if(isDefined(defined, curdDp, x[2]) and getDefined(defined, curdDp, x[2], x[1], x[0]) != False ):
            out.append("{} {} {}".format(x[1], getDefined(defined, curdDp, x[2], x[1], x[0]), x[2]))
        else:
            out.append("err {} {}".format(x[1],x[2]))
            break 
    defined = removeShalow(defined, curdDp) # mice sve koj su plici
    # print(defined, curdDp) 
    # print("----------------------------------")
for x in out:
    print(x)







        


