import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from pandas_datareader import data as pdr
import datetime as dt
import yfinance as yf

def kmean_seg(Start_date):
    start= dt.datetime(Start_date)
    end=dt.datetime.now()

    # Data read from CSV
    data1=pd.read_csv("Ticker.csv")
    ticker_data = data1['Company'].tolist()
    ticker_data.append('^NSEI')

    # Scrapping data from yfinance
    yf.pdr_override()
    tickers=ticker_data

    data_df=pd.DataFrame()

    for ticker in tickers:
        df=pdr.get_data_yahoo(ticker,start,end)
        data_df[ticker]=df['Adj Close']

    # Computing average return for each stock
    daily_return=data_df.pct_change()
    #Converting to annual return
    annual_return=daily_return.mean()*252

    annual_risk=daily_return.std()* math.sqrt(252)

    # Build new dataframe for use in K-mean
    stock_data=pd.DataFrame()
    stock_data['Annual_Return']=annual_return
    stock_data['Annual_risk']=annual_risk

    # Ascertaining the cluster size using Elbow method ( This uses Marginal utility concept)
    from sklearn.cluster import KMeans

    X=stock_data[['Annual_Return','Annual_risk']]
    inertia_list=[]
    for k in range(2,16):
        kmeans=KMeans(n_clusters=k)
        kmeans.fit(X)
        inertia_list.append(kmeans.inertia_)

    from sklearn.cluster import KMeans
    from yellowbrick.cluster import KElbowVisualizer

    # Data
    X=stock_data[['Annual_Return','Annual_risk']]

    # Instantiate the clustering model and visualizer
    model = KMeans()
    visualizer = KElbowVisualizer(model, k=(2,12))

    #visualizer.fit(x)        # Fit the data to the visualizer
    #visualizer.show()        # Finalize and render the figure    

    # Fitting the model  [ Trial 01 : k=5] [ Trial 02 : k=4]
    model =KMeans(n_clusters=4)
    model.fit(X)

    # Ascertaining cluster laber or classification
    labels=model.labels_
    final_data=stock_data
    final_data['labels']=labels

    final_data['Return:Risk']=final_data['Annual_Return']/final_data['Annual_risk']

    Portfolio_1=final_data[final_data['labels']==0]
    Portfolio_2=final_data[final_data['labels']==1]
    Portfolio_3=final_data[final_data['labels']==2]
    Portfolio_4=final_data[final_data['labels']==3]

    return Portfolio_1,Portfolio_2,Portfolio_3,Portfolio_4