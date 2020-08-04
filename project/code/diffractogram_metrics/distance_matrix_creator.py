import os
import numpy as np
from project.code.diffractogram_metrics import distance_functions, save_load_fuctions, pre_processing


class DistanceMatrixCreator:

    def __init__(self):
        self.parameters = {
            'delta': np.finfo(np.double).eps,  # Minimum distance between peaks
            'q1': -10,  # First exponential parameter
            'q2': -0.5,  # Second exponential parameter
            'p_min': 3,  # Minimum number of peaks allowed
            'p_max': 0,  # Maximum number of peaks allowed (0 if no maximum used)
            'beta': 0.8,  # Case ranked distance
            'gamma': 2,  # Case proportional distance
            'list_extremes_file': 'list_extremes',
        }
        self.paths = {
            'results': 'project/results/',
            'resources': 'project/resources/',
            'extremes': '',
        }
        self.dist_function = 'D_PP'
        self.do_plot = True  # Optional do plotting after creating the matrix
        self.path_to_file = 'project/resources/'
        self.currentFile = 'DM  - D_PP - p_min 3 - delta 0.5 - q1 -5 - q2 -0.5.csv'

    def list_extremes(self):
        """
        loads the list extremes files or creates a new one.
        The list extremes is a file that contains information about ...
        """
        if os.path.isfile(self.paths['resources'] + self.parameters['list_extremes_file'] + '.csv'):
            list_extremes, classes, extremes_df = save_load_fuctions.load_extremes(self.paths['resources'] +
                self.parameters['list_extremes_file'])
        else:  # Else loads data from raw files
            # Loads data from raw csv files
            data, classes, file_names, files_id = save_load_fuctions.import_data_raw(
                trPath=self.paths['resources'] + self.parameters['list_extremes_file'])

            # Get Information on extreme values
            list_extremes = pre_processing.apply_to(pre_processing.extremes_sample, data, other=None)

            # Merges the above information in one table
            extremes_df = pre_processing.merge_extreme_information(list_extremes, classes, files_id)

            # Sves file for future use
            extremes_df.to_csv(self.paths['resources'] + self.parameters['list_extremes_file'] + '.csv')

        return list_extremes, classes

    def file_name(self):
        """
        names the distance matrix file
        """
        optional = ''
        if self.dist_function == 'D_PPrk':
            optional += ' beta ' + str(self.parameters['beta'])
        elif self.dist_function == 'D_PPpr':
            optional += ' gamma ' + str(self.parameters['gamma'])
        if self.parameters['p_max'] != 0:
            optional += ' - ' + 'p_max ' + str(self.parameters['p_max'])

        tmp = self.dist_function + ' - ' + optional + ' - p_min ' + str(self.parameters['p_min']) + ' - delta ' + \
              str(self.parameters['delta']) + ' - q1 ' + str(self.parameters['q1']) + ' - q2 ' + \
              str(self.parameters['q2']) + '.csv'
        distM_name = self.paths['resources'] + 'DM ' + tmp
        return distM_name

    def start(self):
        # Distance function to be used
        # Ranked and Proportional distance use positive q2
        # D_PP : basic distance
        # D_PPrk : ranked distance
        # D_PPpr : proportional distance
        if self.dist_function == 'D_PP':
            dist_function = distance_functions.D_PP

        list_extremes, classes = self.list_extremes()

        # Extracts Peak informations
        list_peaks = pre_processing.apply_to(pre_processing.get_search, list_extremes, prog=False)

        # list_valleys = pre_processing.apply_to(pre_processing.get_search, list_extremes, prog=False, other='min')

        name = self.file_name()

        # Filter samples with less peaks than the minimum allowed
        tmp = range(len(classes))
        classes = [classes[i] for i in tmp if list_peaks[i].shape[0] >= self.parameters['p_min']]
        list_peaks = [list_peaks[i] for i in tmp if list_peaks[i].shape[0] >= self.parameters['p_min']]

        # Filter irrelevant peaks (when p_max != 0)
        if self.parameters['p_max'] != 0:
            for i in range(len(list_peaks)):
                if list_peaks[i].shape[0] > self.parameters['p_max']:
                    list_peaks[i] = list_peaks[i].sort_values(by=['value'], ascending=False)
                    list_peaks[i] = list_peaks[i].head(self.parameters['p_max'])

        # Distances matrix
        distances = distance_functions.distances_matrix(list_peaks, classes, self.parameters, dist_function)

        # Normalizes distances: Maximum Distance becomes 1
        max_distance = max(distances.max())
        distances = distances.apply(lambda x: x / max_distance)

        distances.to_csv(name)


def main():
    dmc = DistanceMatrixCreator()
    dmc.start()
