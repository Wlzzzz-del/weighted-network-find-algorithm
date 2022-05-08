# update in 2022/5/8
the code of algorithm in paper: [Set pair three-way overlapping community discovery algorithm for weighted social internet of things](https://www.sciencedirect.com/science/article/pii/S2352864822000530)  
I totally finish the test, but I dont get the name of author, so I decide share these code.  
but maybe sth. wrong in this code...

# What is weighted network find algorithm  
It is a algorithm to process the network data ,after processing the data will be divide to several communities(a community have several nodes and edges),and the algorithm also get the set of overlapping nodes(just means the nodes can be included in different communities)

# libraries  
The algorithm is based on python  
Use networkx.pandas.numpy.math.collections
```python
import numpy as np
import pandas as pd
import networkx as nx
import math
from collections import defaultdict
```
# algorithm  
it seperate the process two steps.One step is seperate the important nodes to be the center of cluster. then check out another node's correlation. Base on the correlation add them to cluster.

# some problem 
The proposed algorithm simply integrates exist similarity measure, K-means clustering algorithm and set pair theory. The motivation of this study is not clear. 

# about this project  
it is from one teammate's article. But in some reasons, the article did not be publish. I uploading this project for recording the problem.  
as you see the comlexity is too large, and the code is not strong, maybe i will fix them someday. 

# how to assess the algorithm  
I will give some other compared algorithm like cpm,conga,lfm and so on and get their Modularity to compare their effect.

# datasets
+ cond-mat-2003
+ dolphins
+ football
+ hep-th
+ karate
+ lesmis
+ netscience
+ polbooks

# about me
email:wu_lizhao@yeah.net  
wechat: xxscoder
