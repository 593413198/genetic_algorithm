#! /opt/anaconda3/bin/python3
#! /usr/local/bin/python3
# @enviro: python3
# @brief: 爬山算法de实现

"""
case 1: calculate maximum of a function
case 2: find closest point to 3*10^7 points in file data
"""

import pandas as pd
from numpy import arange as range
from numpy import sqrt, square
from random import random
from math import e

node = None
RangeX, RangeY = [0,100], [0,100]

def yield_node(n):
	""" 用于随机产生n个node的坐标,以测试代码 """
	global node
	node = pd.DataFrame([random()*100, random()*100] for i in range(n))


def Eval(Node):
	""" 计算距离之和 """
	x, y = Node[0], Node[1]
	def dist(X):
		return sqrt((square(X[0]-x) + square(X[1]-y) ))
	result = node.apply(dist,axis=1)
	return result.sum()

def violent_search(step):
	""" 暴力搜索,step用来控制搜索的精度 """
	area = pd.Series([i,j] for i in range(RangeX[0],RangeX[1],step) for j in range(RangeY[0],RangeY[1],step))
	value = area.apply(Eval)
	print(min(value))
	return min(value)

def yield_start():
	""" yield start point """
	return [random() *6-2, random() *6-2]

def neigh(Node, step):
	""" return neighbour of (x,y) """
	x, y  = Node[0], Node[1]
	return [[x, y+step], [x, y-step], [x+step, y], [x-step, y]]

def climb(Node, step):
	""" find best in his neighbour and choose that one """
	value = Eval(Node)
	print(value)
	area = neigh(Node, step)
	# drop area that out of Range
	for i in area:
		if i[0] < RangeX[0] or i[0] > RangeX[1] or i[1] < RangeY[0] or i[1] > RangeY[1]:
			area.remove(i)
	all_value = [Eval(a) for a in area]
	max_value = min(all_value)
	max_index = all_value.index(max_value)
	if value < max_value: # cannot find better one in his neighbour
		return Node,value
	else:
		climb(area[max_index], step)

def hill_climbing(step):
	start = yield_start()
	climb(start,step)

if __name__ == "__main__":
	# read data first
	with open('data','r') as file:
		node = pd.read_csv(file)
	#violent_search(10)
	hill_climbing(1)


