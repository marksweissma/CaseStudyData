def clean_date(self):
    self.df.loc[df['YearMade']==1000,'YearMade'] = 2000
    self.df['saledate_year'] = pd.to_datetime(self.df['saledate']).dt.year
    self.df.drop('saledate', axis=1)
    self.df['year_diff'] = self.df['saledate_year'] - self.df['YearMade']
    index_todrop = self.df[self.df['year_diff'] < 0].index
