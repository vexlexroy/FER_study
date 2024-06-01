import sys
import argparse
import numpy

class Genetika:
    train_set:dict
    test_set:dict
    nn:str
    popsize:int
    elitism:int
    mut_prob:float
    noise:float
    iterate:int
    def __init__(self, train_set:dict, test_set:dict, nn:str, pops:int, elit:int, p:float, K:float, itr:int):
        self.train_set=train_set
        self.test_set=test_set
        self.nn=nn
        self.popsize=pops
        self.elitism=elit
        self.mut_prob=p
        self.noise=K
        self.iterate=itr

    


# ucitavanje podataka
def parse_in(args):
    parser=argparse.ArgumentParser()
    parser.add_argument("--train", nargs="?", help="train set putanja")
    parser.add_argument("--test",nargs="?", help="test set putanja")
    parser.add_argument("--nn", nargs="?",choices=['5s', '20s', '5s5s'], help="Arhitektura neuronske mreze")
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
    tarain_set={}
    test_set={}
    for idn,i in enumerate(all_lines_train[0].replace("\n","").split(",")):
            tarain_set[idn]=[]
            test_set[idn]=[]

    for i in all_lines_train[1:]:
        for idn, j in enumerate(i.replace("\n","").split(",")):
            tarain_set[idn].append(j)

    for i in all_lines_test[1:]:
        for idn, j in enumerate(i.replace("\n","").split(",")):
            test_set[idn].append(j)

    return tarain_set, test_set, nn, pops, elit, p, K, itr





if __name__=='__main__':
    #  print("start")
    #  print(parse_in(sys.argv[1:]))
    gen = Genetika(parse_in(sys.argv[1:]))

