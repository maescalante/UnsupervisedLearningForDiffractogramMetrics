import numpy as np
import math

def euclidean_distance(X, components=2):
    ans = []
    for x in X:
        l = []
        for x2 in X:
            if components == 2:
                l.append(float(math.sqrt((x[0] - x2[0]) ** 2 + (x[1] - x2[1]) ** 2)))
            elif components == 3:
                l.append(float(math.sqrt((x[0] - x2[0]) ** 2 + (x[1] - x2[1]) ** 2)) + (x[2] - x2[2]) ** 2)
        ans.append(l)
    return ans


def normalizar(m):
    maximo = m.max()
    return np.divide(m, maximo)


def error(m, x, components=2):
    distancias = euclidean_distance(x, components)
    distancias = np.array(distancias, dtype=np.float64)
    m1 = normalizar(distancias)
    m2 = normalizar(m)
    return round(100 * sum(sum((np.subtract(m1, m2))**2)) / (91 * 91), 2)
