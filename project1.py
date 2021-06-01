import pandas as pd
import numpy as np

# read in vaccination csv file
df = pd.read_csv('us_state_vaccinations.csv')
# read in vaccination data for later analysis

# Fix date column
df['date'] = pd.to_datetime(df['date'])
# datatype correction

def extract_data(state, column):
    return df[df['location'] == state].drop( columns='location' ).set_index( 'date' )[column]

extract_data('Alabama', 'people_vaccinated')

def logistic_curve ( x, β0, β1, β2 ):
    return β0 / ( 1 + np.exp( β1*(-x+β2) ) )

logistic_curve()