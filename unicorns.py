import warnings

import matplotlib.pyplot as plt
import pandas as pd
import pumpy as np
import seaborn as sns

warnings.filterwarnings('ignore')

database_unicorns_startups = pd.read_csv('unicorns till sep 2022.csv')

# verify dimensions
database_unicorns_startups.shape
# print('database_unicorns_startups.shape', database_unicorns_startups.shape)

# primary registers
database_unicorns_startups.head()
# print('database_unicorns_startups.head()', database_unicorns_startups.head())


# coluns
database_unicorns_startups.columns
# print('database_unicorns_startups.columns', database_unicorns_startups.columns)

# info
# database_unicorns_startups.info()
# print('database_unicorns_startups.info()', database_unicorns_startups.info())

# plt.figure(figsize=(15, 6))
# plt.title('Analytics Null Fields')
# sns.heatmap(database_unicorns_startups.isnull(), cbar=False)
# plt.show()

database_unicorns_startups.nunique()
# GRAPHIC BLOCOS
# print(database_unicorns_startups.nunique()) verify unique columns
# print(database_unicorns_startups['Country'].unique()) verify unique values in specified column
# print(database_unicorns_startups['Company'].value_counts())  # count unique values
# print(database_unicorns_startups['Company'].value_counts(normalize=True))  # count unique values in percentage
# plt.figure(figsize=(15, 6))
# plt.title('Analytics Industry')
# plt.bar(database_unicorns_startups['Industry'].value_counts().index,
#         database_unicorns_startups['Industry'].value_counts())
# plt.xticks(rotation=45, ha='right')
# plt.show()

countries = database_unicorns_startups['Country'].value_counts(normalize=True)
analytics = round(countries * 100, 1)
# print(analytics)
plt.pie(
    analytics,
    labels=countries.index.tolist(),
    shadow=True,
    startangle=90,
    autopct='%1.1f%%'
)

plt.show()
