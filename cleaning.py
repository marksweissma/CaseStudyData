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
        self.prod_group()
        self.enclosure()

        
    def fiProductClassDesc(self):
        """
        """
        pcd = self.df_in['fiProductClassDesc']
        pattern = re.compile(r'[^\d]*(\d*\.\d)[^\d]*(\d*\.\d)')
        self.df['fiPCD'] = pcd.str.extract(pattern).astype('float').mean(axis=1)

    def prod_group(self):
        dummies = pd.get_dummies(self.df_in, )
        for i in dummies[1:]:
            self.df[i] = dummies[i]

    def enclosure(self):
        '''
        Input: DataFrame
        Output: DataFrame with dummified variables for Enclosure Series.

        Creates dummy variables for enclosure types.

        '''
        # Create dummies.
        dummies = pd.get_dummies(self.df.Enclosure)

        # Define labels for features.
        enclosure_labels = dummies.columns

        # Append the dummies to dataframe.
        self.df[enclosure_labels] = dummies

        # Drop the none or unspecified column
        self.df.drop('None or Unspecified', axis =1)
