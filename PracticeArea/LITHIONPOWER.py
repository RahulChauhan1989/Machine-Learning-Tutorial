#LITHIONPOWER
#Domain :  Automotive
#Focus : Incentivize Drivers

#Business Challenge: Lithionpower is the largest provider of electric vehicle(e - vehicle) batteries. Drivers rent battery typically for a day and then replace it with a charged battery from the company. Lithionpower has a variable pricing model based on the driver’s driving history. As the life of a battery depends on factors such as overspeeding, distance driven per day, etc. You as an ML expert have to create a cluster model where drivers can be grouped together based on the driving data.

#Key issues: Drivers will be incentivized based on the cluster, so grouping has to be accurate.

#Business Benefits: Increase in profits, up to 15 - 20 % as drivers with poor history will be charged more.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set() # for plot styling
#%matplotlib inline
import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (12, 6)
 
df=pd.read_csv('driver-data.csv')
df.head()

df.info()
 
df.describe()

from sklearn.cluster import KMeans
 
#Taking 2 clusters
kmeans = KMeans(n_clusters=2)
df_analyze = df.drop('id',axis=1)
 
kmeans.fit(df_analyze)

kmeans.cluster_centers_

print (kmeans.labels_)
print (len(kmeans.labels_))

print (type(kmeans.labels_))
unique, counts = np.unique(kmeans.labels_, return_counts=True)
print(dict(zip(unique, counts)))

df_analyze['cluster'] = kmeans.labels_
sns.set_style('whitegrid')
sns.lmplot('mean_dist_day','mean_over_speed_perc',data=df_analyze, hue='cluster',
palette='coolwarm',size=6,aspect=1,fit_reg=False)

#Now, Let's check the clusters, when n=4
kmeans_4 = KMeans(n_clusters=4)
kmeans_4.fit(df.drop('id',axis=1))
kmeans_4.fit(df.drop('id',axis=1))
print(kmeans_4.cluster_centers_)
unique, counts = np.unique(kmeans_4.labels_, return_counts=True)
 
kmeans_4.cluster_centers_
print(dict(zip(unique, counts)))

df_analyze['cluster'] = kmeans_4.labels_
sns.set_style('whitegrid')
sns.lmplot('mean_dist_day','mean_over_speed_perc',data=df_analyze, hue='cluster',
palette='coolwarm',size=6,aspect=1,fit_reg=False)