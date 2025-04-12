import pandas as pd
import os

import os


"""script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "Project1/data/DEN_weather_raw.csv"
abs_file_path = os.path.join(script_dir, rel_path)

print(abs_file_path)"""

# Get the absolute path of the current file
abspath = os.path.abspath(__file__)

# Get the directory name
dname = os.path.dirname(abspath)

# Change the current working directory
os.chdir(dname)

# Verify the current working directory (optional)
print("Current working directory:", os.getcwd())


# import csv file as pandas dataframe
path = f'.\data\DEN_weather_raw.csv'
df = pd.read_csv(path)

print(df.head())