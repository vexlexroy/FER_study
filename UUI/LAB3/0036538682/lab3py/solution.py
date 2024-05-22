import sys
import csv
import math

class desTree:
    totla_entropy=None
    def __init__(self):
        pass

    def entropy(self, dataset):
        posible_val={}
        et_val=0
        last_coll=dataset[1:][-1] # last row
        num_of_all=len(last_coll)
        set_of_last=list(set(last_coll))
        for x in set_of_last: # count same
            if(x in set(posible_val.keys)):
                posible_val[x]=posible_val[x]+1
            else:
                posible_val[x]=1
        for x in posible_val: # calculate entropy
            et_val=et_val - (posible_val[x]/num_of_all)*math.log2(posible_val[x]/num_of_all)
        return et_val

    def info_gain(self, dataset, factor):
        data_dict={}
        raz_znacajke={}
        ig_sum=0
        for i,x in enumerate(dataset[0]):
            data_dict[x]=[vals for vals in dataset[i][1:]]
        for x in data_dict[factor]:
            if(x in raz_znacajke):
                raz_znacajke[x]=raz_znacajke[x]+1
            else:
                raz_znacajke[x]=1
        for x in raz_znacajke:
            ig_sum = ig_sum + (raz_znacajke[x]/len(data_dict[factor]))*self.entropy()

        return self.totla_entropy - ig_sum
        
        

    def recur_ID3():
        pass
    
        











if __name__== "__main__":
    arguments=sys.argv[1:]
    dataset=arguments[0]
    testset=arguments[1]
    if(len(arguments)>2):
        depth=arguments[2]
    else:
        pass

    with open(dataset, mode='r') as datain:
        data_set=csv.reader(datain)

    with open(testset, mode='r') as datain:
        test_set=csv.reader(datain)
