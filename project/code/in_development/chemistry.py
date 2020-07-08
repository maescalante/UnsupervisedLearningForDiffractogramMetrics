import chempy
from project.code import GeneralFunctions as fun
from sklearn.manifold import Isomap
import numpy as np


class chemistry():


    def __init__(self):
        self.path_to_file = 'project/resources/'
        self.path_to_results = 'project/results/'
        self.currentFile = 'DM  - D_PP - p_min 3 - delta 0.5 - q1 -5 - q2 -0.5.csv'

    def get_elements(self, labels):
        newDic = {}
        for el in labels:
            newDic[el] = chempy.Substance.from_formula(el)
        return newDic
    def run(self):
        mat, labels = fun.readMatrix(self.path_to_file + self.currentFile)
        dic= self.get_elements(labels)
        print(dic)
def main():
    iso = chemistry()
    iso.run()