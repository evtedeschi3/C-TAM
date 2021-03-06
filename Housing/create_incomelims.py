'''This script creates the income limit categories that are used for the logistic regression in Housing_impute.py'''

'''You can find income_limits2014.csv at https://www.hudexchange.info/programs/home/home-income-limits/?filter_Year=2014&filter_=Scope=&filter_State=&programHOME&group=IncomeLmts'''
import numpy as np
import pandas as pd

# Income Limits
income_lim = pd.read_csv("income_limits2014.csv")
income_lim = income_lim.ix[:,'State':'lim50_14p8']
income_lim = income_lim.rename(columns={'State': 'Fips'})
income_lim = income_lim.groupby('statename').mean().astype(int).reset_index()
# 8 person family adds 40 percent of 4 percent family median income 
start9 = 1.4

for i in np.arange(9,15):
	income_lim['Lim30_14p'+ str(i)] = (start9 * income_lim['Lim30_14p4']).astype(int)
	#After 8 person family add 8 percent of previous median income
	start9 += .08

start9_second = 1.4
for i in np.arange(9,15):
	income_lim['lim50_14p'+ str(i)] = (start9_second * income_lim['lim50_14p4']).astype(int)
	start9_second += .08

income_lim.to_csv('Income_limits.csv', index = None)



