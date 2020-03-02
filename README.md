# What is weighted network find algorithm  
It is a algorithm to process the network data ,after processing the data will be divide to several communities(a community have several nodes and edges),and the algorithm also get the set of overlapping nodes(just means the nodes can be included in different communities)

# about algorithm  
The algorithm is based on python  
Use networkx.pandas.numpy.math.collections
```python
import numpy as np
import pandas as pd
import networkx as nx
import math
from collections import defaultdict
```
# how to assess the algorithm  
I will give some other compared algorithm like cpm,conga,lfm and so on and get their Modularity to compare their effect.

# datasets
cond-mat-2003,dolphins,football,hep-th,karate,lesmis,netscience,polbooks
