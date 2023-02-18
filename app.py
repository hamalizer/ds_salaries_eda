# imports
import pandas as pd
import streamlit as st
import plotly.express as px

# read dataframe
df = pd.read_csv('HR_Analytics.csv')

st.header('Employee Attrition: A short story.')

st.write(px.histogram(df, x='Attrition', color='HourlyRate'))

st.write(px.scatter_matrix(df, color='Attrition'))



st.write('It is not a functional application yet. Under construction.') 