from project.code.dimensonality_reduction import pca, t_sne, isomap, MDS
from project.code.clustering import hierarchical

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
    if p== 'hierarchical':
        hierarchical.main()
