# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

from datetime import datetime, timedelta

    
def get_cases(USCases, GlobalCases, country="global",province=None, county=None ):
    """"
    gets an np.array of the number of total cases in a certain county/province/country per day
    
    country, the country whose cases we want to get
    
    province, the province whose cases we want to get, if this is None, then a sum of all of the cases in a country
    
    county (US only), the county whose cases we want to get, if this is None then sum all of the cases in the province
    """
    #if country = US
    if country == 'US':
        #dataframe=copy(USCases)
        dataframe=USCases.copy(deep=True)
        #if province != None
        if province !=None:
            #dataframe=get all rows where dataframe['Province_State']==province
            dataframe=dataframe[dataframe['Province_State']==province]
            #if county != None
            if county != None:
                #dataframe=all rows where dataframe['Admin2']==county
                dataframe==dataframe[dataframe['Admin2'==county]]
        CaseArray=np.array(dataframe[dataframe.columns[12:]]).sum(axis=0)
    elif country=="global":
        CaseArray=np.array(USCases[USCases.columns[12:]]).sum(axis=0)+\
            np.array(GlobalCases[GlobalCases.columns[5:]]).sum(axis=0)
    #else
    else:
        
        dataframe=GlobalCases.copy(deep=True)
        dataframe=dataframe[dataframe['Country/Region']==country]
        if province!= None:
            dataframe=dataframe[dataframe["Province/State"]==province]
        CaseArray=np.array(dataframe[dataframe.columns[4:]]).np.sum(axis=0)
    return CaseArray

def get_deaths(USDeaths,GlobalDeaths, country="global",province=None, county=None ):
    """"
    gets an np.array of the number of total deaths in a certain county/province/country every day day
    
    country, the country whose deaths we want to get
    
    province, the province whose deaths we want to get, if this is None, then a sum of all of the deaths in a country
    
    county (US only), the county whose deaths we want to get, if this is None then sum all of the deaths in the province
    """
    #if country = US
    if country == 'US':
        #dataframe=copy(USDeaths)
        dataframe=USDeaths.copy(deep=True)
        #if province != None
        if province !=None:
            #dataframe=get all rows where dataframe['Province_State']==province
            dataframe=dataframe[dataframe['Province_State']==province]
            #if county != None
            if county != None:
                #dataframe=all rows where dataframe['Admin2']==county
                dataframe==dataframe[dataframe['Admin2'==county]]
        CaseArray=np.array(dataframe[dataframe.columns[13:]]).sum(axis=0)
    #elif if country = global
    elif country=="global":
        CaseArray=np.array(USDeaths[USDeaths.columns[13:]]).sum(axis=0)+\
            np.array(GlobalDeaths[GlobalDeaths.columns[5:]]).sum(axis=0)
    #else
    else:
        
        dataframe=GlobalDeaths.copy(deep=True)
        dataframe=dataframe[dataframe['Country/Region']==country]
        if province!= None:
            dataframe=dataframe[dataframe["Province/State"]==province]
        CaseArray=np.array(dataframe[dataframe.columns[5:]]).np.sum(axis=0)
    return CaseArray

def get_data():
    """
    

    Returns
    -------
    Import the 4 csv files and return them as pandas

    """
    GlobalCases=pd.read_csv('time_series_covid19_confirmed_global.csv')
    GlobalDeaths=pd.read_csv('time_series_covid19_deaths_global.csv')

    USCases=pd.read_csv('time_series_covid19_confirmed_US.csv')
    USDeaths=pd.read_csv('time_series_covid19_deaths_US.csv')
    
    return USCases,GlobalCases,USDeaths,GlobalDeaths

def make_ticks(start_date=None,end_date=None,n_days=None, step=30):
    """
    returns the locations and date labels of the X-ticks, these ticks are sepperated by step days
    
    of the first three parameters, two are required
    """
    if start_date!=None:
        StartTimeDate=datetime.strptime(start_date, '%m/%d/%y')
    if end_date!=None:
        EndTimeDate=datetime.strptime(start_date, '%m/%d/%y')
    try:
        StartTimeDate=EndTimeDate-timedelta(days=n_days)
    #if end_date==None then NameError would be raised
    except NameError:
        EndTimeDate=StartTimeDate+timedelta(days=n_days)
    
    ticks=np.array([])
    dates=np.array([])
    n=0
    CurrentDateTime=StartTimeDate
    while CurrentDateTime <EndTimeDate:
        ticks=np.append(ticks,n)
        dates=np.append(dates,CurrentDateTime.strftime('%m/%d/%y'))
        CurrentDateTime+=timedelta(days=step)
        n+=step
    return ticks,dates

def get_delta(data):
    """
    data, np.array
    gets the delta of the data
    by definition, the delta of the first day should just be data[0,:]
    """
    d_array=np.append([0],np.diff(data))
    return d_array

def moving_average(data,bandwith):
    """
    gets the moving average of data, with the number of days=bandwith
    """
    moving_average_array=np.zeros(data.shape[0])
    for n in range(data.shape[0]):
        moving_average_array[n]=np.mean(data[n:n+bandwith])
    return moving_average_array