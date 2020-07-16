from project.code.dimensonality_reduction import pca, t_sne, isomap, mds
from project.code.clustering import hierarchical
from project.code.clustering import k_means
from project.code.in_development import chemistry
from project.code.dimensonality_reduction import mds_raw
def run(p):
    print('--- APP RUNNING ---')
    if p == 'sne':
        t_sne.main()
    elif p == 'mds':
        mds.main()
    elif p == 'pca':
        pca.main()
    elif p == 'isomap':
        isomap.main()
    elif p== 'hierarchical':
        hierarchical.main()
    elif p == 'k-means':
        k_means.main()
    elif p=='chemistry':
        chemistry.main()
