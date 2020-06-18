from project.code import t_sne, MDS,pca,isomap


def run(p):
    print('--- APP RUNNING ---')
    if p == 'sne':
        t_sne.main()
    if p == 'mds':
        MDS.main()
    if p=='pca':
        pca.main()
    if p=='isomap':
        isomap.main()
