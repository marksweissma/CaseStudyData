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
        self.clean_date()
        self.add_region()


    def fiProductClassDesc(self):
        """
        """
        pcd = self.df_in['fiProductClassDesc']
        pattern = re.compile(r'[^\d]*(\d*\.\d)[^\d]*(\d*\.\d)')
        self.df['fiPCD'] = pcd.str.extract(pattern).astype('float').mean(axis=1)

    def prod_group(self):
        dummies = pd.get_dummies(self.df_in)
        for i in dummies[1:]:
            self.df[i] = dummies[i]

    def enclosure(self):
        '''
        Input: DataFrame
        Output: DataFrame with dummified variables for Enclosure Series.

        Creates dummy variables for enclosure types.

        '''
        # Create dummies.
        dummies = pd.get_dummies(self.df_in.Enclosure)

        # Define labels for features.
        enclosure_labels = dummies.columns

        # Append the dummies to dataframe.
        self.df[enclosure_labels] = dummies

        # Drop the none or unspecified column
        self.df.drop('None or Unspecified', axis =1)

    def add_region(self):
        self.northeast = ('New York','Pennsylvania','New Jersey','Connecticut','Rhode Island','Massachusetts','New Hampshire','Vermont','Maine')
        self.southeast = ('Arkansas','Louisiana','Mississippi','Alabama','Tennessee','Kentucky','Georgia','North Carolina','South Carolina','Virginia','West Virginia','Maryland','Delaware','Washington DC', 'Florida')
        self.midwest = ('North Dakota','South Dakota','Nebraska','Kansas','Minnesota','Iowa','Missouri','Wisconsin','Illinois','Michigan','Ohio','Indiana')
        self.west = ('Montana','Idaho','Wyoming','Colorado','Utah','Oregon','Washington', 'California','Nevada')
        self.southwest = ('Texas','Arizona','New Mexico','Oklahoma')
        self.other = ('Unspecified','Puerto Rico','Hawaii','Alaska')

        self.df['region'] = self.df_in['state'].apply(_to_region)

    def _to_region(self,state):
        if state in self.northeast:
            return 0
        elif state in self.southeast:
            return 1
        elif state in self.midwest:
            return 2
        elif state in self.west:
            return 3
        elif state in self.southwest:
            return 4
        else:
            return 5



    def clean_date(self):
        self.df_in.loc[df_in['YearMade']==1000,'YearMade'] = 2000
        self.df_in['saledate_year'] = pd.to_datetime(self.df_in['saledate']).dt.year
        self.df_in.drop('saledate', axis=1)
        self.df_in['year_diff'] = self.df_in['saledate_year'] - self.df_in['YearMade']

        self.df['year_diff'] = self.df_in['year_diff']
        self.df['YearMade'] = self.df_in['YearMade']
        self.df['saledate_year'] = self.df_in['saledate_year']

        self.cd_index_todrop = self.df_in[self.df_in['year_diff'] < 0].index
