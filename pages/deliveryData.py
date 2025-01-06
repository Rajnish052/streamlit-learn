import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Delivery Time Analysis",  # Change the tab title
)

data = pd.read_csv("food.csv")

# print(data.head())


st.title("food delivery analytics")
st.header("Food delivery time")

st.write("Hello *guys*")

st.write('Below is a some part of DataFrame:', data.head())

st.line_chart(data, x = 'Distance_km', y = 'Delivery_Time_min')
# st.bar_chart(data, x = 'Distance_km', y = 'Delivery_Time_min')

st.scatter_chart(data, x= 'Time_of_Day' , y = 'Preparation_Time_min' ,size = 'Preparation_Time_min')


st.scatter_chart(data, x= 'Distance_km' , y = 'Delivery_Time_min' ,size = 'Delivery_Time_min',color="#ffaa0088")
