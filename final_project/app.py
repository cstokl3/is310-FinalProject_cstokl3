import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt

st.set_page_config(page_title="Programming", page_icon=":bar_chart:")

st.title('Programming Over Time')
st.subheader('This dashboard was created for my final project in IS310! It also happens to be the very first app I have built based in data science.')

def load_data():
    data=pd.read_csv('datascience.csv')
    return data

java_data=load_data()


st.subheader('Data Science Tweets Over a Decade')

tweets_java = java_data['Datetime'].value_counts()

#st.write(java_data)
#Bar Chart
st.bar_chart(tweets_java)


st.sidebar.checkbox("Programming Over a Decade", True, key=1)
select = st.sidebar.selectbox('Select a Year',java_data['Datetime'])

#get the state selected in the selectbox
java_tweet_data = java_data[java_data['Datetime'] == select]

