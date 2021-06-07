import pandas as pd
import math
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
import numpy as np

# load in CSV files
electionData = pd.read_csv('election-data.csv')
stateName = pd.read_csv('state-abbr.csv')
usVacc = pd.read_csv('us_state_vaccinations.csv')

# print out data to confirm data was succesfully read into the system
print(electionData.head(1))
print(stateName.head(1))
print(usVacc.head(1))

# write a Python function w/state name, DF column inputs & returns DF column indexed by date
def curveFit(columnName, state):
    state_filter = usVacc[usVacc['location'] == state]
    state_filter.set_index('date')
    col_data = state_filter[columnName]
    return col_data

# plot one such series as example
column = 'people_vaccinated'
state = 'Alabama'
curveSeries = curveFit(column, state)
curveSeries.fillna(0)
plt.scatter(curveSeries.index, curveSeries)
print(curveSeries)
# plt.title('Vaccinations over Time (in days)')
# plt.ylabel('Vaccinations')
# plt.xlabel('Days')
# plt.show()

# many_xs = np.linspace(2, 5, 100)

# def curve_model(x, β0, β1, β2):
#     return β0 / (1 + math.exp(β1*(-x + β2)))

# my_guessed_betas = [3, 1, (0.5*len(usVacc['date']))]
# found_betas, covariance = curve_fit(curve_model, xdata=curveSeries.index, ydata=curveSeries)
# β0, β1, β2 = found_betas
# fit_model = lambda x: curve_model(x, β0, β1, β2)
# plt.scatter(curveSeries.index, curveSeries)
# plt.plot(many_xs, fit_model(many_xs))
# plt.show()
