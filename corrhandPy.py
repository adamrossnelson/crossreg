import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import math as math

thedata = {'y':[4,8,6,6,7,3,4,5],
          'x':[1,9,9,4,8,2,4,7]}

df = pd.DataFrame(thedata)

print(df)

# Individually calculate Y-bar (or Ysubi minus Ybar) | The error terms
ymean = df['y'].mean()
df = df.assign(ymybar=df['y'] - ymean)

# Individually calculate Y-bar (or Ysubi minus Ybar) | The error terms
xmean = df['x'].mean()
df = df.assign(xmxbar=df['x'] - xmean)

# Generate the covariances; then use to calculate numerator
# This term is stated as sum of the error terms (from above) multiplied together
df = df.assign(covxy=df['ymybar'] * df['xmxbar'])
cov = df['covxy'].sum()

# Generate squared errors
df = df.assign(ymybarsq=df['ymybar'] * df['ymybar'])
# The squared error of y is stored in variable -ymy-
ymy = df['ymybarsq'].sum()

df = df.assign(xmxbarsq=df['xmxbar'] * df['xmxbar'])
# The squared error of y is stored in variable -xmx-
xmx = df['xmxbarsq'].sum()

# Display the results
print('The data correlation ''hand calculated'' results : ', end='')
print((cov)/(math.sqrt(ymy * xmx)), end=str(chr(13) * 2))
print('The data correlation ''python calculated'' results : ' , end='')
print(df['y'].corr(df['x']), end=str(chr(13) * 2))

formulas = open('formulas.txt')
print(formulas.read())