from project.code.dimensonality_reduction import pca, t_sne, isomap, mds, mds_corrected
from project.code.clustering import hierarchical, k_means
from project.code import results_visualization
from project.code.in_development import chemistry, database
from project.code.diffractogram_metrics import distance_matrix_creator
from project.code.in_development import triangle_inequality
from project.code.quality_assesment import compare


def run(p):
    print('--- APP RUNNING ---')
    if p[1] == 'sne':
        if len(p) > 2:
            t_sne.main(p[2])
        else:
            t_sne.main()
    elif p[1] == 'mds':
        mds.main()
    elif p[1] == 'pca':
        pca.main()
    elif p[1] == 'isomap':
        if len(p) > 2:
            isomap.main(p[2])
        else:
            isomap.main()
    elif p[1] == 'hierarchical':
        hierarchical.Hierarchical().run()
    elif p[1] == 'k-means':
        k_means.main()
    elif p[1] == 'chemistry':
        chemistry.main()
    elif p[1] == 'db':
        database.main()
    elif p[1] == 'distance':
        distance_matrix_creator.main()
    elif p[1] == 'mds_corrected':
        if len(p) > 2:
            mds_corrected.main(p[2])
        else:
            mds_corrected.main()
    elif p[1] == 'results':
        results_visualization.main()
    elif p[1] == 'triangle_inequality':
        triangle_inequality.main()
    elif p[1] == 'compare':
        compare.main()
