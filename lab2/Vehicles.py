import matplotlib

matplotlib.use('Agg')

import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np

if __name__ == "__main__":
    df = pd.read_csv('./vehicles_current.csv')
    df2 = pd.read_csv('./vehicles_new.csv')
    print df.columns
    sns_plot = sns.lmplot(df.columns[0], df.columns[1], data=df, fit_reg=False)

    sns_plot.axes[0, 0].set_ylim(0, )
    sns_plot.axes[0, 0].set_xlim(0, )

    sns_plot.savefig("vehicle_new_Scater.png", bbox_inches='tight')

    plt.clf()
    print df.columns
    sns_plot = sns.lmplot(df2.columns[0], df2.columns[1], data=df2, fit_reg=False)

    sns_plot.axes[0, 0].set_ylim(0, )
    sns_plot.axes[0, 0].set_xlim(0, )

    sns_plot.savefig("vehicle_current_Scater.png", bbox_inches='tight')

    data = df.values.T[1]
    data2 = df2.values.T[1]

    plt.clf()

    sns_plot2 = sns.distplot(data, bins=20, kde=False, rug=True).get_figure()

    axes = plt.gca()
    axes.set_xlabel('mpg')
    axes.set_ylabel('car count')

    sns_plot2.savefig("vehicle_new_histogram.png", bbox_inches='tight')


    plt.clf()
    sns_plot2 = sns.distplot(data2, bins=20, kde=False, rug=True).get_figure()

    axes = plt.gca()
    axes.set_xlabel('mpg')
    axes.set_ylabel('car count')

    sns_plot2.savefig("vehicle_current_histogram.png", bbox_inches='tight')
