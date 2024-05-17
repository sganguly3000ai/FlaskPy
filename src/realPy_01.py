import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import pandas as p
import torch.cuda as cuda
import matplotlib as plt
import sys


class cl_01:
    def __init__(self,l):
        self.l = l

    def getlist(self):
        return self.l
    

class cl_02:

    def __init__(self, T):
        self.T = T

    def getTrans(self):
        tt = self.T.transpose(0,1)
        return tt
    
class cl_03:

    def __init__(self, d):
        self.d = d
        self.l = []

    def getValuesInList(self):
        for k in self.d:
            self.l.append(self.d[k])
        return self.l



