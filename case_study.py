# coding: utf-8
get_ipython().magic(u'pwd ')
get_ipython().magic(u'ls ')
import cleaning
cleaned = cleaning.Cleaner('../regression-case-study/data/Train.csv', ['SaleId','SalePrice'])
cleaned = cleaning.Cleaner('../regression-case-study/data/Train.csv', ['SaleID','SalePrice'])
reload(cleaning)
cleaned = cleaning.Cleaner('../regression-case-study/data/Train.csv')
cleaned.clean()
get_ipython().magic(u'pinfo pd.get_dummies')
reload(cleaning)
cleaned = cleaning.Cleaner('../regression-case-study/data/Train.csv')
cleaned.prod_group()
cleaned.clean()
reload(cleaning)
cleaned = cleaning.Cleaner('../regression-case-study/data/Train.csv')
cleaned.clean()
cleaned.df
cleaned.df.columns
cleaned.df.to_csv('data2.txt')
get_ipython().magic(u'pwd ')
cleanTest = cleaning.Cleaner('../regression-case-study/data/test.csv', start_columns=['SalesID'])
cleanTest.clean()
cleanTest.df
cleanTest.df_in
e cleanTest.df_in.Enclosure
e= cleanTest.df_in.Enclosure
e
e.unique()
cleaned.df_in.Enclosure.unique()
e.unique()
'None or Unspecified' in e
e
'None or Unspecified' in cleaned.df_in.Enclosure
cleaned.df_in.Enclosure.set()
cleaned.df_in.Enclosure.unique()
cleaned.df.columns
cleaned.df['fiPCD'].unique()
dfc = cleaned.df.columns
dfc
cleaned.df_in.Enclosure.str.contains('None or Unspecified')
any(cleaned.df_in.Enclosure.str.contains('None or Unspecified'))
any(e.str.contains('None or Unspecified'))
e.unique()
any(e.str.contains("None or Unspecified"))
reload(cleaning)
cleanTest = cleaning.Cleaner('../regression-case-study/data/test.csv', start_columns=['SalesID'])
cleanTest.clean()
cleanTest
cleanTest.df
cleaned.df.columns
len(cleaned.df.columns)
[for i in cleanTest.df.columns if i not in cleaned.df.columns]
[i for i in cleanTest.df.columns if i not in cleaned.df.columns]
i
[i for i in cleanTest.df.columns if i not in cleaned.df.columns]
[i for i in cleaned.df.columns if i not in cleanTest.df.columns]
cleanTest.df.to_csv('test.csv')
get_ipython().magic(u'pwd ')
from sklearn import LinearRegression
from sklearn.linear_model import LinearRegression
model = LinearRegression()
exclude_columns
exclude_columns = ['SalePrice', 'NO ROPS', 'None or Unspecified']
x = cleaned.df[[i for i in cleaned.df if i not in exclude_columns]]
x
y = cleaned.df.SalePrice
xc = np.c_[np.ones_like(y), x]
fit = model.fit(xc,y)
d = cleaned.df.dropna()
x = d[[i for i in d if i not in exclude_columns]]
xc = np.c_[np.ones_like(y), x]
y = d.SalePrice
xc = np.c_[np.ones_like(y), x]
fit = model.fit(xc,y)
get_ipython().magic(u'ls ')
yh = fit.predict(y)
yh = fit.predict(xc)
np.sum((yh-y)**2)/float(len(y))
np.sqrt(np.sum((yh-y)**2)/float(len(y)))
np.mean(y)
fit.coef_
x
xm = x-x.mean(axis=0)
xms = x.astype('float')/x.std(axis=0)
model = LinearRegression()
xmsc = np.c_[np.ones_like(y), xms]
xmsc
fit = model.fit(xmsc,y)
yh = fit.predict(xmsc)
np.sqrt(np.sum((yh-y)**2)/float(len(y)))
np.sqrt(np.sum((log(yh+1)-log(y+1))**2)/float(len(y)))
np.sqrt(np.sum((np.log(yh+1)-np.log(y+1))**2)/float(len(y)))
d.columns
t = d[[i for i in d.columns if i i not in exclude_columns]]
t = d[[i for i in d.columns if i not in exclude_columns]]
t.columns
x.columns
tm = t-t.mean(axis=0)
tms = t.astype('float')/t.std(axis=0)
tmsc = np.c_[np.ones((tms.shape[0])), tms]
yhc = fit.predict(tmsc)
yhc
out_df = pd.DataFrame(data=np.c_[cleanTest.df.SalesID.values, yhc], columns=['SalesID', ['SalePrice']])
out_df = pd.DataFrame(data=np.c_[cleanTest.df.SalesID.values, yhc], columns=['SalesID', ['SalePrice']])
cleanTest.df.SalesID.values.shape
yhc.shape
tms.shape
tdf = cleanTest.df
t =tdf[[i for i in d.columns if i i not in exclude_columns]]
t =tdf[[i for i in d.columns if i not in exclude_columns]]
t.shape
tm = t-t.mean(axis=0)
tms = t.astype('float')/t.std(axis=0)
tmsc = np.c_[np.ones((tms.shape[0])), tms]
yhc = fit.predict(tmsc)
d = cleaned.df.fillna(cleaned.df.mean(axis=0))
t = cleanTest.df.fillna(cleanTest.df.mean(axis=0))
x = d[[i for i in d if i not in exclude_columns]]
y = d.SalePrice
xm = x-x.mean(axis=0)
xms = x.astype('float')/x.std(axis=0)
xmsc = np.c_[np.ones_like(y), xms]
model = LinearRegression()
fit = model.fit(xmsc,y)
fit.predict(xmsc)
yh = fit.predict(xmsc)
np.sqrt(np.sum((np.log(yh+1)-np.log(y+1))**2)/float(len(y)))
tm = t-t.mean(axis=0)
tms = t.astype('float')/t.std(axis=0)
tmsc = np.c_[np.ones((tms.shape[0])), tms]
yhc = fit.predict(tmsc)
t = cleanTest.df.fillna(cleanTest.df.mean(axis=0))
t
tm = t-t.mean(axis=0)
t.mean(axis=0
)
t.std(axis=0)
exclude_columns = ['SalesID','SalePrice', 'NO ROPS', 'None or Unspecified']
t =tdf[[i for i in d.columns if i not in exclude_columns]]
tm = t-t.mean(axis=0)
tms = t.astype('float')/t.std(axis=0)
tmsc = np.c_[np.ones((tms.shape[0])), tms]
yhc = fit.predict(tmsc)
tmsc
t
tm
tm
t
fit = model.fit(x)
fit = model.fit(x,y)
yhc = fit.predict(t)
t.mean(axis=0)
yhc = fit.predict(t)
x
t.count()
t.fillna(t.mean(axis=))
t.fillna(t.mean(axis=0))
t=t.fillna(t.mean(axis=0))
t.count()
x = d[[i for i in d if i not in exclude_columns]]
x = x.fillna(x.mean(axis=0))
model = LinearRegression()
fit = model.fit(x,y)
yh = fit.predict(t)
yh
out_df = pd.DataFrame(data=np.c_[cleanTest.df.SalesID.values, yhc], columns=['SalesID', 'SalePrice'])
cleanTest.df.shape
yhc.shape
t = cleanTest.df.fillna(cleanTest.df.mean(axis=0))
t.shape
yhc = fit.predict(t)
t.shape
yhc.shape
model = LinearRegression()
fit = model.fit(x,y)
x.shape
x.columns
t.columns
yhc = fit.predict(t[t.columns[1:]])
out_df = pd.DataFrame(data=np.c_[cleanTest.df.SalesID.values, yhc], columns=['SalesID', 'SalePrice'])
out_df
out_df.to_csv('lin_reg.csv')
get_ipython().magic(u'pwd ')
out_df = pd.DataFrame(data=np.c_[cleanTest.df.SalesID.values.astype(int), yhc], columns=['SalesID', 'SalePrice'])
out_df = pd.DataFrame(data=np.c_[cleanTest.df.SalesID.values.astype(int), yhc], columns=['SalesID', 'SalePrice'],dtype=['int', 'float'])
out_df = pd.DataFrame(data=np.c_[cleanTest.df.SalesID.values.astype(int), yhc], columns=['SalesID', 'SalePrice'],dtype=['integer', 'float'])
out_df
out = np.c_[cleanTest.df.SalesID.values.astype(int), yhc]
out
out_df = pd.DataFrame(data=np.c_[cleanTest.df.SalesID.values.astype(int), yhc.astype(int)], columns=['SalesID', 'SalePrice'])
out_df.to_csv('lin_reg.csv')
import sklearn
model sklearn.linear_model.Ridge()
model= sklearn.linear_model.Ridge()
fit = model.fit(x,y)
yhc = fit.predict(t[t.columns[1:]])
out = np.c_[cleanTest.df.SalesID.values.astype(int), yhc]
get_ipython().magic(u'pwd ')
get_ipython().magic(u'cd ..')
get_ipython().magic(u'cd regression-case-study/')
get_ipython().magic(u'ls ')
get_ipython().magic(u'cd data/')
out_df = pd.DataFrame(data=np.c_[cleanTest.df.SalesID.values.astype(int), yhc.astype(int)], columns=['SalesID', 'SalePrice'])
out_df.to_csv('lin_reg.csv')
out_df
yhc
model sklearn.linear_model.Ridge(alpha=2)
model= sklearn.linear_model.Ridge(alpha=2)
fit = model.fit(x,y)
yhc = fit.predict(t[t.columns[1:]])
out_df = pd.DataFrame(data=np.c_[cleanTest.df.SalesID.values.astype(int), yhc.astype(int)], columns=['SalesID', 'SalePrice'])
out_df.to_csv('lin_reg.csv')
out_df
model= sklearn.linear_model.Ridge(alpha=10)
from sklearn.ensemble import AdaBoostRegressor
model = AdaBoostRegressor
model = AdaBoostRegressor()
fit = model.fit(x,y)
from sklearn.ensemble import GradientBoostingRegressor
model = GradientBoostingRegressor()
fit = model.fit(x,y)
yhc = fit.predict(t[t.columns[1:]])
out_df = pd.DataFrame(data=np.c_[cleanTest.df.SalesID.values.astype(int), yhc.astype(int)], columns=['SalesID', 'SalePrice'])
out_df.to_csv('lin_reg.csv')
yhc
out_df
model = GradientBoostingRegressor(learning_rate=.005)
fit = model.fit(x,y)
yhc = fit.predict(t[t.columns[1:]])
out_df = pd.DataFrame(data=np.c_[cleanTest.df.SalesID.values.astype(int), yhc.astype(int)], columns=['SalesID', 'SalePrice'])
out_df.to_csv('lin_reg.csv')
model = GradientBoostingRegressor(learning_rate=.5)
fit = model.fit(x,y)
model = GradientBoostingRegressor(max_features='sqrt')
fit = model.fit(x,y)
yhc = fit.predict(t[t.columns[1:]])
out_df = pd.DataFrame(data=np.c_[cleanTest.df.SalesID.values.astype(int), yhc.astype(int)], columns=['SalesID', 'SalePrice'])
out_df.to_csv('lin_reg.csv')
model = AdaBoostRegressor()
fit = model.fit(x,y)
yhc = fit.predict(t[t.columns[1:]])
out_df.to_csv('lin_reg.csv')
out_df = pd.DataFrame(data=np.c_[cleanTest.df.SalesID.values.astype(int), yhc.astype(int)], columns=['SalesID', 'SalePrice'])
out_df.to_csv('lin_reg.csv')
from  sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()
fit = model.fit(x,y)
yhc = fit.predict(t[t.columns[1:]])
out_df = pd.DataFrame(data=np.c_[cleanTest.df.SalesID.values.astype(int), yhc.astype(int)], columns=['SalesID', 'SalePrice'])
out_df.to_csv('lin_reg.csv')
