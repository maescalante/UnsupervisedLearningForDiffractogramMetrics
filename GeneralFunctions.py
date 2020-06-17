import csv
import matplotlib.pyplot as plt
import random

#Function for importing a distance matrix from a cvs file into a python matrix
def readMatrix (filename):
    matrix=[]

    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            fila = []
            if line_count == 0:
                labels=row
                line_count += 1
            else:
                line=0
                for j in row:
                    if line!=0:
                        fila.append(j)

                    line+=1
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


def plot(label_dict, X):
    """

    :param label_dict: dictonary with index of every label
    :param X: X after Dimentinality reduction
    :param color_dict:
    """

    for k in label_dict:
        col=randomColor()
        label= k
        cont=0
        for j in label_dict[k]:
            if cont==0:
                plt.plot(X[j:, 0], X[j:, 1], 'o', c=col, label=label)
                cont=1
            else:
                plt.plot(X[j:, 0], X[j:, 1], 'o', c=col)
    plt.legend()
    plt.show()


def randomColor():
    r = random.random()

    b = random.random()

    g = random.random()

    color = (r, g, b)
    return color