import GeneralFunctions as fun
from sklearn.manifold import MDS
import numpy as np
import matplotlib.pyplot as plt
import random
currentFile='DM  - D_PP - p_min 3 - delta 0.5 - q1 -5 - q2 -0.5.csv'
mat,labels=fun.readMatrix(currentFile)
mat = np.array(mat, dtype=np.float64)


embedding = MDS(n_components=2,dissimilarity='precomputed')
X_transformed = embedding.fit_transform(mat)

dic=fun.create_dictionary(labels)

fun.plot(dic,X_transformed)


