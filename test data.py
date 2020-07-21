#!/usr/bin/env python
# coding: utf-8

# In[5]:


url="https://raw.githubusercontent.com/WalePhenomenon/climate_change/master/fuel_ferc1.csv"
import pandas as pd
testdata=pd.read_csv(url)
#testdata.describe(include='all')
test_data=pd.DataFrame(testdata)
test_data


# In[11]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(7,5))
plt.xticks(rotation=90)
sns.barplot(data=test_data,x='report_year',y='fuel_cost_per_unit_burned')
plt.xlabel('test_data')

g = sns.barplot(data=test_data, x='report_year', y='fuel_cost_per_unit_burned')
g.set_yscale("log")
g.set_ylim(1, 12000)
plt.xlabel('test_data')


# In[23]:


test_data.mean()


# In[8]:


test_data.skew()


# In[9]:


test_data.kurt()


# In[10]:


test_data.std()

