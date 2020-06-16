import csv
matriz=[]

with open('DM  - D_PP - p_min 3 - delta 0.5 - q1 -5 - q2 -0.5.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        fila = []
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            line=0
            for j in row:
                if line!=0:
                    fila.append(j)

                line+=1
            matriz.append(fila)

    print(f'Processed {line_count} lines.')


