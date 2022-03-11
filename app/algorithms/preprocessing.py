import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


class Preprocessing:

    def preprocess_data(self, data: pd.Dataframe):
        # TODO
        scaler = StandardScaler()
        pass

    def process_data(self, data: pd.Dataframe):
        # TODO
        pca = PCA()
        clustering = DBSCAN()
        pass
