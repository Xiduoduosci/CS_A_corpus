import os
import pandas as pd

#疾病字典构建

path = "C:/Users/Wenxi Wang/Desktop/acu_en"

acupoint_list = []

for filename in os.listdir(path):
    acupoint_list.append(filename.split('.')[0].lower())

pd.DataFrame(acupoint_list).to_csv('acupoint.csv')
