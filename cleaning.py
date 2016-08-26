import pandas as pd
import re


class Cleaner(object):
    """
    """
    def __init__(self, fname, start_columns):
        """
        """
        self.df_in = pd.read_csv(fname)
        self.df= pd.DataFrame(data = self.df_in[start_columns], index=self.df_in.index)

    def clean(self):
        """
        """
        self.fiProductClassDesc()

        
    def fiProductClassDesc(self):
        """
        """
        pcd = self.df_in['fiProductClassDesc']
        pattern = re.compile(r'[^\d]*(\d*\.\d)[^\d]*(\d*\.\d)')
        self.df['fiPCD'] = pcd.str.extract(pattern).astype('float').mean(axis=1)

