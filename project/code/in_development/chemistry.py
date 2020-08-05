import chempy
from project.code import general_functions as fun
from sklearn.manifold import Isomap
import numpy as np
import mendeleev

class chemistry():


    def __init__(self):
        self.path_to_file = 'project/resources/'
        self.path_to_results = 'project/results/'
        self.currentFile = 'DM  - D_PP - p_min 3 - delta 0.5 - q1 -5 - q2 -0.5.csv'
    def get_unique(self,labels):
        new_labels=[]
        for i in labels:
            act=i.split(".")[0]
            if act not in new_labels:
                new_labels.append(i)
        return new_labels
    def get_elements(self, labels):
        elem=[]
        for el in labels:
            element=chempy.Substance.from_formula(el)
            if element not in elem:
                elem.append(element)

        return elem
    def run(self):
        mat, labels = fun.readMatrix(self.path_to_file + self.currentFile)
        li=self.get_unique(labels[1:])

        dic= self.get_elements(li)


        for i in dic:
            print("element name: "+i.name)
            for k in i.composition:
                actual=mendeleev.element(k)
                print(actual.name+": "+str(i.composition[k]))#" electrones: "+ str(actual.covalent_radius))





def main():
    iso = chemistry()
    iso.run()