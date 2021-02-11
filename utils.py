# some utils and helper functions for library
import pandas as pd 

# 1. generate config from dataframe
	# a. current config is json, but it will change

def generate_config(df, y):
	features = df.columns # drop y
	classes = df[y].unique()
	# max min
	### TODO!!!!