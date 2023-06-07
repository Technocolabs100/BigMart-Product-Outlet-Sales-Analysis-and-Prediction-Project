#!/usr/bin/env python
# coding: utf-8

# ### Libraries Used:

# In[1]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import category_encoders as ce
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.ensemble import RandomForestRegressor
import seaborn as sns


# ### All about Data:

# In[2]:


df1 = pd.read_csv('C:\\Users\\lenovo\\Downloads\\Train.csv')
df2 = pd.read_csv('C:\\Users\\lenovo\\Downloads\\Test.csv')


# In[3]:


print(df1)
print(df2)
df1.head()
df1.shape
df2.head()
df2.shape


# In[4]:


#missing values
df1.isna().sum()


# In[5]:


df1=df1.dropna()
df1.isnull().sum()


# In[6]:


df2=df2.dropna()
df2.isna().sum()


# In[7]:


df1.sample(5)


# In[8]:


df1.info()


# In[9]:


df1.describe()


# In[10]:


df2.describe()


# In[11]:


df1.columns


# In[12]:


df1.corr()


# In[13]:


df1=df1.replace('LF','Low Fat')
df1=df1.replace('reg','Regular')
df1=df1.replace('low fat','Low Fat')

df1['Item_Fat_Content'].value_counts().plot(kind='bar')


# In[14]:


df1['Outlet_Size'] = df1['Outlet_Size'].astype('category')
sns.countplot(data=df1, x='Outlet_Size')


# In[15]:


df1['Item_Type'].value_counts().plot(kind='pie')


# In[16]:


sns.scatterplot(x=df1['Item_MRP'], y=df1['Item_Outlet_Sales'])


# In[17]:


#Box Plot
sns.boxplot(x=df1['Outlet_Type'], y=df1['Item_Outlet_Sales'])


# ### Linear Regression model

# In[18]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.xlabel('Item_MRP')
plt.ylabel('Item_Outlet_Sales')
plt.scatter(df1.Item_MRP,df1.Item_Outlet_Sales)


# In[19]:


x=df1.iloc[:,5]
y=df1.iloc[:,11]


# In[20]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.2,random_state=2)


# In[21]:


x_train_reshaped = x_train.values.reshape(-1, 1)
y_train_reshaped = y_train.values.reshape(-1, 1)
reg = LinearRegression()
reg.fit(x_train_reshaped, y_train_reshaped)


# In[22]:


plt.scatter(df1['Item_MRP'],df1['Item_Outlet_Sales'])
plt.plot(x_train_reshaped,reg.predict(x_train_reshaped),color='red')


# In[23]:


# Convert x_test to a numpy array if it's not already
x_test = np.array(x_test) 
# Reshape to have a single feature column
x_test = x_test.reshape(-1, 1) 
y_pred=reg.predict(x_test)


# In[24]:


y_test.values


# In[25]:


print("MSE:",r2_score(y_test,y_pred))


# In[26]:


x2=df2.iloc[:,5]


# In[27]:


x_test2 = np.array(x2)  # Convert x_test to a numpy array if it's not already
x_test2 = x_test2.reshape(-1, 1)
y_pred2=reg.predict(x_test2)
print(y_pred2)


# ### Label Encoding:

# In[28]:


#Label Encoding
label_encoder = LabelEncoder()
categorical_cols = ['Item_Fat_Content',"Outlet_Establishment_Year","Outlet_Size","Outlet_Location_Type","Outlet_Type"]
for col in categorical_cols:
    df1[col] = label_encoder.fit_transform(df1[col])
    df2[col] = label_encoder.fit_transform(df2[col])


# In[29]:


df1


# ### One hot encoding: 

# In[30]:


#One hot encoding
encoder=ce.OneHotEncoder(cols='Outlet_Size',handle_unknown='return_nan',return_df=True,use_cat_names=True)
df1 = encoder.fit_transform(df1)
df2 = encoder.fit_transform(df2)


# In[31]:


df1
df1.drop(columns=['Item_Identifier','Outlet_Identifier','Item_Type'],axis=1,inplace=True)


# In[32]:


df2
df2.drop(columns=['Item_Identifier','Outlet_Identifier','Item_Type'],axis=1,inplace=True)


# In[33]:


df1


# In[34]:


df2


# In[36]:


# Define the desired column order as a list
new_order = ['Item_Weight', 'Item_Fat_Content', 'Item_Visibility', 'Item_MRP', 'Outlet_Establishment_Year', 'Outlet_Size_1.0', 'Outlet_Size_2.0', 'Outlet_Size_0.0', 'Outlet_Location_Type', 'Outlet_Type', 'Item_Outlet_Sales']

# Reorder the columns
df1 = df1[new_order]

# Updated DataFrame with columns in new order
print(df1)


# In[37]:


X=df1.drop(["Item_Outlet_Sales"],axis=1)
Y=df1["Item_Outlet_Sales"]


# ### Random Forest Regression:

# In[38]:


X_train_rf, X_test_rf, y_train_rf, y_test_rf = train_test_split(X,Y,test_size=0.2)


# In[39]:


model = RandomForestRegressor()
model1=model.fit(X_train_rf,y_train_rf)


# In[40]:


Y_pred=model1.predict(X_test_rf)
print(r2_score(y_test_rf, Y_pred))


# In[41]:


ypred2=model1.predict(df2)


# In[42]:


ypred2


# In[ ]:




