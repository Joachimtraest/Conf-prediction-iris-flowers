from iris import Iris, Iris_Dataset
import pandas as pd
import numpy as np
from nonconf import Conf_Predict as cp
#the dataset of table 2 in shafer and vovk: tutorial on conformal prediction p.390
sepal_lengths = [5.0,4.4,4.9,4.4,5.1,5.9,5.0,6.4,6.7,6.2,5.1,4.6,5.0,5.4,5.0,6.7,5.8,5.5,5.8,5.4,5.1,5.7,4.6,4.6]
speciess = ['se', 'se', 'se', 'se', 'se', 've', 'se', 've', 've', 've', 'se', 'se', 'se' , 'se','ve', 've', 've', 'se', 've', 'se', 'se', 've', 'se', 'se']

train_set = Iris_Dataset() 
for i in range(len(sepal_lengths)): #the first fifty flowers are used as training set 
    flower = Iris(flower_index = i, sepal_length=sepal_lengths[i], species = speciess[i])
    train_set.add_iris(flower)

flower25 = Iris(sepal_length=6.8, flower_index=25)
print(cp.get_py(cp.NN, train_set.flowerlist, flower25, 've'))
print(cp.get_nonconf_scores(cp.NN, train_set.flowerlist, flower25, 've'))