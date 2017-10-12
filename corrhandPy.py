# Fall 2017 - Adam Ross Nelson - Modified for python draft.
# Fall 2015 - Adam Ross Nelson - Originally exectued in Stata.
#           - See: https:github.com/adamrossnelson/crossreg/blob/master/corrhandStata.do
# Maintained at: https:github.com/adamrossnelson/crossreg

# Use this do file to calculate the correlation without using -df.corr-
# Can be used to assist when learning hot to calculate by by hand. Or, useful
# when double checking hand work.

import pandas as pd
import math as math
import requests

thedata = {'y':[4,8,6,6,7,3,4,5],
          'x':[1,9,9,4,8,2,4,7]}

df = pd.DataFrame(thedata)

print(df, end=str(chr(13) * 2))

# Individually calculate Y-bar (or Ysubi minus Ybar) | The error terms
df = df.assign(ymybar=df['y'] - df['y'].mean())

# Individually calculate X-bar (or Xsubi minus Xbar) | The error terms
df = df.assign(xmxbar=df['x'] - df['x'].mean())

# Generate the covariances; then use to calculate numerator
# This term is stated as sum of the error terms (from above) multiplied together
df = df.assign(covxy=df['ymybar'] * df['xmxbar'])
cov = df['covxy'].sum()

# Generate squared errors
# The sum of squared error of y is stored in variable -ymy-
df = df.assign(ymybarsq=df['ymybar'] * df['ymybar'])
ymy = df['ymybarsq'].sum()

# The sum of squared error of x is stored in variable -xmx-
df = df.assign(xmxbarsq=df['xmxbar'] * df['xmxbar'])
xmx = df['xmxbarsq'].sum()

# Display the dataframe with additional variables
print(df, end=str(chr(13) * 2))

# Display the results
print('The data correlation ''hand calculated'' results : ', end='')
print((cov)/(math.sqrt(ymy * xmx)), end=str(chr(13) * 2))
print('The data correlation ''python calculated'' results : ' , end='')
print(df['y'].corr(df['x']), end=str(chr(13) * 2))

formulas = requests.get('https://raw.githubusercontent.com/adamrossnelson/crossreg/master/formulas.txt')
print('Provide formula notes for reference:')
print(formulas.text)