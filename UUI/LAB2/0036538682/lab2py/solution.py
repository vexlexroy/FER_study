import sys, argparse, re



class Opovrgavanje:
    Rfile=None
    Cfiles=None
    klauze=None
    lastKlaz=None
    newlastKlaz=None
    originalklauze=None
    userActions=None
    lastUklaz=None
    usingKlaz=None
    used_opovrgnute=None
    all_used_klazs=None
    startingKlaz=None

    

    def __init__(self):
       self.klauze=[]
       self.userActions=[]
       self.usingKlaz={}
       self.originalklauze=[]
       self.used_opovrgnute={}
       self.all_used_klazs=set()

    def main(self, arguments):
        parser=argparse.ArgumentParser()
        parser.add_argument("--resolution", nargs="?", help="path to file")
        parser.add_argument("--cooking", nargs=2, help="file paths")
        args= parser.parse_args(arguments)
        # print(args)
        if args.resolution:
            self.Rfile=args.resolution
            self.load(R=True)
            self.Reduce()
            self.checkCombine()
        if args.cooking:
            self.Rfile=args.cooking[0]
            self.Cfiles=args.cooking[1]
            self.load(C=True, R=True)
            self.performUserActions()
        return

    def load(self, R=False, C=False):
        if(R):
            with open(self.Rfile, "r") as r:
                lines:str=r.readlines()
            for linein in lines:
                if(linein.startswith("#")):
                    continue
                line=linein.rstrip("\n")
                self.klauze.append(line.lower().split(" v "))
            self.originalklauze=self.klauze.copy()
            self.lastKlaz=self.klauze.pop()
            x:str
            for x in self.lastKlaz:
                if x.startswith("~"):
                    self.klauze.append([x.lstrip("~")])
                else:
                    self.klauze.append(["~"+x])
            # print(f"load: {self.klauze}")
        if(C):
            with open(self.Cfiles, "r") as r:
                lines:str=r.readlines()
            for linein in lines:
                if(linein.startswith("#")):
                    continue
                line=linein.rstrip("\n")
                self.userActions.append(line.lower().split(" v "))
                pom=self.userActions[-1].pop().split(" ")
                self.userActions[-1].append(pom[0])
                self.userActions[-1].append(pom[1])
            # print(self.userActions)

    # pojednostavljivanje--------------------------------
    def removeDuplicat(self):
        newKlaz=self.klauze
        for i,klaz in enumerate(self.klauze):
            newKlaz[i]=sorted(list(set(klaz)))
        self.klauze=newKlaz
        # print(f"dup: {self.klauze}")
        return
    
    def removeNulify(self):
        newKlaz=self.klauze
        for i,klaz in enumerate(self.klauze):
            for simb in klaz:
                if "~"+simb in klaz:
                    newKlaz.pop(i)
        self.klauze=newKlaz
        # print(f"nul: {self.klauze}")
        return
    
    def Reduce(self):
        self.removeDuplicat()
        self.removeNulify()
        stringKlaz=[]
        removeind=set()
        newKlaz=[]
        for klaz in self.klauze:
            stringKlaz.append(" ".join(klaz)) 
        for i,strK in enumerate(stringKlaz):
            regex_match = fr'(^|\s)(?<!~){re.escape(strK)}($|\s)'
            # print(regex_match)
            patern1 = re.compile(regex_match) 
            for ii in range(len(stringKlaz)):
                if(i != ii and patern1.search(stringKlaz[ii])!=None and i not in removeind):
                    # print(f"(({strK},{i})||({stringKlaz[ii]},{ii}))", patern1.search(stringKlaz[ii]))
                    removeind.add(ii)
        for i,strKlaz in enumerate(stringKlaz):
            if(i not in removeind):
                newKlaz.append(strKlaz.split(" "))
        self.klauze=newKlaz
        # print(f"final: {self.klauze}")
        self.usingKlazfill()
        return
    
    def usingKlazfill(self):
        for i,ent in enumerate(self.klauze):
            self.usingKlaz[i]=tuple(ent)
        # print(self.usingKlaz)
        self.startingKlaz=self.usingKlaz.copy()
        # for x in self.usingKlaz:
        #     strentry= " v ".join(self.usingKlaz[x])
        #     print(f"{x}. {strentry}")
        return
    #--------------------pojednostavljivanje-----------------

    # Cooking -----------------------------------------------
    def loadWith(self, newendklaz):
        self.klauze=self.originalklauze.copy()
        self.lastKlaz=newendklaz
        for x in self.lastKlaz:
                if x.startswith("~"):
                    self.klauze.append([x.lstrip("~")])
                else:
                    self.klauze.append(["~"+x])
        return
        
    def performUserActions(self):
        for action in self.userActions:
            if(action[-1]=="?"):
                ucomand=" v ".join(action[:-1])
                print(f"User’s command: {ucomand} ?")
                self.loadWith(action[:-1])
                self.Reduce()
                self.checkCombine()
            elif(action[-1]=="+"):
                ucomand=" v ".join(action[:-1])
                print(f"User’s command: {ucomand} +")
                self.originalklauze.append(action[:-1])
            elif(action[-1]=="-"):
                ucomand=" v ".join(action[:-1])
                print(f"User’s command: {ucomand} -")
                while True:
                    try:
                        idx=self.originalklauze.index(action[:-1])
                        self.originalklauze.pop(idx)
                    except Exception as e:
                        break
        return
    #  ----------------------Cooking-------------------------

    # Provera opovrgavanjem----------------------------------
    def checkCombine(self):
        used_klaz_combos={}
        last_regular=max(self.usingKlaz.keys())+1
        print("======================================")
        line=0
        while(line <= max(self.usingKlaz.keys())): # iterate over each element
            entry=self.usingKlaz[line]
            for linex  in range(line, -1, -1): # check all behinde combos
                entryx=self.usingKlaz[linex]
                if(self.combinable(entry, entryx)): # check if combinable
                    ch_set=set(self.usingKlaz.values())
                    newentry=self.combine(entry, entryx) # make combo
                    if(tuple(newentry) not in ch_set):
                        newkey=max(self.usingKlaz.keys())+1
                        self.usingKlaz[newkey]=newentry
                        value=" v ".join(self.usingKlaz[newkey])
                        # print(f"{newkey}. {value} ({line},{linex})")
                        used_klaz_combos[newkey]=(value, line, linex)
                        if(value=="NIL"):
                            self.backtrack_print(used_klaz_combos, newkey, line, linex, last_regular)
                            self.printer_for_backtrack()
                            self.conclusion(True)
                            return
            line=line+1
        self.conclusion(False)
        return

    def combinable(self, entry1, entry2):
        for x in entry1:
            for y in entry2:
                if((x=="~"+str(y)) or ("~"+x == str(y))):
                    return True
        return False

    def combine(self, entry1, entry2):
        newentry=set()
        newentry.update(entry1)
        newentry.update(entry2)
        for x in entry1:
            for y in entry2:
                if(x=="~"+y or "~"+x == y):
                    newentry.remove(x)
                    newentry.remove(y)
        if not newentry:
            return ["NIL"]
        return tuple(sorted(newentry))
    
    def conclusion(self, state):
        self.usingKlaz={}
        statemante=" v ".join(self.lastKlaz)
        if(state):
            print(f"[CONCLUSION]: {statemante} is true")
        else:
            print(f"[CONCLUSION]: {statemante} is unknown")
        print()
        return

    def backtrack_print(self, dict_off_claz, current, used1, used2, maxidn):
        try:
            self.used_opovrgnute[maxidn]=None
            self.backtrack_print(dict_off_claz, used1, dict_off_claz[used1][1], dict_off_claz[used1][2], max(self.used_opovrgnute.keys())+1)
            self.backtrack_print(dict_off_claz, used2, dict_off_claz[used2][1], dict_off_claz[used2][2], max(self.used_opovrgnute.keys())+1)
        except Exception as e:
            # print(f"{current}. {dict_off_claz[current][0]} ({used1},{used2})")
            self.all_used_klazs.add(used1)
            self.all_used_klazs.add(used2)
            self.used_opovrgnute[maxidn]=[current,[used1, used2], dict_off_claz[current][0]]
            return
        # print(f"{current}. {dict_off_claz[current][0]} ({used1},{used2})")
        self.all_used_klazs.add(used1)
        self.all_used_klazs.add(used2)
        self.used_opovrgnute[maxidn]=[current,[used1, used2], dict_off_claz[current][0]]
        return
    
    def printer_for_backtrack(self):
        for x in self.startingKlaz:
            strentry= " v ".join(self.startingKlaz[x])
            if(x in self.all_used_klazs):
                print(f"{x}. {strentry}")
        print("===========================================")  
        # print(self.used_opovrgnute)
        sorted_opo={}
        sorted_keys=sorted(self.used_opovrgnute.keys())
        self.used_opovrgnute=dict(sorted(self.used_opovrgnute.items(), reverse=True))

        for i,z in enumerate(self.used_opovrgnute):
            sorted_opo[sorted_keys[i]]=self.used_opovrgnute[z]
        self.used_opovrgnute=sorted_opo


        for val in self.used_opovrgnute:
            replace_key=self.used_opovrgnute[val][0]
            self.used_opovrgnute[val][0]=val
            for next in self.used_opovrgnute:
                if(replace_key in self.used_opovrgnute[next][1]):
                    index=self.used_opovrgnute[next][1].index(replace_key)
                    self.used_opovrgnute[next][1][index]=val   
        for x in self.used_opovrgnute:
            values=self.used_opovrgnute[x]
            print(f"{x}. {values[2]} ({values[1][0]},{values[1][1]})")
        self.used_opovrgnute={}
        return

    # ---------------Provera opovrgavanjem-------------------



if __name__== "__main__":
    x=Opovrgavanje()
    arguments=sys.argv[1:]
    for i,z in enumerate(arguments):
        if(z == "cooking" or z == "resolution"):
            arguments[i]="--"+arguments[i]
    x.main(arguments)
        