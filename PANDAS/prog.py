#series
import pandas as pd
import numpy as np
# dict1=[2,3,4,5,np.nan,6]
# df=pd.Series(dict1,index=[11,22,33,44,5,15],name="numbers")
# print(df)
# print("Name Of Series=",df.name)
# print("Values Of Series=",df.values)
# print("Size Of Series=",df.size)
# print("count Of Series=",df.count())


# lst=[11,22,33,44,55,66,77,88,99]
# df=pd.DataFrame(lst,index=[1,2,3,4,5,6,7,8,9])
# print(df.head(4))
# print(df.tail(2))


# lst=[11,22,33,44,55,66,77,88,99]
# df=pd.DataFrame(lst,index=[1,2,3,4,5,6,7,8,9])
# print(df)
# # print(df["a":"d"])
# print(df[3:7])

# 1.adding the series of values
# a=pd.Series([100,200,300,400])
# b=pd.Series([500,600,700,800])
# c=a.add(b)
# print(c)

# a=pd.Series([100,200,300,400],index=[1,2,3,4])
# b=pd.Series([500,600,700,800],index=[1,2,3,4])
# c=a.add(b)
# print(c)

# a=pd.Series([100,200,300,400],index=[1,2,3,33])
# b=pd.Series([500,600,700,800],index=[1,2,3,4])
# c=a.add(b,fill_value=0)
# print(c)

# 2.Subtracting the series of values
# a=pd.Series([100,200,300,400])
# b=pd.Series([500,600,700,800])
# c=a.subtract(b)
# print(c)

# a=pd.Series([100,200,300,400],index=[1,2,3,4])
# b=pd.Series([500,600,700,800],index=[1,2,3,4])
# c=a.subtract(b)
# print(c)

# a=pd.Series([100,200,300,400],index=[1,2,3,33])
# b=pd.Series([500,600,700,800],index=[1,2,3,4])
# c=a.subtract(b,fill_value=0)
# print(c)

# 3.Drop the series of values
# a=pd.Series([100,200,300,400],index=['a','b','c','d'])
# a=a.drop("a",inplace=False)
# print(a)

# s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])

# s['e']=999
# print(s)

#DataFrame

# #list
# lst=[11,12,23,45,67]
# df=pd.DataFrame(lst)
# print(df)

#dict
# d={'name':'jack','age':20,'city':'beijing','country':'china'}
# df=pd.DataFrame(d,index=[1])
# print(df)

#series
# s=pd.Series([11,12,23,45,67])
# df=pd.DataFrame(s)
# print(type(df),df)

#ndarray
# import numpy as np
# a=np.array([[1,2,3],[4,5,6],[7,8,9]])
# df=pd.DataFrame(a)
# print(df)

#csv file
# df=pd.read_csv('saniket1.csv')
# print(df)

# data = {'Name': ['John', 'Alice', 'Bob'], 'Age': [25, 30, 28]}
# df=pd.DataFrame(data)
# df.to_csv("sal.csv")
# print("Data saved successfully...!")\

#dataframe attribute
# 1.index
# 2.columns
# 3.values
# 4.shape
# 5.size
# 6.axes
# 7.ndim
# 8.empty
# 9.T
# dtypes

# 1.index
# data={"name":["sagar","aniket","sumit","manv"],"class":["bca","bsc","bcom","ba"]}
# df=pd.DataFrame(data,index=[11,22,33,44])
# print(df.index)
# for ind in df.index:
#     print(ind)

# 2.columns
# data={"name":["sagar","aniket","sumit","manv"],"class":["bca","bsc","bcom","ba"]}
# df=pd.DataFrame(data,index=[11,22,33,44])
# print(df.columns)
# for ind in df.columns:
#     print(ind)


# 3.values
# data={"name":["sagar","aniket","sumit","manv"],"class":["bca","bsc","bcom","ba"]}
# df=pd.DataFrame(data,index=[11,22,33,44])
# print(df.values)
# print("-------------------------")
# for ind in df.values:
#     print(ind)

# 4.shape
# data={"name":["sagar","aniket","sumit","manv"],"class":["bca","bsc","bcom","ba"]}
# df=pd.DataFrame(data,index=[11,22,33,44])
# print(df.shape)
# print("-------------------------")
# for ind in df.shape:
#     print(ind)

# 5.size
# data={"name":["sagar","aniket","sumit","manv"],"class":["bca","bsc","bcom","ba"]}
# df=pd.DataFrame(data,index=[11,22,33,44])
# print(df.size)
# print("-------------------------")

# 6.axes
# data={"name":["sagar","aniket","sumit","manv"],"class":["bca","bsc","bcom","ba"]}
# df=pd.DataFrame(data,index=[11,22,33,44])
# print(df.axes)
# print("-------------------------")
# for ind in df.axes:
#     print(ind)

# 7.ndim
# data={"name":["sagar","aniket","sumit","manv"],"class":["bca","bsc","bcom","ba"]}
# df=pd.DataFrame(data,index=[11,22,33,44])
# print(df.ndim)
# print("-------------------------")

# 8.empty
# data={"name":["sagar","aniket","sumit","manv"],"class":["bca","bsc","bcom","ba"]}
# df=pd.DataFrame(data,index=[11,22,33,44])
# print(df.empty)
# print("-------------------------")

#9.T
# data={"name":["sagar","aniket","sumit","manv"],"class":["bca","bsc","bcom","ba"]}
# df=pd.DataFrame(data,index=[11,22,33,44])
# print(df.T)
# print("-------------------------")
# for ind in df.T:
#     print(ind)

# 10.dtypes
# data={"name":["sagar","aniket","sumit","manv"],"class":["bca","bsc","bcom","ba"]}
# df=pd.DataFrame(data,index=[11,22,33,44])
# print(df.dtypes)
# print("-------------------------")
# for ind in df.dtypes:
#     print(ind)

import pandas as pd
data = {
    'Order ID': [1001, 1002, 1003, 1004],
    'Product Name': ['Office Chair', 'Laptop', 'Printer Paper', 'Desk Lamp'],
    'Category': ['Furniture', 'Technology', 'Office Supplies', 'Furniture'],
    'Order Date': ['01/10/2024', '05/10/2024', '07/10/2024', '08/10/2024'],
    'Sales': [150.00, 1200.00, 25.00, 80.00],
    'Quantity': [2, 1, 5, 2],
    'Profit': [30.00, 200.00, 5.00, 15.00],
    'Customer Name': ['John Doe', 'Jane Smith', 'Mike Lee', 'Sarah Johnson']
}
df=pd.DataFrame(data)
print(df)
print("----------------------------------------------------")
print(df[2:10])
print("---------------------------------------------------")
# for rec in df.iterrows():
#     print(rec)
print("---------------------------------------------------")
# print(df[4:10:-1])
df["totalprofit"]=df["Profit"]+df["Sales"]
print(df)
print("-------------------------------------------------------")
print(df.drop_duplicates())

"""
Django settings for modelproject project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-iocldgy9yaecdgm(3a8lw7iraev-cx_-zeeymv9c=2!&8##yym'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'testapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'modelproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'modelproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'modeldb',
        'USER':'root',
        'PASSWORD':'12345',
        'PORT':'3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
