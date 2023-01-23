import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(page_title="Progress Arrar Transmission line",layout="wide")


x=pd.read_excel(io="mybook.xlsx" ,sheet_name='1'  ,usecols='A:C',nrows=10)


st.dataframe(x)
