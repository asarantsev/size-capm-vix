import numpy
import pandas
import scipy
import statsmodels
from statsmodels.api import OLS

def reg(target, bench, vol, relSize):
    noutput = (target - bench) / vol
    nbenchmark = relSize * bench / vol
    inputDF = pandas.DataFrame({'const' : 1, 'relativeSize' : relSize.astype(float), 'benchmark' : nbenchmark.astype(float)})
    Reg = OLS(noutput.astype(float), inputDF).fit()
    res = Reg.resid
    std = numpy.std(res)
    LB = statsmodels.stats.diagnostic.acorr_ljungbox(res, lags = [10])
    ALB = statsmodels.stats.diagnostic.acorr_ljungbox(abs(res), lags = [10])
    LBp = LB.values[0][1]
    ALBp = ALB.values[0][1]
    SWp = scipy.stats.shapiro(res).pvalue
    JBp = scipy.stats.jarque_bera(res).pvalue
    print('Point estimates\n', Reg.params)
    print('P-values\n', Reg.pvalues)
    print('T-values\n', Reg.tvalues)
    print('Stderr', std, ' R^2', Reg.rsquared)
    print('10 lags Ljung-Box p-value for residuals')
    print('original values ', LBp) # '\nand absolute values ', ALBp)
    print('Normality tests p-values')
    print('Shapiro-Wilk', SWp)

NDECILES = 10

PriceReturns = pandas.read_excel('data-new.xlsx', sheet_name = 'Price-Returns')
TotalReturns = pandas.read_excel('data-new.xlsx', sheet_name = 'Total-Returns')
Volatility = pandas.read_excel('data-new.xlsx', sheet_name = 'Volatility').values[:, 1]
Short = pandas.read_excel('data-new.xlsx', sheet_name = 'Short-Treasury').values[:-1, 1]
Size = pandas.read_excel('data-new.xlsx', sheet_name = 'Average-Size')
benchmarkSize = Size.values[:, NDECILES]
benchmarkPrice = PriceReturns.values[:, NDECILES]
benchmarkTotal = TotalReturns.values[:, NDECILES]
benchmarkPremia = benchmarkTotal - Short/12

for decile in range(NDECILES-1):
    returns = PriceReturns.values[:, decile + 1]
    treturns = TotalReturns.values[:, decile + 1]
    premia = treturns - Short/12
    relsize = -numpy.log(Size.values[:, decile + 1]/benchmarkSize)
    print('decile', decile + 1)
    print('Regression for Price Returns')
    reg(returns, benchmarkPrice, Volatility, relsize)
    print('Regression for Equity Premia')
    reg(premia, benchmarkPremia, Volatility, relsize)
    

    

    
