import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('leagueoflegends/LeagueofLegends.csv')
data.head()
sections = ['Top', 'Jungle', 'Middle', 'ADC', 'Support']
num_sections = len(sections)

for i in range(num_sections):
    plt.figure(i)
    plt.plot(goldData[goldData.NameType == 'goldblue' + sections[i]].groupby('minute').gold.mean(), 'b-')
    plt.plot(goldData[goldData.NameType == 'goldred' + sections[i]].groupby('minute').gold.mean(), 'r-')
    plt.xlabel('Minute')
    plt.ylabel('Gold')
    plt.title(sections[i])