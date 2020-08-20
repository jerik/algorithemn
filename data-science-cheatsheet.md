# Data Science Cheatsheet

List all files: 

    import os
    for dirname, _, filenames in os.walk('/kaggle/input'):
        for filename in filenames:
            print(os.path.join(dirname, filename))


## Variable identification 

    data = pd.read_csv('/kaggle/input/new-york-city-airbnb-open-data/AB_NYC_2019.csv')
    data.head()
    numerical = []
    for var in data.columns:
        if data[var].dtype != 'object':
          numerical.append(var)

     print('Numerical values {0}'.format(numerical))


    categorical = []
    for var in data.columns:
        if data[var].dtype =='object':
            categorical.append(var)

    print('Categorical values: {0}'.format(categorical))

    discrete = []
    for var in numerical:
        if len(data[var].unique()) < 20:
            discrete.append(var)

    print(discrete)

    continuous = [x for x in numerical if x not in ['id','price'] and x not in discrete]
    print(continuous)

    for var in data.columns:
      if(data[var].isnull().sum() != 0):
        print(var, data[var].isnull().sum(), data[var].dtype)


Source: https://www.kaggle.com/naveenraajan/regression-nyk-airbnb

# Print e-number 

    print("%.35f" % 5.387e-35)
