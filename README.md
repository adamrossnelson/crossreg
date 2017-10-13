# crossreg
## Introduction
This project is designed to provide an applied crosswalk between Stata, R, and Python. Other crosswalks provide a list of columns with equivalent code snippits. This crosswalk aims to provide similar projects in different environments. Aside from being useful as a crosswalk this project can be useful in teaching and/or learning first semester statistics.

First demonstrates and implements correlation calculations in each environment. See the file series `coorhandStata.do coorhandPy.py corrhandR.r`. In Stata enter the following command for a demonstration (no downloads necessary):

```Stata
do https://raw.githubusercontent.com/adamrossnelson/crossreg/master/corrhandStata.do
```
In R use the following command for a demonstration (no downloads necessary):
```R
source("https://raw.githubusercontent.com/adamrossnelson/crossreg/master/corrhandR.r")
```

Second, demonstrates/Implements OLS regression calculations in each environment. See the file series `reghandStata.do reghandPy.py reghandR.r`.

For a similar, but far less technical, example see:

[BadgerGameday](https:github.com/adamrossnelson/BadgerGameday)

## Other Similar References

Over @vikjam replicated, in three ways, tables from [Mostly Harmless Econometrics](http://www.mostlyharmlesseconometrics.com/). Check it out at [Mostly Harmless Replication](https://github.com/vikjam/mostly-harmless-replication). A two-way dictionary with a growing number of entries compares common Stata and R code and conventions. Originally it was an April 1st fool's joke. But, the dictionary is useful at [RStata](https://github.com/EconometricsBySimulation/RStata).

## Questions, Comments, Hatemail
Send me your questions, comments, and tell me what I did wrong.

Fork and pull requests welcome.
