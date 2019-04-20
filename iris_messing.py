# Python project - Fintan Hegarty
# April 19th 2019
#  

# References used:
# https://www.dataquest.io/blog/pandas-python-tutorial/
# https://stackoverflow.com/questions/31715119/how-can-i-open-a-website-in-my-web-browser-using-python
# https://www.geeksforgeeks.org/python-pandas-dataframe-sort_values-set-2/
# https://seaborn.pydata.org/examples/horizontal_boxplot.html

import pandas
import webbrowser
import matplotlib.pyplot as plt

# (After remembering to add the header values from iris.names section 7)

iris_data_set=pandas.read_csv("iris.data")

# Want to find the standard deviation, median, mode, mean, max, min, 
# of a given column - maybe ask user to pick? Perhaps too many variables.
# Want to find the correlation between any two columns - user option.

#print(iris_data_set.describe())
#for i in iris_data_set['class'].unique():
##    print(i)
#    filtered_info=iris_data_set[i]
#    print(filtered_info)
##    print(filtered_info.describe())
#

print(iris_data_set.head())

#for i in iris_data_set['class'].unique():
#    prefiltered=iris_data_set['class']==i
#    filtered = iris_data_set[prefiltered]
#    print('\n',i,'\n\n',filtered.describe(),'\n')
#

#for i in range(1,5):
#    for j in ['mean','median','mode','std','max','min']:
#        print(blagh)
#        echo(print('The', j, 'of column', i, 'is', iris_data_set.iloc[i,:].j, sep=''))


# Graphs stuff
#for i in range(0,4):
#    plt.plot(iris_data_set.iloc[:,i])
#
#plt.show()
#    
#plt.plot(iris_data_set.iloc[:,2])
#

# To create a map of Ireland
#sorted_iris=iris_data_set.sort_values(['sepalLength'],ascending=False)
#for i in range(0,4):
#    plt.plot(sorted_iris.iloc[:,i]) 
#
#plt.show()

#webbrowser.open('https://www.youtube.com/watch?v=NdYWuo9OFAw', new=2)

import seaborn as sns

#for i in ['sepalLength','sepalWidth','petalLength','petalWidth']:
#    sns.boxplot(y=i, x='class', data=iris_data_set) 
#    sns.despine()
#    plt.show()
#

for i in iris_data_set['class'].unique():
    prefiltered=iris_data_set['class']==i
    filtered = iris_data_set[prefiltered]
    for j in ['sepalLength','sepalWidth','petalLength','petalWidth']:
        title=i
        plt.title(title)
        x=filtered[j]
        sns.distplot(x)
        plt.show()







 

