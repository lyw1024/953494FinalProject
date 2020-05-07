import pandas as pd
import matplotlib.pyplot as plt
from bokeh.plotting import figure, output_file, show
from collections import Counter
from bokeh.models import ColumnDataSource



data2 = pd.read_csv('/Users/almostloverv/Desktop/953494FinalProject/LeagueofLegends.csv',
                   usecols=['Year','goldblue','goldred','goldblueSupport','goldredSupport',])

gold_2015 = 0
gold_2016 = 0
gold_2017 = 0
gold_2018 = 0
count_2015 = 0
count_2016 = 0
count_2017 = 0
count_2018 = 0
supp_2015 = 0
supp_2016 = 0
supp_2017 = 0
supp_2018 = 0
data2_list = data2.values.tolist()
for each in data2_list:
    if(each[0]) == 2015:
        gold_2015 += int(each[1].split(',')[-1][:-1])
        supp_2015 += int(each[-1].split(',')[-1][:-1])
        count_2015 += 1
    if (each[0]) == 2016:
        gold_2016 += int(each[1].split(',')[-1][:-1])
        supp_2016 += int(each[-1].split(',')[-1][:-1])
        count_2016 += 1
    if (each[0]) == 2017:
        gold_2017 += int(each[1].split(',')[-1][:-1])
        supp_2017 += int(each[-1].split(',')[-1][:-1])
        count_2017 += 1
    if (each[0]) == 2018:
        gold_2018 += int(each[1].split(',')[-1][:-1])
        supp_2018 += int(each[-1].split(',')[-1][:-1])
        count_2018 += 1

avg_2015 = gold_2015/count_2015/5
avg_2016 = gold_2016/count_2016/5
avg_2017 = gold_2017/count_2017/5
avg_2018 = gold_2018/count_2018/5

avg_supp_2015 = supp_2015/count_2015
avg_supp_2016 = supp_2016/count_2016
avg_supp_2017 = supp_2017/count_2017
avg_supp_2018 = supp_2018/count_2018

y1 = [avg_2015, avg_2016, avg_2017, avg_2018]
y2 = [avg_supp_2015, avg_supp_2016, avg_supp_2017, avg_supp_2018]

# print(y1)
# print(y2)
output_file("lol2.html")

source = ColumnDataSource(data=dict(
    y=[2015, 2016, 2017, 2018],
    x1=y1,
    x2=y2,
))
p2 = figure(plot_width=400, plot_height=400)

p2.hbar_stack(['x1', 'x2'], y='y', height=0.4, color=("red", "blue"), source=source)

show(p2)