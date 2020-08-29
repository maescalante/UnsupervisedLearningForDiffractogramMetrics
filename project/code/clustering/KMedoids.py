import numpy as np
import random


class KMedoids:

    def __init__(self, iterations=1000, medoids=5):
        self.medoids = medoids
        self.iterations = iterations
        self.matrix = []
        self.n = 0
        self.cost = 99999999999

    def select_random_points(self):
        list = []
        for i in range(self.medoids):
            r = random.randint(1, self.n)
            if r not in list: list.append(r)

        return list

    def find_nearest_medoid(self, medoids, point):
        ans = None
        min = 100000
        for i in medoids:
            if self.matrix[i, point] < min:
                min = self.matrix[i, point]
                ans = i
        return ans

    def assign_points_to_medoids(self, medoids):
        map = {}
        for i in range(self.n):
            medoid = self.find_nearest_medoid(medoids, i)
            map[i] = medoid
        return map

    def calculate_cost(self, map):
        cost = 0
        for k in map:
            cost += self.matrix[k, map[k]]
        return cost

    def select_random_point(self, medoids):
        r = random.randint(1, self.n)
        while r in medoids:
            r = random.randint(1, self.n)
        return r

    def swap_medoid(self, medoid, point, medoids):
        for m in medoids:
            if m == medoid:
                m = point
                break

    def select_random_point(self, medoids):
        r = random.randint(1, self.n)
        while r in medoids:
            r = random.randint(1, self.n)
        return r

    def minimize(self, medoids, costo_inicial):
        point = self.select_random_point(medoids)
        medoid = random.choice(medoids)
        self.swap_medoid(medoid, point, medoids)
        mapa = self.assign_points_to_medoids(medoids)

        cost = costo_inicial
        best_medoids = medoids

        iter = 0
        while iter < self.iterations:
            new_cost = self.calculate_cost(mapa)

            if new_cost < cost:
                best_medoids = self.medoids
                cost = new_cost
            iter += 1

        return best_medoids, cost, mapa

    def fit(self, mat):
        self.matrix = mat
        self.n = mat.shape[0]
        medoids = self.select_random_points()
        mapa = self.assign_points_to_medoids(medoids)

        medoids, cost, mapa = self.minimize(medoids, self.calculate_cost(mapa))

        return medoids, mapa, cost
