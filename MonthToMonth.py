import pandas as pd
import glob
import os
import numpy as np

def TS():
    #filepath = '/Users/artb/Desktop/SDART/2017-1'
    filepath = '/Users/artb/Desktop/SDART/2017-2'
    #filepath = '/Users/artb/Desktop/AMCAR/2017-1'
    #filepath = '/Users/artb/Desktop/AMCAR/2017-2'

#    filepath = input('Enter your the absolute path of this folder (without quotes): ')
    extension = 'csv'
    os.chdir(filepath)
    allFiles = [i for i in glob.glob('*.{}'.format(extension))]
    i = 0
    DateA1 = ['Feb 2017', 'Mar 2017', 'Mar 2017', 'Apr 2017', 'May 2017', 'Jun 2017']
    DateS1 = ['Feb 2017', 'Mar 2017', 'Apr 2017', 'May 2017', 'Jun 2017']
    DateA2 = ['May 2017', 'Jun 2017', 'Jun 2017']
    DateS2 = ['May 2017', 'May 2017', 'Jun 2017']

    raw_data = {
        'AccessionNumber': [],
        'CIK': [],
        'Date': [],
        'TotalOriginalLoan': [],
        'TotalActualAmount': [],
        'TotalChargedOffPrincipalAmount': []
    }
    df_a = pd.DataFrame(raw_data, columns=['AccessionNumber', 'CIK', 'Date', 'TotalOriginalLoan',
                                           'TotalActualAmount', 'TotalChargedOffPrincipalAmount'])
    for file_ in allFiles:
        f = pd.read_csv(file_)
        f = f[np.isfinite(f['originalloanamount'])]
        df_a.loc[i] = ([f['accessionnumber'][1], f['cik'][1], DateS2[i], sum(f['originalloanamount']),
                        sum(f['actualinterestcollectedamount'] + f['actualothercollectedamount'] +
                            f['actualprincipalcollectedamount']), sum(f['chargedoffprincipalamount'])])
        print('processing filling...', allFiles[i])
        i += 1

    #df_a.to_csv('/Users/artb/Desktop/POOLS1.csv')
    df_a.to_csv('/Users/artb/Desktop/POOLS2.csv')


 #   df_b.to_csv('/Users/artb/Desktop/PoolAverage.csv')


#
#
#


# use your path : Please don't use relative path in Mac
# path = r'/Users/artb/Desktop/AMCAR/2017-1'
    #   allFiles = glob.glob(filepath + "/*.csv")

