    def enclosure_dummies(self):
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

    def UsageBand_dummies(self):

        '''
        Input: DataFrame
        Output: DataFrame with dummified variables for UsageBand Series.

        Create usage band to 1,2,3, nan = 0

        

        '''

        self.df.UsageBand = self.df.UsageBand.map({'Low': 1, 'Medium': 2, 'High': 3, np.nan : 0})
