# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 19:30:14 2019

@author: SCU
"""


#Imports
import glob
import pandas as pd
import datetime as dt

# Relative path to all the data files
file_path_names = glob.glob('datos/precios/*')
files_list = []

# Read all the files and get them into a single dataframe
for file_path in file_path_names:
    dataframe = pd.read_excel(file_path, header=2, usecols="A:Y")
    files_list.append(dataframe)

dataset = pd.concat(files_list)

# Transform "Fecha" values to ordinal numbers for model predictions
dataset["Fecha"] = pd.to_datetime(dataset["Fecha"])
dataset['Fecha'] = dataset['Fecha'].map(dt.datetime.toordinal)
dataset = dataset.set_index('Fecha', append=False)

# Calculate mean for each day, omiting NA values
dataset['mean'] = dataset.mean(axis=1)
dt.datetime.toordinal(dt.datetime.today())

training_data = dataset["mean"]

date_and_mean_data = training_data.to_dict()
mean_values = training_data.tolist()
date_values = dataset.index.tolist()

date_and_mean_data[729019]
