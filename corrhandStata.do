// Fall 2017 - Adam Ross Nelson - Updated.
// Spring 2015 - Adam Ross Nelson - Original draft
// Maintained at: https://github.com/adamrossnelson/crossreg

// Use this do file to calculate the correlation without using -corr- or -pwcorr-
// Can be used to assist when learning hot to calculate by by hand. Or, useful
// when double checking hand work.

set more off
clear all

set obs 8
generate y = 3 in 1
replace y = 7 in 2
replace y = 6 in 3
replace y = 6 in 4
replace y = 6 in 5
replace y = 3 in 6
replace y = 3 in 7
replace y = 6 in 8

generate x = 2 in 1
replace x = 10 in 2
replace x = 9 in 3
replace x = 5 in 4
replace x = 8 in 5
replace x = 2 in 6
replace x = 4 in 7
replace x = 8 in 8

// List (display) the original data
list

// Individually calculate Y-Ybar (or Ysubi minus Ybar) | The error terms
sum y
gen ymybar = y - r(mean)          // Generate Y-Ybar variable
// Individually calculate X-Xbar (or Xsubi minus xbar)
sum x
gen xmxbar = x - r(mean)          // Generate X-XBar variable

// Generate the covariances; then use to calculate numerator
// This term is stated as sum of the error terms (from above) multiplied together
gen covxy = ymybar * xmxbar       // Generate covariances
sum covxy                         // Find total
// The local -cov- stores the sum of the covariances, the numerator
local cov = r(sum)				  // Save to local for later reference

// Generate squared errors
gen ymybarsq = ymybar * ymybar    // Generate YBar^2 squared
sum ymybarsq                      // Find total
// The squared error of y is stored in local -ymy-
local ymy = r(sum)				  // Save to local for later reference

gen xmxbarsq = xmxbar * xmxbar    // Generate XBar^2 squared
sum xmxbarsq                      // Find total
// The squared error of x is stored in local -xmx-
local xmx = r(sum)                // Save to local for later reference

// List (display) the data with additional variables
list

// Display the results of the calculation.
di %-12.4g (`cov') / sqrt(`xmx' * `ymy')

// Double check the work with existing Stata command.
pwcorr y x

di "Provide notes for reference : "
scalar formulas = fileread("https://raw.githubusercontent.com/adamrossnelson/crossreg/master/formulas.txt")
di formulas
