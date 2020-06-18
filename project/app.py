from project.code import t_sne, MDS


def run(p):
    print('--- APP RUNNING ---')
    if p == 'sne':
        t_sne.main()
    if p == 'mds':
        MDS.main()
