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
