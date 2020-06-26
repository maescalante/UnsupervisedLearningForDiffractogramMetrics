import csv
import matplotlib.pyplot as plt
import random
import math
import numpy as np
from mpl_toolkits import mplot3d



# Function for importing a distance matrix from a cvs file into a python matrix
def readMatrix(filename):
    matrix = []

    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            fila = []
            if line_count == 0:
                labels = row
                line_count += 1
            else:
                line = 0
                for j in row:
                    if line != 0:
                        fila.append(j)

                    line += 1
                matrix.append(fila)

    return matrix, labels


def create_dictionary(labels):
    """

    :param labels: labels of the samples
    :return: dictonary with index of every label
    """
    d = {}

    i = 0
    for l in labels:
        l1 = l.split('.')
        if l1[0]:
            if l1[0] not in d:
                d[l1[0]] = [i]
            else:
                lista = d[l1[0]]
                lista.append(i)
                d[l1[0]] = lista
        i += 1

    return d


def plot(labels, X):
    """

    :param label_dict: dictonary with index of every label
    :param X: X after Dimentinality reduction
    :param color_dict:
    """

    label_dict= create_dictionary(labels)

    for k in label_dict:
        col = randomColor()
        label = k

        flag=0
        cont = 0
        for j in label_dict[k]:
            if flag == 0:
                plt.plot(X[j-1, 0], X[j-1, 1], 'o', c=col, label=label)
                flag=1
            else:

                plt.plot(X[j-1,0], X[j-1,1], 'o', c=col)
                plt.annotate(str(cont),xy=(X[j-1,0], X[j-1,1]))
       
            cont+=1

    plt.legend()
    return plt

def plot3d(labels, X):

    label_dict = create_dictionary(labels)
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    for k in label_dict:
        col = randomColor()
        label = k

        flag = 0
        cont = 0
        for j in label_dict[k]:
            if flag == 0:
                ax.scatter3D(X[j-1,0], X[j-1,1], X[j-1,2], 'o', c=col, label=label)
                flag = 1
            else:

                ax.scatter3D(X[j-1,0], X[j-1,1], X[j-1,2], 'o', c=col)
                x=X[j-1,0]

                y=X[j-1,1]
                z=X[j - 1, 2]
                ax.text(x,y,z, cont,'x')


            cont += 1

    plt.legend()
    plt.show()
    return plt

def randomColor():
    r = random.random()

    b = random.random()

    g = random.random()

    color = (r, g, b)
    return color

def euclidean_distance(X):
    ans = []
    for x in X:
        l = []
        for x2 in X:
            l.append(float(math.sqrt((x[0] - x2[0]) ** 2 + (x[1] - x2[1]) ** 2)))
        ans.append(l)
    return ans

def euclidean_distance_3d(X):
    ans = []
    for x in X:
        l = []
        for x2 in X:
            l.append(float(math.sqrt((x[0] - x2[0]) ** 2 + (x[1] - x2[1]) ** 2)) + (x[2] - x2[2]) ** 2)
        ans.append(l)
    return ans

def normalizar(m):
    maximo = m.max()
    return np.divide(m, maximo)

def error(m, x):
    distancias = euclidean_distance(x)
    distancias = np.array(distancias, dtype=np.float64)
    m1 = normalizar(distancias)
    m2 = normalizar(m)
    return round(100*sum(sum(abs(np.subtract(m1, m2)))) / (91 * 91), 2)

def error_3d(m, x):
    distancias = euclidean_distance_3d(x)
    distancias = np.array(distancias, dtype=np.float64)
    m1 = normalizar(distancias)
    m2 = normalizar(m)
    return round(100*sum(sum(abs(np.subtract(m1, m2)))) / (91 * 91), 2)