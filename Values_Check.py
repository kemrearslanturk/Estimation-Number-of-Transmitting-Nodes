# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 18:44:46 2021

@author: Emre
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 23:47:49 2021

@author: Emre
"""

import numpy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from scipy.stats import norm

values = pd.read_excel('NewValues.xlsx') 
list_formula = values['formula'].tolist()
list_simulation = values['simulation'].tolist()

node=values['node'].tolist()
yirmibes=values['yuzyirmibes'].tolist()

st_dev_for = np.std(list_formula)
st_dev_sim = np.std(list_simulation)
print("Standard deviation of the formula list: " + str(st_dev_for))
print("Standard deviation of the simulation list: " + str(st_dev_sim))

mean_for = sum(list_formula) / len(list_formula)
var_for = sum((i - mean_for) ** 2 for i in list_formula) / len(list_formula)

mean_sim = sum(list_simulation) / len(list_simulation)
var_sim = sum((i - mean_sim) ** 2 for i in list_simulation) / len(list_simulation)

print("Variance of the formula list: " + str(var_for))
print("Variance of the simulation list: " + str(var_sim))


x_data = list_formula
y_data = list_simulation


g=0.386096; g= float(g);

j=2

while(j<21):
    
    i=2;
    while (i<21):
            if(yirmibes[j-2]<x_data[i-2]+(2*var_for) and yirmibes[j-2]>x_data[i-2]-(2*var_for)):
                sonuc=i
                print(sonuc)     
                break
            else:
                i=i+1;
    j=j+1;

#%%
import matplotlib.pyplot as plt
# line 1 points
import numpy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from scipy.stats import norm

values = pd.read_excel('heyo.xlsx') 
y1 = values['two'].tolist()
y2 = values['three'].tolist()
y3 = values['four'].tolist()
y4 = values['five'].tolist()
x1 = [25,50,100,125]


z1_1=[0.04228,	0.04228,	0.04228,	0.04228]
z1_2=[0.07772,    0.07772,    0.07772,    0.07772]

# plotting the line 1 points 
plt.plot(x1, y1, label = "Simulation Result")
plt.plot(x1, y2, label = "Simulation Result")
# line 2 points

# plotting the line 2 points 
plt.plot(x1, z1_1, label = "Mean Value -2* Standart Deviation")
plt.plot(x1, z1_2, label = "Mean Value +2* Standart Deviation")
plt.xlabel('time(ms)')
# Set the y axis label of the current axis.
plt.ylabel('probability of collision')
# Set a title of the current axes.
plt.title('Checking of quantization level ')
# show a legend on the plot
plt.legend()
# Display a figure.
plt.show()