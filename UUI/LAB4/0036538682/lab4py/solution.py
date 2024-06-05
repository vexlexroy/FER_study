import sys
import argparse
import numpy as np
from numpy import random
import random as rng
import math

class NeuralNet:
    layers=None # layer : weights(np array)
    arcitecture:str
    inParams:int
    outParams:int
    mse:float = None
    fit:float = None
    count:float = 0.001
    def __init__(self, id, architecture:str=None, inparm:int=None, outparm:int=None, existingweights:dict=None, standard_dev=None):
        # self.count=str(int(self.count)+1+int(id))
        if (existingweights==None):
            self.layers={}
            self.arcitecture=architecture
            self.inParams=inparm
            self.outParams=outparm
            self.count=id
            arc=(str(self.inParams)+'s'+architecture+str(self.outParams)).split('s')
            # print(architecture.split("s"))
            # print(arc)
            for i,x in enumerate(arc[1:]):
                # print(i, " ", x)
                self.layers[i]=random.uniform(low=-standard_dev, high=standard_dev, size=(int(arc[i])+1, int(x))) # ekstra red za bias
        else:
            self.layers=existingweights.copy()
            self.inParams=inparm
            self.outParams=outparm
            self.count=id
            pass
        return
    
    def __str__(self):
        return(f"NeuroNet:{self.count}  fit:{self.fit}  weights:",self.layers)
    def fit__str(self):
        return(f"NeuroNet {self.count}  fit: {self.fit}")
    
    def set_fit(self, fitnes:float):
        self.fit=fitnes
        return fitnes
    
    def get_fit(self):
        return self.fit
    
    def sigmoid_finction(self, xexp):
        return 1/(1 + np.exp(-xexp))
    
    def calculate_resault(self, input:np.array):
        out:np.array=input
        for i,x in enumerate(self.layers):
            # print(out)
            # print("++++++++++++++++++++++++++++++++++++++++++")
            if out.ndim == 1:  # ako je 1d dodati dimenziju
                out = out.reshape(-1, 1)
            ones = np.ones((out.shape[0], 1), dtype=float)  
            out = np.hstack((out, ones))  # dodaje stupac jedinica
            # print(out)
            if(i<len(self.layers)-1):
                out=self.sigmoid_finction(np.dot(out,self.layers[x]))
            else:
                out=np.dot(out,self.layers[x])
        self.fit=None
        # print(self,"out: ",out)
        return out
    
    def local_fitnes(self, resault:np.array, test_val:np.array):
        ret=((test_val-resault)**2)
        # print(ret)
        return ret

class Genetika:
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
            x = NeuralNet(i*0.001,nn,len(train_set)-1,1, standard_dev=float(self.noise))
            # print(x)
            self.populacija.append(x)
            # print("populacija :: ",[z.__str__() for z in self.populacija])
        return
    
    def Mutate(self, child:NeuralNet): # prolazi sve clanove u matrici tezina i mutira
        new_layers={}
        for x in child.layers:
            layer_matrix=np.array(child.layers[x])
            # print(f"mut:{x} ly: ",layer_matrix)
            for j,y in enumerate(layer_matrix):
                for i,z in enumerate(y):
                    hit=rng.random()
                    if(float(self.mut_prob) <= hit):
                        layer_matrix[j][i]=layer_matrix[j][i]+random.normal(loc=0.0, scale=float(self.noise))
            new_layers[x]=layer_matrix
        child.layers=new_layers
        return child

    def CrosParents(self, parent1:NeuralNet, parent2:NeuralNet): # izabire dva roditelja i radi srednje vrijednosti tezina slojeva
        id=parent1.count*10+parent2.count
        inparms=parent1.inParams
        outparams=parent1.outParams
        child_layers={}
        for x in parent1.layers:
            p1_layer=np.array(parent1.layers[x])
            p2_layer=np.array(parent2.layers[x])
            avg=(p1_layer+p2_layer)/2
            # print(x," : ",p1_layer, "\n||\n", p2_layer, "\n||\n", avg)
            child_layers[x]=avg
            # print(child_layers)
        child=NeuralNet(id, None, inparms, outparams, child_layers)
        # print(child)
        return child
    
    def NewPopulate(self): # odvaja elite i radi dijecu do pop size
        self.calculateFitnes()
        self.sort_fitest()
        if(self.elitism!=0):
            new_population=self.populacija[:max(0, int(self.elitism)-1)]
        else:
            new_population=[]
        fit_list=[u.get_fit() for u in self.populacija]
        # print([u.get_fit()[0] for u in self.populacija])
        # print(fit_list)
        for i in range(int(self.popsize)-int(self.elitism)+1):
            parent1, new_fit=self.rand_by_fit(fit_list)
            parent2, _ = self.rand_by_fit(fit_list) #fit_list ako se dopusta jedan rodielj
            child=self.CrosParents(self.populacija[parent1], self.populacija[parent2])
            # print(child)
            mutated_child=self.Mutate(child)
            # print(mutated_child)
            new_population.append(mutated_child)
            # print([x.__str__() for x in new_population])
        # print(i)
        self.populacija=new_population
        return self.populacija
    
    def trainModel(self): # treniranje iter iteracija
        top_fit=None
        for i in range(int(self.iterate)+1):
            self.NewPopulate()
            self.calculateFitnes()
            if(i!=0 and i%(int(self.iterate)/5)==0):
                top_fit=self.sort_fitest()[0]
                print(f"[Train error @{i}]: {self.average_mistake_train(top_fit)}")
        self.calculateFitnes()
        top_fit=self.sort_fitest()[0]
        print(f"[Test error]: {self.average_mistake_test(top_fit)}")
        return top_fit

    def rand_by_fit(self, fit_list:list): # odabire nasumice index nekog neural neta po fitU
        new_fit_list=fit_list.copy()
        max=sum(fit_list)
        picked=rng.random()*max
        sum_ = max
        # print(fit_list)
        # print("picked: ", picked)
        for i,x in enumerate(fit_list[::-1]):
            sum_= sum_-x
            # print(sum_)
            if(picked>=sum_):
                # print("found :", len(fit_list)-i-1)
                new_fit_list.pop(len(fit_list)-i-1)
                # print(fit_list,"\n", new_fit_list)
                return len(fit_list)-i-1, new_fit_list
        # print("error")
        return None

    def calculateFitnes(self): # racuna mse za svaki i dijeli s totalnim , te koristi 1/relativ_mse
        total_fit=0
        for x in self.populacija:
            # print(x)
            x:NeuralNet
            x.mse=self.average_mistake_train(x)
            # print(x.count," : : ",x.mse)
            total_fit=total_fit+x.mse
        rel_sum=0
        for x in self.populacija:
            # print(f"loc: {x.mse} , tot: {total_fit} , rel: {1/(x.mse/total_fit)}")
            relative_fit=x.mse/total_fit
            x.set_fit(1/relative_fit)
            # x.set_fit(1/(1+(x.mse/total_fit)))
            rel_sum+=x.get_fit()
        # print(f"full: {rel_sum}")
        return
    
    def average_mistake_train(self, net:NeuralNet):# racuna mse za train set
        total_fit=0
        count=0
        for i,x in enumerate(self.train_set[-1]):
            inpt = np.array([z[i] for z in self.train_set[:-1]])
            # print(f"in:{inpt} , out: {x}, calculated: {net.calculate_resault(inpt)[0]}")
            count+=1
            total_fit=total_fit+net.local_fitnes(net.calculate_resault(inpt)[0], x)
        average_fit=(total_fit/(count))
        return average_fit

    def average_mistake_test(self, net:NeuralNet):# racuna mse za test set
        total_fit=0
        count=0
        for i,x in enumerate(self.test_set[-1]):
            inpt = np.array([z[i] for z in self.test_set[:-1]])
            # print(f"in:{inpt} , out: {x}, calculated: {net.calculate_resault(inpt)[0]}")
            count+=1
            total_fit=total_fit+net.local_fitnes(net.calculate_resault(inpt)[0], x)
        average_fit=(total_fit/(count+1))
        return average_fit

    def sort_fitest(self): # sortira po fitnesu
        self.populacija.sort(key=lambda entry: entry.get_fit() , reverse=True)
        # print([x.__str__() for x in self.populacija])
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

    # print("train_set:", tarain_set)
    # print("test_set:", test_set)
    return tarain_set, test_set, nn, pops, elit, p, K, itr





if __name__=='__main__':
    #  print("start")
    #  print(parse_in(sys.argv[1:]))
    gen = Genetika(*parse_in(sys.argv[1:]))
    # print(str(gen.populacija[0].__str__()))
    # print(gen.populacija[0].calculate_resault(np.array([3.469])))
    # gen.calculateFitnes()
    # print([u.fit__str() for u in gen.sort_fitest()])
    model:NeuralNet=gen.trainModel()
    # print([(model.calculate_resault(np.array([z[i] for z in gen.train_set[:-1]]))[0],gen.train_set[-1][i]) for i in range(len(gen.train_set[0]))])


