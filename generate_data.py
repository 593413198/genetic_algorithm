#! /opt/anaconda3/bin/python3
# @brief: yield some no-random data for algorithmn test

import os, sys
import pandas as pd
from random import random 

with open('data','a') as file:
	for i in range(pow(10,4)):
		x = random() * 70
		y = random() * 50
		file.write(str(x)+','+str(y)+'\n')
