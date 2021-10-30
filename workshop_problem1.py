from sklearn.datasets import load_iris
iris = load_iris()

import pandas as pd
import numpy as np

iris_nparray = iris.data

iris_dataframe = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_dataframe['group'] = pd.Series([iris.target_names[k] for k in iris.target], dtype="category") 

print (iris_dataframe['sepal length (cm)'].mean())
print (iris_dataframe.mean())
print (iris_dataframe.median())
print (iris_dataframe.std())
print (iris_dataframe.max(numeric_only=True)-iris_dataframe.min())
print (iris_dataframe.quantile(np.array([0,.25,.50,.75,1])))

from scipy.stats import kurtosis, kurtosistest
k = kurtosis(iris_dataframe['petal length (cm)'])
zscore, pvalue = kurtosistest(iris_dataframe['petal length (cm)'])
print ('Kurtosis %0.3f z-score %0.3f p-value %0.3f' % (k, zscore, pvalue))

from scipy.stats import skew, skewtest
s = skew(iris_dataframe['petal length (cm)'])
zscore, pvalue = skewtest(iris_dataframe['petal length (cm)'])
print ('Skewness %0.3f z-score %0.3f p-value %0.3f' % (s, zscore, pvalue))

iris_binned = pd.concat([
pd.qcut(iris_dataframe['sepal length (cm)'], [0, .25, .5, .75, 1]),
pd.qcut(iris_dataframe['sepal width (cm)'], [0, .25, .5, .75, 1]),
pd.qcut(iris_dataframe['petal length (cm)'], [0, .25, .5, .75, 1]),
pd.qcut(iris_dataframe['petal width (cm)'], [0, .25, .5, .75, 1])
], join='outer', axis = 1)

print (iris_dataframe['group'].value_counts())
print (iris_binned['petal length (cm)'].value_counts())
print (iris_binned.describe())
print (pd.crosstab(iris_dataframe['group'], iris_binned['petal length (cm)']))

boxplots = iris_dataframe.boxplot(return_type='axes')

from scipy.stats import ttest_ind

group0 = iris_dataframe['group'] == 'setosa'
group1 = iris_dataframe['group'] == 'versicolor'
group2 = iris_dataframe['group'] == 'virginica'
print ('var1 %0.3f var2 %03f' % (iris_dataframe['petal length (cm)'][group1].var(), iris_dataframe['petal length (cm)'][group2].var()))

t, pvalue = ttest_ind(iris_dataframe['sepal width (cm)'][group1], iris_dataframe['sepal width (cm)'][group2], axis=0, equal_var=False)
print ('t statistic %0.3f p-value %0.3f' % (t, pvalue))

from scipy.stats import f_oneway      
f, pvalue = f_oneway(iris_dataframe['sepal width (cm)'][group0], 
                     iris_dataframe['sepal width (cm)'][group1], 
                     iris_dataframe['sepal width (cm)'][group2])
print ("One-way ANOVA F-value %0.3f p-value %0.3f" % (f,pvalue))

from pandas.plotting import parallel_coordinates
iris_dataframe['group'] = iris.target
iris_dataframe['labels'] = [iris.target_names[k] for k in iris_dataframe['group']]
pll = parallel_coordinates(iris_dataframe,'labels')

densityplot = iris_dataframe[iris_dataframe.columns[:4]].plot(kind='density')
single_distribution = iris_dataframe['petal length (cm)'].plot(kind='hist')

colors_palette = {0: 'red', 1: 'yellow', 2:'blue'}
colors = [colors_palette[c] for c in iris_dataframe['group']]
simple_scatterplot = iris_dataframe.plot(kind='scatter', x='petal length (cm)', y='petal width (cm)', c=colors)

from pandas.plotting import scatter_matrix
colors_palette = {0: "red", 1: "yellow", 2: "blue"}
colors = [colors_palette[c] for c in iris_dataframe['group']]
matrix_of_scatterplots = scatter_matrix(iris_dataframe, figsize=(6, 6), color=colors, diagonal='kde')

print (iris_dataframe.cov())
print (iris_dataframe.corr())

covariance_matrix = np.cov(iris_nparray, rowvar=0, bias=1)
correlation_matrix = np.corrcoef(iris_nparray, rowvar=0, bias=1)

from scipy.stats import spearmanr
from scipy.stats.stats import pearsonr
spearmanr_coef, spearmanr_p = spearmanr(iris_dataframe['sepal length (cm)'], iris_dataframe['sepal width (cm)'])
pearsonr_coef, pearsonr_p = pearsonr(iris_dataframe['sepal length (cm)'], iris_dataframe['sepal width (cm)'])
print ('Pearson correlation %0.3f | Spearman correlation %0.3f' % (pearsonr_coef, spearmanr_coef))

from scipy.stats import chi2_contingency
table = pd.crosstab(iris_dataframe['group'], iris_binned['petal length (cm)'])
chi2, p, dof, expected = chi2_contingency(table.values)
print ('Chi-square %0.2f p-value %0.3f' % (chi2, p))

from sklearn.preprocessing import scale
stand_sepal_width = scale(iris_dataframe['sepal width (cm)'])

from scipy.stats.stats import pearsonr
tranformations = {'x': lambda x: x, '1/x': lambda x: 1/x, 'x**2': lambda x: x**2, 'x**3': lambda x: x**3, 'log(x)': lambda x: np.log(x)}
for transformation in tranformations:
    pearsonr_coef, pearsonr_p = pearsonr(iris_dataframe['sepal length (cm)'], tranformations[transformation](iris_dataframe['sepal width (cm)']))
    print ('Transformation: %s \t Pearson\'s r: %0.3f' % (transformation, pearsonr_coef))


