import numpy
import pandas
from matplotlib import pyplot as plt
from statsmodels.graphics.gofplots import qqplot
from statsmodels.graphics.tsaplots import plot_acf

def plots(series):
    qqplot(series, line = 's')
    plt.show()
    plot_acf(series)
    plt.show()
    plot_acf(abs(series))
    plt.show()

returns = pandas.read_excel('data-new.xlsx', sheet_name = 'Total-Returns').values[:, 10]
vix = pandas.read_excel('data-new.xlsx', sheet_name = 'Volatility').values[:, 1]
rates = pandas.read_excel('data-new.xlsx', sheet_name = 'Short-Treasury').values[1:, 1]
premia = returns - rates/12
npremia = premia/vix
plots(premia)
plots(npremia)


