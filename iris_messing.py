## Python project - Fintan Hegarty
## April 19th 2019
##  

## References used:
## https://www.dataquest.io/blog/pandas-python-tutorial/
## https://stackoverflow.com/questions/31715119/how-can-i-open-a-website-in-my-web-browser-using-python
## https://www.geeksforgeeks.org/python-pandas-dataframe-sort_values-set-2/
## https://seaborn.pydata.org/examples/horizontal_boxplot.html
## https://stackoverflow.com/questions/3253966/python-string-to-attribute
## https://matplotlib.org/api/_as_gen/matplotlib.pyplot.legend.html

import pandas
import webbrowser
import matplotlib.pyplot as plt

## (After remembering to add the header values from iris.names section 7)

iris_data_set=pandas.read_csv("iris.data")

## Give the standard deviation, median, mode, mean, max, min of a given column.
## .describe gives most of these, but can also use something like the following:

## 1.
## for i in range(1,5):
##   for j in ['median','mode']:
##        we_want = str(iris_data_set.iloc[i,:].median)
##        print('The', j, 'of column', i, 'is', we_want, sep=' ')
## This is giving some weird junk along with the correct answer, so I'll leave it out.
## It also gives the same weird junk for
##       print('The median of column', i, 'is', iris_data_set.iloc[i,:].median, sep=' ')
## so it doesn't appear to be an issue with looping through the list rather than doing
## each attribute separately

#print(iris_data_set.describe())
#
#for i in iris_data_set['class'].unique():
#    prefiltered=iris_data_set['class']==i
#    filtered = iris_data_set[prefiltered]
#    print('\n',i,'\n\n',filtered.describe(),'\n')
#


## 2.
## Want to find the correlation between any two columns
    
#print("Total correlation\n")
#print(iris_data_set.corr())
#
#for i in iris_data_set['class'].unique():
#    prefiltered=iris_data_set['class']==i
#    filtered = iris_data_set[prefiltered]
#    print('\n',i,'\n\n',filtered.corr(),'\n')


## 3.
## Graphs the various values, separated by species.

#attribs=['sepal length','sepal width','petal length','petal width']
#markers=['o','^','s','x']
#
#for i in iris_data_set['class'].unique():
#    prefiltered=iris_data_set['class']==i
#    filtered = iris_data_set[prefiltered]
#    title = i
#    for j in range(0,4):
#        plt.plot(filtered.iloc[:,j], label=attribs[j], marker=markers[j])
#        plt.title(title)
#        legend= plt.legend(loc = 'upper left')
#    plt.show()
## I thought sorting by sepal length or one of the others would make it easier
## to see correlation etc, but the multiple instances of the same number
## mean the resulting chart is junk
##    sorted_iris=iris_data_set.sort_values(['sepalLength'],ascending=True)
 

## 4. 
## To create a surprising map of Ireland
#sorted_iris=iris_data_set.sort_values(['sepalLength'],ascending=False)
#for i in range(0,4):
#    plt.plot(sorted_iris.iloc[:,i]) 
#
#plt.show()

## 5.
## Opens IRIS by the GooGoo Dolls. Can't get it to play automatically without forcing
## a package download on the user's machine, which would probably be frowned upon.
#webbrowser.open('https://www.youtube.com/watch?v=NdYWuo9OFAw', new=2)

## 6.  
#import seaborn as sns

#for i in ['sepalLength','sepalWidth','petalLength','petalWidth']:
#    sns.boxplot(y=i, x='class', data=iris_data_set) 
#    sns.despine()
#    plt.show()


#for i in iris_data_set['class'].unique():
#    prefiltered=iris_data_set['class']==i
#    filtered = iris_data_set[prefiltered]
#    for j in ['sepalLength','sepalWidth','petalLength','petalWidth']:
#        title=i
#        plt.title(title)
#        x=filtered[j]
#        sns.distplot(x)
#        plt.show()







 

