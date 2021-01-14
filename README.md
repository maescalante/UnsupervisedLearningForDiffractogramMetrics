# Unsupervised Learning for Diffractogram Metrics


## Authors 
Juan Camilo Castiblanco and Maria Alejandra Escalante 
Based on the work made by Nicolas Lopez

Universidad de Los Andes, Colombia
## How to run 
Clone the project and navigate to the root 
### Required Libraries
- numpy
- sklearn 
- matplotlib
- networkx
- scipy
- pandas
- statistics
- chempy
- mendeleev
- coranking metrics installed by the command <pip install git+https://github.com/samueljackson92/coranking.git>

### Run command
Each file of the project can be executed by using the following command
python -m project filename

## File Distribution

- Clustering: Includes all the clustering techniques used during the project. On execute graphs the clustering result
- Diffractogram metrics: Includes the code made by Nicolas Lopez in order to obtain the diffractogram dissimilarities
- Dimensionality reduction: Includes all the dimensionality techniques used during the project. When one of them is executed the "D and 3D graph is created and the reconstruction error is calculated
- quality assesment: Includes the file "compare" which compares the performance of MDS, ISOMAP, and T-sne  using reconstruction error, inter class distance, intra class distance and other metrics.
- In development: Includes incomplete code and ideas that were not included in the final version of the project such as functions to obtain chemical information of the materials.


All the generated graphs are also saved in results folder in png format

