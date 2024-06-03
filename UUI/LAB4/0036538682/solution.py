import sys
import argparse
import numpy as np
from numpy import random
import random as rng

class NeuralNet:
    layers=None # layer : weights(np array)
    arcitecture:str
    inParams:int
    outParams:int
    local_fit:float = None
    fit:float = None
    count:str = '0'
    def __init__(self, id, architecture:str=None, inparm:int=None, outparm:int=None, existingweights:dict=None):
        self.count=str(int(self.count)+1+id)
        if (existingweights==None):
            self.layers={}
            self.arcitecture=architecture
            self.inParams=inparm
            self.outParams=outparm
            arc=(str(self.inParams)+'s'+architecture+str(self.outParams)).split('s')
            # print(architecture.split("s"))
            # print(arc)
            for i,x in enumerate(arc[1:]):
                # print(i, " ", x)
                self.layers[i]=random.uniform(low=-100, high=100, size=(int(arc[i]), int(x)))
        else:
            self.layers=existingweights.copy()
            self.inParams=inparm
            self.outParams=outparm
            self.count=id
            pass
        return
    
    def __str__(self):
        return(f"NeuroNet {self.count}  fit: {self.fit}  weights: {self.layers}")
    def fit__str(self):
        return(f"NeuroNet {self.count}  fit: {self.fit}")
    
    def set_fit(self, fitnes:float):
        self.fit=fitnes
        return
    
    def get_fit(self):
        return self.fit
    
    def sigmoid_finction(self, xexp):
        return 1/(1 + np.exp(xexp))
    
    def calculate_resault(self, input:np.array):
        out=input
        for i,x in enumerate(self.layers):
            if(i<len(self.layers)-1):
                out=self.sigmoid_finction(np.dot(out,self.layers[x]))
            else:
                out=np.dot(out,self.layers[x])
        self.fit=None
        # print(self,"out: ",out)
        return out
    
    def local_fitnes(self, resault:np.array, test_val:np.array):
        ret=((resault-test_val)**2)
        # print(ret)
        return ret
        


class Genetika:
    index=0
    populacija:list
    train_set:list
    test_set:list
    nn:str
    popsize:int
    elitism:int
    mut_prob:float
    noise:float
    iterate:int
    def __init__(self, train_set:list, test_set:list, nn:str, pops:int, elit:int, p:float, K:float, itr:int):
        random.seed()
        self.populacija=[]
        self.train_set=train_set
        self.test_set=test_set
        self.nn=nn
        self.popsize=pops
        self.elitism=elit
        self.mut_prob=p
        self.noise=K
        self.iterate=itr
        for i in range(int(self.popsize)):
            x = NeuralNet(i,nn,len(train_set)-1,1)
            # print(x)
            self.populacija.append(x)
            # print("populacija :: ",[z.__str__() for z in self.populacija])
        return
    
    def Mutate(self, child:NeuralNet):
        
        pass
    def CrosParents(self, parent1:NeuralNet, parent2:NeuralNet):
        
        pass
    def NewPopulate(self):
        self.sort_fitest()
        new_population=self.populacija[:int(self.elitism)]
        fit_list=[u.fit for u in self.populacija]
        for i in range(int(self.popsize)-int(self.elitism)):
            parent1, new_fit=self.rand_by_fit(fit_list)
            parent2, _ = self.rand_by_fit(new_fit) #fit_list ako se dopusta jedan rodielj
            child=self.CrosParents(self.populacija[parent1], self.populacija[parent2])
            mutated_child=self.Mutate(child)
            new_population.append(mutated_child)
        self.populacija=new_population
        return self.populacija
    
    def trainModel(self):
        pass

    def rand_by_fit(self, fit_list:list):
        new_fit_list=fit_list
        max=sum(fit_list)
        picked=rng.random()
        sum = max
        for i,x in enumerate(fit_list[-1:]):
            sum=sum-x
            if(picked>=sum):
                new_fit_list.pop(len(list)-i-1)
                return len(list)-i-1, new_fit_list

    def calculateFitnes(self): # fix
        total_fit=0
        for x in self.populacija:
            # print(x)
            x:NeuralNet
            avg_fit=0
            count=0
            for i,y in enumerate(self.train_set[-1]):
                inpt = np.array([z[i] for z in self.train_set[:-1]])
                # print(x.calculate_resault(inpt), "  ",y)
                local_fit=x.local_fitnes(x.calculate_resault(inpt), y)
                # print("local_fits: ",local_fit," ",)
                avg_fit=avg_fit+local_fit
                count=i+1
            x.local_fit=avg_fit/count
            # print(x," : : ",x.local_fit)
            total_fit=total_fit+x.local_fit
        for x in self.populacija:
            # x.set_fit(x.local_fit/total_fit)
            x.set_fit(x.local_fit/total_fit)
        return

    def sort_fitest(self):
        self.populacija.sort(key=lambda entry: entry.get_fit() , reverse=True)
        return self.populacija




    


# ucitavanje podataka
def parse_in(args):
    parser=argparse.ArgumentParser()
    parser.add_argument("--train", nargs="?", help="train set putanja")
    parser.add_argument("--test",nargs="?", help="test set putanja")
    parser.add_argument("--nn", nargs="?", help="Arhitektura neuronske mreze")
    parser.add_argument("--popsize", nargs="?", help="velicina populacije")
    parser.add_argument("--elitism", nargs="?", help="elitizam gen algoritma")
    parser.add_argument("--p", nargs="?", help="vjerojatnost mutacije svakog elementa")
    parser.add_argument("--K", nargs="?", help="standardna devijacia gausov sum")
    parser.add_argument("--iter", nargs="?", help="broj iteracija")
    pars_args = parser.parse_args(args)
    with open(pars_args.train, "r") as r:
        all_lines_train = r.readlines()
    with open(pars_args.test, "r") as r:
        all_lines_test = r.readlines()

    nn=pars_args.nn
    pops=pars_args.popsize
    elit=pars_args.elitism
    p=pars_args.p
    K=pars_args.K
    itr=pars_args.iter
    # popunjavanje tran i test dicta
    tarain_set:list=[]
    test_set:list=[]
    for idn,i in enumerate(all_lines_train[0].replace("\n","").split(",")):
            tarain_set.append([])
            test_set.append([])

    for i in all_lines_train[1:]:
        for idn, j in enumerate(i.replace("\n","").split(",")):
            tarain_set[idn].append(float(j))

    for i in all_lines_test[1:]:
        for idn, j in enumerate(i.replace("\n","").split(",")):
            test_set[idn].append(float(j))

    return tarain_set, test_set, nn, pops, elit, p, K, itr





if __name__=='__main__':
    #  print("start")
    #  print(parse_in(sys.argv[1:]))
    NeuralNet.calculate_resault
    gen = Genetika(*parse_in(sys.argv[1:]))
    # print(gen.populacija[0].calculate_resault(np.array([3.469])))
    gen.calculateFitnes()
    print([u.fit__str() for u in gen.sort_fitest()])

