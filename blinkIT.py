#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\taeju\jupyter\BlinkIT-Grocery-Data.csv")

# basic statistical summary
print(df.describe())
print(df.info())
print(df.isnull().sum())
# fill missing Item Weight with median
df.fillna({'Item Weight': df['Item Weight'].median()}, inplace=True)
print("**************************************")
# confirm cleaning
print(df.isnull().sum())



# In[2]:


print(df.dtypes)


# In[ ]:


for col in df.columns:
    dup_count=df.duplicated().sum()
    print(f"{col} has {dup_count} duplicate values")


# In[ ]:


categorical_cols = ['item_fat_content', 'item_type', 'outlet_location_type', 'outlet_size', 'outlet_type']
df['outlet_size'] = df['outlet_size'].replace({'High': 'Large'})
df['item_fat_content'] = df['item_fat_content'].replace({
    'LF': 'Low Fat',
    'low fat': 'Low Fat',
    'reg': 'Regular'
})
for col in categorical_cols:
    print(f"{col} unique values:")
    print(df[col].unique())
    print(f"\n{col} value counts:")
    print(df[col].value_counts())
    print("\n------------------\n")



# In[ ]:


import seaborn as sns
import matplotlib.pyplot as plt

numeric_cols = ['item_visibility', 'item_weight', 'sales', 'rating']

for col in numeric_cols:
    sns.boxplot(x=df[col])
    plt.title(f"Boxplot of {col}")
    plt.show()


# In[ ]:


def cap_outliers_iqr(column):
    Q1 = column.quantile(0.25)
    Q3 = column.quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    return column.clip(lower=lower_bound, upper=upper_bound)


# In[ ]:





# In[ ]:




