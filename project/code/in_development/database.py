import csv


class Database:

    def __init__(self):
        self.cod_db = 'project/resources/cod/cif/1/55/'
        self.csv = 'project/resources/cod_db.csv'

    def write_csv(self, d):
        print('--- CSV ---')
        with open(self.csv, mode='w') as csv_file:
            writer = csv.writer(csv_file)
            for key in d:
                writer.writerow([key, d[key]])

    def run(self):
        muestras = {}
        total = 0
        for folder in range(100):
            for i in range(100):
                if i < 10:
                    file = self.cod_db + str(folder) + "/155" + str(folder) + '0' + str(i) + ".cif"
                else:
                    file = self.cod_db + str(folder) + "/155" + str(folder) + str(i) + ".cif"
                try:
                    f = open(file, "r")
                    total += 1
                    for x in f:
                        data = x.split(" ")
                        if data:
                            if data[0] == '_chemical_formula_sum':
                                elemento = ''
                                for d in range(len(data)):
                                    if d != 0:
                                        elemento += str(data[d]) + '-'
                                elemento = elemento.replace("-", "")
                                if elemento not in muestras:
                                    count = 1
                                else:
                                    count = muestras[elemento] + 1
                                muestras[elemento] = count
                except:
                    pass
        print('--- Se cuenta con un total de ' + str(total) + ' entradas---')
        print('--- Hay un total de  ' + str(len(muestras)) + ' materiales diferentes---')
        self.write_csv(muestras)


def main():
    db = Database()
    db.run()
