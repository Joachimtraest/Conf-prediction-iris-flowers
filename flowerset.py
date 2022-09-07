from iris import Iris, Iris_Dataset
import pandas as pd
import numpy as np
from cp_iris import CP_Iris as cp
from copy import deepcopy

#the dataset of table 2 in shafer and vovk: tutorial on conformal prediction p.390
sepal_lengths = [5.0,4.4,4.9,4.4,5.1,5.9,5.0,6.4,6.7,6.2,5.1,4.6,5.0,5.4,5.0,6.7,5.8,5.5,5.8,5.4,5.1,5.7,4.6,4.6]
speciess = ['se', 'se', 'se', 'se', 'se', 've', 'se', 've', 've', 've', 'se', 'se', 'se' , 'se','ve', 've', 've', 'se', 've', 'se', 'se', 've', 'se', 'se']

train_set = Iris_Dataset() 
for i in range(len(sepal_lengths)): #the first fifty flowers are used as training set 
    flower = Iris(flower_index = i, sepal_length=sepal_lengths[i], species = speciess[i])
    train_set.add_iris(flower)

flower25 = Iris(sepal_length=6.8, flower_index=25)
#print(cp.get_py(cp.NN,  flower25, train_set.flowerlist, 've'))
#print(cp.get_nonconf_scores(cp.NN,  flower25, train_set.flowerlist,'ve'))
cp.classify_Iris(cp.Dist_to_avg, flower25, train_set.flowerlist, train_set.get_unique_species())


