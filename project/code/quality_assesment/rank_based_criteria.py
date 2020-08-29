def ranks(d):
    cont=0
    N=len(d)
    p=[ [0 for i in range(N)]] * N
    for i in range(0,len(d)):
        for j in range(0,len(d)):
            dij = d[i][j]
            for k in range(0,j):
                dik=d[i][k]
                if dik<=dij:
                    cont+=1
            p[i][j]=cont
            cont=0
    return p

def coranking_mat(d, dp):
    p=ranks(d)
    r=ranks(dp)
    N=len(d)
    q = [[0 for i in range(N)]] * N
    cont=0
    for  in range(0,N):
        for j in range (0,N):
          if p[i]