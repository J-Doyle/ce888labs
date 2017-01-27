import matplotlib
matplotlib.use('Agg')

import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np 




def boostrap(statistic_func, iterations, data):
	samples  = np.random.choice(data,replace = True, size = [iterations, len(data)])
	#print samples.shape
	data_mean = data.std()
	vals = []
	for sample in samples:
		sta = statistic_func(sample)
		#print sta
		vals.append(sta)
	b = np.array(vals)
	#print b
	lower, upper = np.percentile(b, [2.5, 97.5])
	return data_mean,lower, upper



if __name__ == "__main__":
	df = pd.read_csv('./vehicles_current.csv')

	data = df.values.T[1]
	boots = []

	boot = boostrap(np.std, 10000, data)
	print ("Current_Fleet_std: %f")%(np.std(data))
	print ("Current_Fleet_lower: %f")%(boot[1])
	print ("Current_Fleet_upper: %f")%(boot[2])

	df = pd.read_csv('./vehicles_new.csv')

	data = df.values.T[1]
	boots = []

	boot = boostrap(np.std, 10000, data)
	print ("New_Fleet_std: %f") % (np.std(data))
	print ("New_Fleet_lower: %f") % (boot[1])
	print ("New_Fleet_upper: %f") % (boot[2])

	# boots.append([10000,boot[0], "mean"])
	# boots.append([10000,boot[1], "lower"])
	# boots.append([10000,boot[2], "upper"])



	#print ("Mean: %f")%(np.mean(data))
	#print ("Var: %f")%(np.var(data))
	


	