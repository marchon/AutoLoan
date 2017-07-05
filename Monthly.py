import pandas as pd
import glob

A1Feb = pd.read_csv('C:/Users/78561/Desktop/Visualization/AMCAR/AMCAR/2017-1/autoloan-0001347185-17-000010-assets.csv')
#A1Mar = pd.read_csv('~/Desktop/AMCAR/2017-1/autoloan-0001694010-17-000011-assets.csv')
#A1Mar2 = pd.read_csv('~/Desktop/AMCAR/2017-1/autoloan-0001694010-17-000013-assets.csv')
#A1Apr = pd.read_csv('~/Desktop/AMCAR/2017-1/autoloan-0001694010-17-000016-assets.csv')
#A1May = pd.read_csv('~/Desktop/AMCAR/2017-1/autoloan-0001694010-17-000019-assets.csv')
#A1Jun = pd.read_csv('~/Desktop/AMCAR/2017-1/autoloan-0001694010-17-000022-assets.csv')

#df_newall = pd.concat([A1Feb, A1Mar2, A1Apr, A1May, A1Jun])

# def average_column (csv):
#     f = pd.read_csv('~/Desktop/AMCAR/2017-1/autoloan-0001347185-17-000010-assets.csv')
#     average = 0
#     Sum = 0
#     row_count = 0
#     for row in f:
#         for column in row.split(','):
#             n=float(column)
#             Sum += n
#         row_count += 1
#     average = Sum / len(column)
#     f.close()
#     return 'The average is:', average

A1Feb['w_OriLoan'] = (A1Feb['originalloanamount']/sum(A1Feb['originalloanamount']))



def sumloan():
    filepath = input('Enter your the path of this filling: ')
    f = pd.read_csv(filepath)
    sumloan = sum(f['originalloanamount'])

    return 'The total loan amount is:', sumloan

A1Feb['w_OriLoan'] = (A1Feb['originalloanamount']/sum(A1Feb['originalloanamount']))
A1Feb['Sum_Actual'] = A1Feb['actualinterestcollectedamount'] + A1Feb['actualothercollectedamount'] + \
                      A1Feb['actualprincipalcollectedamount']


def poollevel():
    raw_data = {
        'AccessionNumber': [],
        'Date': [],
        'TotalOriginalLoan': [],
        'TotalActualAmount': []}
    df_a = pd.DataFrame(raw_data, columns=['AccessionNumber', 'CIK', 'Date', 'TotalOriginalLoan',
                                           'TotalActualAmount', 'TotalActualToOriginal'])
    filepath = input('Enter your the path of this filling: ')
    f = pd.read_csv(filepath)
    df_a.loc[0] = [f['accessionnumber'][1], f['cik'][1], 'Feb 2017', sum(f['originalloanamount']),
                   sum(f['actualinterestcollectedamount'] + f['actualothercollectedamount'] +
                       f['actualprincipalcollectedamount']), (f['actualinterestcollectedamount'] +
                                                              f['actualothercollectedamount'] +
                                                              f['actualprincipalcollectedamount']) /
                   sum(f['originalloanamount'])]
    df_a.to_csv('~/Desktop/temp.csv')
    return 'the first line is ', df_a



