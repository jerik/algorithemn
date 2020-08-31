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

# map a list as dict with numers

    foo = ['North America', 'Asia', 'Africa', 'Europe', 'South America', 'Oceania', 'Antarctica', 'Seven seas (open ocean)']
    {foo[x]:x for x in range(len(foo))}
    # Out: {'North America': 0, 'Asia': 1, 'Africa': 2, 'Europe': 3, 'South America': 4, 'Oceania': 5, 'Antarctica': 6, 'Seven seas (open ocean)': 7}
    
# Ellenbogenverfahren um optimale Clusteranzahl zu finden (KMeans)
Voraussetzung, man hat eine Lite mit WCSS (Within_Clusters_Sum_of_Squares) werten

    wcss = [42605.41356666667, 13208.958119999996, 290.10523333333333, 113.91233333333332, 39.00624999999998, 0.0]
    # Daten aufbereiten für sns.lineplot: 42605.4 = 1, 13208.9 = 2, ..
    line_data = [[x, wcss.index(x)+1] for x in wcss]
    # line_data = [[42605.41356666667, 1], [13208.958119999996, 2], [290.10523333333333, 3], [113.91233333333332, 4], [39.00624999999998, 5], [0.0, 6]]
    # Dataframe daraus erstellen
    line_df = pd.DataFrame(line_data, columns = ['wcss', 'cluster'])
    # Diagramm darstellen
    sns.lineplot(x="cluster", y="wcss", data=line_df)


# KMeans Clustering

    from sklearn.cluster import KMeans
    # get the feature/data which shall be clusters
    feature = data.iloc[:,1:3]  # e.g. rows of latitude and longitude
    cluster = 4  # initial cluster amount / guessed
    kmeans = KMeans(cluster).fit(feature)
    # calculate clusters
    clusters = kmeans.fit_predict(feature)
    # add clusters to analysed data 
    new_data = feature.copy()
    new_data['cluster'] = clusters
    # plot new_data
    # sns.lmplot(x='Longitude', y='Latitude', data=new_data, hue='cluster', fit_reg=False)
    # besser, da ohne fit_reg
    sns.scatterplot(x='Longitude', y='Latitude', data=new_data, hue='cluster')

    # calculate the wcss
    wcss_for_cluster_4 = kmeans.inertia_

    # buld the wcss for Ellenbogenverfahren
    wcss = []
    for i in range(1,10): 
        kmeans = KMeans(i).fit(feature)
        wcss.append([i, kmeans.inertia_])
    wcss  # see above the code

