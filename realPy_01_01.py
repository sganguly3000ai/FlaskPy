import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
import sys
import realPy_01 as myC


'''
g = torch.Generator(torch.device('cpu'))
a = torch.randint(1, 6, (2,3), dtype = torch.int64, generator = g) 
print(a)
print(sys.version)
'''

t = myC.cl_01([1,2,3])

x = torch.tensor([[1,2,3],[2,3,4]])

y = {1:'a', 2:'b', 3:'c'}

t1 = myC.cl_02(x)

t2 = myC.cl_03(y)

myList = t2.getValuesInList()

print(t.l)

print(t1.getTrans())

print(myList)
print(myList)
