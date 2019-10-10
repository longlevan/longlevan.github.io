import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
import pandas as pd



# SSB2018
## Pie chart: EU28_Econso_sector (2016) to plot source: https://pythonspot.com/matplotlib-pie-chart/
EU28_Econso_sector = {
    'labels' : ['Industry', 'Transport', 'Household','Services', 'Agriculture/', 'Other'], # Tuple
    'sizes' : [276823, 367272, 284832, 150043, 24079, 4769], 
    'explode' : [0, 0, 0.1, 0,0,0] # explode 1st slice
}
plt.pie(EU28_Econso_sector['sizes'], explode=EU28_Econso_sector['explode'],labels=EU28_Econso_sector['labels'], autopct='%1.1f%%', pctdistance=1.1,labeldistance=1.25)
plt.show()


## Bar chart: EU28_Econso_sector (2016) to plot
EU28_Econso_sector = {
    'labels' : ['Industry', 'Transport', 'Household','Services', 'Agriculture/', 'Other'], # Tuple
    'sizes' : [276823, 367272, 284832, 150043, 24079, 4769], 
    'explode' : [0, 0, 0.1, 0,0,0] # explode 1st slice
}
plt.pie(EU28_Econso_sector['sizes'], explode=EU28_Econso_sector['explode'],labels=EU28_Econso_sector['labels'], autopct='%1.1f%%', pctdistance=1.1,labeldistance=1.25)
plt.show()


## Bel_Econso_sector (2016) to plot
BEL_Econso_sector = {
    'labels' : ['Industry', 'Transport', 'Household','Services', 'Agriculture', 'Other'], # Tuple
    'sizes' : [12209,  10514,  8135, 4656, 773, 46], 
    'explode' : [0, 0, 0.1, 0,0,0] # explode 1st slice
}
plt.pie(BEL_Econso_sector['sizes'], explode=BEL_Econso_sector['explode'],labels=BEL_Econso_sector['labels'], autopct='%1.1f%%', pctdistance=1.1,labeldistance=1.25)
plt.axis('on')
plt.show()

# Stacked bar plot: Final energy consumption
"Data preparation"
raw_data = {'Industry':[276823,12209], 
            'Transport':[367272,10514],
            'Household':[284832,8135],
            'Services':[150043,4656], 
            'Agriculture':[24079,773],
            'Other':[4769,46]}
df = pd.DataFrame(raw_data)

"From raw value to percentage"
totals  = [a+b+c+d+e+f for a,b,c,d,e,f in zip(df['Industry'],df['Transport'],df['Household'],df['Services'],df['Agriculture'],df['Other'])]
Industry = [float(i)/float(j)*100.0 for i, j in zip(df['Industry'],totals)]
Transport = [float(i)/float(j)*100.0 for i, j in zip(df['Transport'],totals)]
Household = [float(i)/float(j)*100.0 for i, j in zip(df['Household'],totals)]
Services = [float(i)/float(j)*100.0 for i, j in zip(df['Services'],totals)]
Agriculture = [float(i)/float(j)*100.0 for i, j in zip(df['Agriculture'],totals)]
Other = [float(i)/float(j)*100.0 for i, j in zip(df['Other'],totals)]

"The position of the bars on the x-axis"
barPos = [0,1]
"Names of group and bar width"
barNames = ['EU28', 'Belgium']
barWidth = 0.85

plt.bar(barPos,Industry,width = barWidth,label = 'Industry')
plt.bar(barPos,Transport,bottom = Industry, width = barWidth,label = 'Transport')
plt.bar(barPos,Household,bottom = [i+j for i,j in zip(Industry,Transport)],width = barWidth,label = 'Household')
plt.bar(barPos,Services,bottom = [i+j+k for i,j,k in zip(Industry,Transport,Household)],width = barWidth,label = 'Services')
plt.bar(barPos,Agriculture,bottom = [i+j+k+t for i,j,k,t in zip(Industry,Transport,Household,Services)],width = barWidth,label='Agriculture/Forestry')
plt.bar(barPos,Other,bottom = [i+j+k+t+u for i,j,k,t,u in zip(Industry,Transport,Household,Services,Agriculture)],width = barWidth,label='Other')

plt.title("Final Energy Consumption",fontsize = 18,fontweight = 'bold')
plt.legend(loc = 'upper left',bbox_to_anchor=(1,0.9),ncol = 1,fontsize = 18)
plt.xticks(barPos,barNames,fontsize = 18,fontweight = 'bold')
plt.ylabel('[%]', fontsize = 18,fontweight = 'bold')
plt.yticks(fontsize = 18,fontweight = 'bold')
plt.show()

# Stacked bar plot: Final energy consumption by type
"Data preparation"
raw_data = {'solid_fuels':[45338,1748], 
            'petroleum_products':[437131,15298],
            'gas':[245284,9726],
            're_wastes':[92729,2026],
            'elec': [239405,7038],
            'derived_heat':[47932,498]}
df = pd.DataFrame(raw_data)

"From raw value to percentage"
totals  = [a+b+c+d+e+f for a,b,c,d,e,f in zip(df['solid_fuels'],df['petroleum_products'],df['gas'],df['re_wastes'],df['elec'],df['derived_heat'])]
solid_fuels = [float(i)/float(j)*100.0 for i, j in zip(df['solid_fuels'],totals)]
petroleum_products = [float(i)/float(j)*100.0 for i, j in zip(df['petroleum_products'],totals)]
gas = [float(i)/float(j)*100.0 for i, j in zip(df['gas'],totals)]
re_wastes = [float(i)/float(j)*100.0 for i, j in zip(df['re_wastes'],totals)]
elec = [float(i)/float(j)*100.0 for i, j in zip(df['elec'],totals)]
derived_heat = [float(i)/float(j)*100.0 for i, j in zip(df['derived_heat'],totals)]

"The position of the bars on the x-axis"
barPos = [0,1]
"Names of group and bar width"
barNames = ['EU28', 'Belgium']
barWidth = 0.85

fig = plt.figure()
ax = fig.add_subplot(111)
plt.bar(barPos,solid_fuels,width = barWidth,label = 'Solid Fossil Fuels')
plt.bar(barPos,petroleum_products,bottom = solid_fuels, width = barWidth,label = 'Petroleum Products')
plt.bar(barPos,gas,bottom = [i+j for i,j in zip(solid_fuels,petroleum_products)],width = barWidth,label = 'Gas')
plt.bar(barPos,re_wastes,bottom = [i+j+k for i,j,k in zip(solid_fuels,petroleum_products,gas)],width = barWidth,label = 'Renewable Energies & Wastes')
plt.bar(barPos,elec,bottom = [i+j+k+t for i,j,k,t in zip(solid_fuels,petroleum_products,gas,re_wastes)],width = barWidth,label='Electricity')
plt.bar(barPos,derived_heat,bottom = [i+j+k+t+u for i,j,k,t,u in zip(solid_fuels,petroleum_products,gas,re_wastes,elec)],width = barWidth,label='Derived Heat')
plt.title("Final Energy Consumption",fontsize = 18,fontweight = 'bold')
plt.legend(loc = 'upper left',bbox_to_anchor=(1,1),ncol = 1,fontsize = 18)
plt.xticks(barPos,barNames,fontsize = 18,fontweight = 'bold')
plt.ylabel('[%]', fontsize = 18,fontweight = 'bold')
# ax.yaxis.tick_right()
plt.yticks(fontsize = 18,fontweight = 'bold')
plt.show()


# Stacked bar plot: Final energy consumption by type of end-use
"Data preparation"
raw_data = {'space_heating':[64.6,73.3], 
            'space_cooling':[0.3,0.1],
            'water_heating':[14.5,11.6],
            'cooking':[5.5,1.7],
            'lighting_appliances': [13.8,13],
            'other':[1.3,0.4]}
df = pd.DataFrame(raw_data)

"From raw value to percentage"
totals  = [a+b+c+d+e+f for a,b,c,d,e,f in zip(df['space_heating'],df['space_cooling'],df['water_heating'],df['cooking'],df['lighting_appliances'],df['other'])]
space_heating = [float(i)/float(j)*100.0 for i, j in zip(df['space_heating'],totals)]
space_cooling = [float(i)/float(j)*100.0 for i, j in zip(df['space_cooling'],totals)]
water_heating = [float(i)/float(j)*100.0 for i, j in zip(df['water_heating'],totals)]
cooking = [float(i)/float(j)*100.0 for i, j in zip(df['cooking'],totals)]
lighting_appliances = [float(i)/float(j)*100.0 for i, j in zip(df['lighting_appliances'],totals)]
other = [float(i)/float(j)*100.0 for i, j in zip(df['other'],totals)]

"The position of the bars on the x-axis"
barPos = [0,1]
"Names of group and bar width"
barNames = ['EU28', 'Belgium']
"The width of the bars"
barWidth = 0.85

fig = plt.figure()
ax = fig.add_subplot(111)
plt.bar(barPos,space_heating,width = barWidth,label = 'Space Heating')
plt.bar(barPos,space_cooling,bottom = space_heating, width = barWidth,label = 'Space Cooling')
plt.bar(barPos,water_heating,bottom = [i+j for i,j in zip(space_heating,space_cooling)],width = barWidth,label = 'Water Heating')
plt.bar(barPos,cooking,bottom = [i+j+k for i,j,k in zip(space_heating,space_cooling,water_heating)],width = barWidth,label = 'Cooking')
plt.bar(barPos,lighting_appliances,bottom = [i+j+k+t for i,j,k,t in zip(space_heating,space_cooling,water_heating,cooking)],width = barWidth,label='Lighting')
plt.bar(barPos,other,bottom = [i+j+k+t+u for i,j,k,t,u in zip(space_heating,space_cooling,water_heating,cooking,lighting_appliances)],width = barWidth,label='Other')

plt.title("Energy Consumption in Household",fontsize = 18,fontweight = 'bold')
plt.legend(loc = 'lower right',bbox_to_anchor=(0,0.1),ncol = 1,fontsize = 18)
plt.xticks(barPos,barNames,fontsize = 18,fontweight = 'bold')
plt.ylabel('[%]', fontsize = 18,fontweight = 'bold')
ax.yaxis.tick_right()
ax.yaxis.set_label_position('right')
plt.yticks(fontsize = 18,fontweight = 'bold')
plt.show()