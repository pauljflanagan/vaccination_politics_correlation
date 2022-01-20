# Statistical Analysis of Vaccination Data

## Vaccination data
This project took in national U.S. vaccination data (sourced from https://github.com/owid/covid-19-data), which detailed the percent of each state's population that was fully vaccinated, as of 07/01/2021. This data was processed using the Pandas library to read in the CSV file.

The corresponding Jupyter notebook that analyzes this data can be found [here](https://pauljflanagan.github.io/vaccination_politics_correlation/ "Vaccination Jupyter Notebook").

### Partial data analysis
From this, a function was generated to take in a given metric and state, giving an output of a graph of that statistic's evolution over time.

## Correlation mapping
After creating a function that generates the statistical betas of a given statistic from a predetermined state, the notebook iterates over each statistic from each state to create a dictionary of every U.S. state. Each state entry has corresponding fields listing the beta values of the state's data: the most vaccinated in one day by the state, the state's rate of vaccination (how many were vaxxed a day), and the largest change in vaccination rate respectively.

## Political data
This data was combined with data from the 2016 presidential election (sourced from https://www.npr.org/2016/11/08/500927768/2016-presidential-election-results-for-each-state, formatted to fit U.S. state list sourced from http://www.50states.com/abbreviations.htm). This data was processed in the same fashion as the vaccination data was.

## Correlation and conclusion
Both of these data groupings were combined using the Pandas DataFrame setup. The resulting DataFrame was used to create a correlation graph through the Seaborn library, with the correlation coefficients being derived through the NumPy library.

The combined DataFrame was tested against a significance value of 0.05 to determine if the correlations from the Seaborn library were statistically significant enough to warrant a hypothesis test, which was found to not be the case.

Link to DeepNote notebook for those who prefer:
https://deepnote.com/@paul-flanagan/MA346-Project-1-Z3rMzJ_OS5mNA48mB5oH2g
