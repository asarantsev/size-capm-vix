This is for the manuscript with Abraham Atsiwo titled 

Capital Asset Pricing Model with Size Factor and Normalizing by Volatility Index. 

size-break-points.xlsx shows size breakpoints at capitalizations 5%, 10%, ..., 90%, 95%, for each month from December 1925 to October 2024. size-break-points.py plots related capital distribution curves for December 1925, 1945, 1965, 1985, 2005. 

equity-premia.py has analysis for equity premia and their normalized versions: plotting quantile-quantile plots versus the normal distribution, and the empirical autocorrelation function for original and absolute values of data. Data file data.xlsx shows returns for the benchmark, VIX, and short-term rates.

gaussian-simulation.py simulates whether the mean of the logarithm of normal random variable is negative. Namely, find the set of all m, s > 0 such that the normal random variable X with mean m and stdev s has negative expected value of the logarithm of |X|. This corresponds to Section 4. 

capital-distribution-simulation.py simulates the capital distribution curve for this market model. We simulate the volatility and the benchmark, and then we make four simulations of the capital distribution curve with two parameters each taking two values, total 2x2 = 4 simulations. We plot all 4 simulations in one graph. In Section 5, we included two such graphs: Run the code twice. 

standard-normal-simulation.py simulates the capital distribution curve based on the standard normal order statistics. This was discussed in subsection 5.3. 

standard-curve-simulation.py contains Python code to simulate the upper left and lower right of the standard normal market curve, based on ranked standard normal sample. This was discussed in the Appendix.



