path =r'C:/Users/78561/Desktop/Visualization/AMCAR/AMCAR/2017-1' # use your path
allFiles = glob.glob(path + "/*.csv")
i = 0
raw_data = {
    'AccessionNumber': [],
    'Date': [],
    'TotalOriginalLoan': [],
    'TotalActualAmount': []}
df_a = pd.DataFrame(raw_data, columns=['AccessionNumber', 'CIK', 'Date', 'TotalOriginalLoan',
                                       'TotalActualAmount', 'TotalActualToOriginal'])
for file_ in allFiles:
    f = pd.read_csv(file_)
    df_a.loc[i] = ([f['accessionnumber'][1], f['cik'][1], 'Feb 2017', sum(f['originalloanamount']),
                       sum(f['actualinterestcollectedamount'] + f['actualothercollectedamount'] +
                           f['actualprincipalcollectedamount']), (f['actualinterestcollectedamount'] +
                                                                  f['actualothercollectedamount'] +
                                                                  f['actualprincipalcollectedamount']) /
                       sum(f['originalloanamount'])])
    i += 1
df_a.to_csv('~/Desktop/temp.csv')

