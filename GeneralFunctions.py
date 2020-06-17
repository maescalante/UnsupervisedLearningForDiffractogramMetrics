import csv


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