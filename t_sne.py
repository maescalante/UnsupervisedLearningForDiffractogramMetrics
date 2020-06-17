import GeneralFunctions as fun
from sklearn.manifold import TSNE

currentFile = 'DM  - D_PP - p_min 3 - delta 0.5 - q1 -5 - q2 -0.5.csv'
mat, labels = fun.readMatrix(currentFile)

label_dict = fun.create_dictionary(labels)

color_dict = {
    'Ag2Se': 'bo',
    'AgSe': 'go',
    'Cu2Se': 'ro',
    'CuSe': 'co',
    'Si': 'mo',
    'TiN': 'yo',
    'Ti': 'ko',
}

X = mat
X_embedded = TSNE(n_components=2).fit_transform(X)

fun.plot(label_dict, X_embedded, color_dict)
print(labels)
