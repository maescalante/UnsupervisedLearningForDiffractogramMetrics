muestras = {}
for i in range(100):
    if i<10:
        file = "COD/400000" + str(i) + ".cif"
    else:
        file = "COD/40000" + str(i) + ".cif"
    f = open(file, "r")
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
    print(muestras)