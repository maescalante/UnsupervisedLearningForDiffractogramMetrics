from project.code.dimensonality_reduction import pca, t_sne, isomap, MDS
<<<<<<< Updated upstream
from project.code.clustering import hierarchical
=======
from project.code.clustering import k_means

>>>>>>> Stashed changes

def run(p):
    print('--- APP RUNNING ---')
    if p == 'sne':
        t_sne.main()
    elif p == 'mds':
        MDS.main()
    elif p == 'pca':
        pca.main()
    elif p == 'isomap':
        isomap.main()
<<<<<<< Updated upstream
    if p== 'hierarchical':
        hierarchical.main()
=======
    elif p == 'k-means':
        k_means.main()
>>>>>>> Stashed changes
