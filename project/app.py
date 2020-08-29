from project.code.dimensonality_reduction import pca, t_sne, isomap, mds, mds_raw
from project.code.clustering import hierarchical, k_means, k_medoids, results_visualization
from project.code.in_development import chemistry, database
from project.code.diffractogram_metrics import distance_matrix_creator


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
    elif p == 'hierarchical':
        hierarchical.main()
    elif p == 'k-means':
        k_means.main()
    elif p == 'chemistry':
        chemistry.main()
    elif p == 'db':
        database.main()
    elif p == 'distance':
        distance_matrix_creator.main()
    elif p == 'mds_raw':
        mds_raw.main()
    elif p == 'k-medoids':
        k_medoids.main()
    elif p == 'results':
        results_visualization.main()
