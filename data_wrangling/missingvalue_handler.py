import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer


class MissingValueHandler:
    def __init__(self, data_df):
        self.imputer_mean = SimpleImputer(strategy='mean')
        self.imputer_median = SimpleImputer(strategy='median')
        self.imputer_mode = SimpleImputer(strategy='most_frequent')
        self.data_df = data_df

    def dropping_na(self, data):
        """
        
        
        """
        return data.dropna()

    def impute_statly(self, data):
        """
        
        implement imputation using statistics
        imcomplete
        """


        return self.imputer_mean.fit_transform(data), self.imputer_median.fit_transform(data), self.imputer_mode.fit_transform(data)

    def baysian_imputation(self, data):
        """
        Implement Bayesian imputation here
        
        
        """ 


        # Perform Bayesian imputation here
        return data












# dropping missing values



"""

Common statistics calculated include:

    The column mean value.
    The column median value.
    The column mode value.
    A constant value.


"""
# define imputer: mean
imputer_mean = SimpleImputer(strategy='mean')


# define imputer: median
imputer_median = SimpleImputer(strategy='median')


# define imputer: mode
imputer_mode = SimpleImputer(strategy='most_frequent')


"""

Baysian imputation:


"""

