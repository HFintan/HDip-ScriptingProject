This is my project for Dr. McLoughlin's programming and scripting course as part of the Higher Diploma in Data Analytics in GMIT. 
https://github.com/ianmcloughlin/project-pands/blob/master/project.pdf

It centres on the analysis of the Fisher's Iris data set.

The python script iris_messing.py contains all of the various bits of code that were 
used to produce these data and figures. They are all commented out, and can be run individually,
so as not to bombard the user. If bombardment is what you're after, the command
:%s/^#//g
in vim should uncomment all the necessary parts at once.

In brief, the script labelled 1 returns max, min, std deviation etc.


The script 2 returns the correlation. 

The script 3 returns, sequentially, a graph for each species, displaying the plants' four attributes together.

Script 4 isn't very useful, but the output looks like a map of Ireland, so I kept it in out of patriotism.

Script 5 opens a youtube tab with Iris by the GooGoo Dolls. Making it play automatically involves a slightly more invasive script than would probably be appreciated, so the user will have to click the play button themselves.

Script 6 gives box plots comparing the four attributes of the various species.

The script iris.pdf contains a copy of the data and images produced by running the scripts.

If there are any questions, please email me at fintan[dot]hegarty[at]gmail[dot]com.


References (alongside those python-specific references listed in comments in iris_messing.py

Wiki page: https://en.wikipedia.org/wiki/Iris_flower_data_set


This data set consists of 50 samples of each of three types of iris, all collected under the same conditions (location, time, measurement apparatus and method) to minimise any unexpected variation in the plant samples.

Four features were measured; length of sepals, length of petals, width of sepals, and width of petals. The species was also noted.


Findings:
The mean, standard deviation, min and max etc, for the entire sample set are as follows.

Sepal length
mean 5.84333, standard deviation 0.828066, min 4.3, max 7.9

Sepal Width
mean 3.054, standard deviation 0.433594, min 2, max 4.4

Petal length
mean 3.758667, standard deviation 1.76442, min 1, max 6.9

Petal width
mean 1.19, standard deviation 0.763161, min 0.1, man 2.5

Further info on the individual species is available in iris.pdf.



Unseparated by class, there appears to be strong correlation between sepal length and petal length (0.871754), and between sepal length and petal width (0.817954), and between petal length and petal width(0.962757). Sepal width, however, seems to not be strongly correlated with anything.
Interestingly, when all the species are taken together, everything appears strongly correlated bar the sepal width, but when the species are taken separately, the correlation is much weaker, which I guess makes sense because the variance, relatively speaking, is smaller. A group of plants comprised of bonzai and a sequoia would exhibit a stronger correlation between branch length and thickness than the sequoia would on their own, for example.


