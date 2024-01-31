

# create a class for joining dataframes
from joblib import Parallel, delayed


class JoinFunctions:
    @staticmethod
    def inner_join(df1, df2, on):
        return df1.merge(df2, on=on, how='inner')

    @staticmethod
    def left_join(df1, df2, on):
        return df1.merge(df2, on=on, how='left')

    @staticmethod
    def outer_join(df1, df2, on):
        return df1.merge(df2, on=on, how='outer')

    def parallel_inner_join(self, df1, df2, on, n_jobs=-1):
        return Parallel(n_jobs=n_jobs)(delayed(self.inner_join)(df1, df2, on))
    
    def parallel_left_join(self, df1, df2, on, n_jobs=-1):
        return Parallel(n_jobs=n_jobs)(delayed(self.left_join)(df1, df2, on))
    
    def parallel_outer_join(self, df1, df2, on, n_jobs=-1):
        return Parallel(n_jobs=n_jobs)(delayed(self.outer_join)(df1, df2, on))
    