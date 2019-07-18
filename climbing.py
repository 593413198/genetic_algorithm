#! /usr/local/bin/python3
# @enviro: python3
# @brief: 爬山算法de实现

"""
POJ 2420
给出n(n<=100)个点，找平面上一个点使得这个点到所有点的距离最小
"""

import pandas as pd
from numpy import arange as range
from random import random

node = None

def yield_node(n):
    """ 用于随机产生n个node的坐标,以测试代码 """
    global node
    node = pd.DataFrame([random()*100, random()*100] for i in range(n))

def calcul_dist(x, y):
    """ 计算距离之和 """
    return sum([pow(x-node[0][i],2) + pow(y-node[1][i],2) for i in range(node.shape[0])])

def violent_search(step):
    """ 暴力搜索,step用来控制搜索的精度 """
    min_dist = 100000000
    min_x, min_y = 0,0
    for i in range(0,100,step):
        for j in range(0,100,step):
            dist = calcul_dist(i, j)
            if dist < min_dist:
                min_dist = dist
                min_x, min_y = i, j
    return (min_x, min_y, min_dist)

if __name__ == '__main__':
    yield_node(30)
    print(violent_search(1))
    

