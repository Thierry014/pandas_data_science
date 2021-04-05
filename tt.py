import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlb inline




df=pd.read_csv('tt.csv')
# print(df.shape)
# print(df.head())
# print(df.describe())
# print(df.drop(['SibSp','Parch','Ticket'],axis=1).head())
# print(df.head())
# print(df.isnull().sum())
# pd.value_counts(df['Survived']).plot.bar()
# plt.show()
# pd.value_counts(df['Sex']).plot.bar()
# plt.show()
# print(df['Survived'].mean())
# print(df.groupby(['Sex']).mean())
# print(df.groupby(['Sex','Pclass']).mean())
# print(df[df['Age']<18].groupby(['Sex','Pclass']).mean())
# print(df.index)


df = df.drop(['Name','SibSp','Parch','PassengerId'], axis =1 )
# print(df.head())

# print(df.info())
# plt.figure(figsize = (10,7))
# sns.heatmap(df.isnull(), yticklabels=False, cmap='ocean')
# plt.show()
# df = df.drop('Cabin', axis=1)
print(df.groupby('Pclass').Age.transform('mean'))
# print(df['Age'].describe())
# print(df.Age.median())
sns.boxplot(data = df, x = df.Age)
plt.show()
