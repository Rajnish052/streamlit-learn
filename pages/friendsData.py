import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Friends Detail",  # Change the tab title
    page_icon="🫎",                # Change the favicon (can be an emoji or image URL)
)
st.title("Data analytics app")


st.header('This is my first app')

# Example 1


st.audio("myaudio.mp3", format="audio/mpeg")


st.write('Hello, *guys* :sunglasses:')

df = pd.DataFrame({
    "Name": ["Rohan", "Rajnish", "Akash", "Gangesh", "Yash", "Ayush", "Advitiya"],
     'Current_company': ["Paytm", "Berojgaar", "Shell", "DXC", "Shell", "Cognizant", "Insight"],
     "lat": [28.53, 25.31,12.97,30.15,12.97,28.70,31.82],
     "lon": [77.39,82.97,77.59,76.86,77.59,77.10,77.47],
     'Current_location': ["Noida", "Varanasi", "Bangalore", "Shahbad","Bangalore", "Delhi", "Himachal"],
     "Weight (kg)": [71,61,96,65,75,63,78],
     "Height (cm)": [177,176,180,150,190,172,172],
    #  "color": np.random.rand(7,4).tolist()
     })



st.write('Below is a DataFrame:', df, 'Friends dataframe.')

# Example 5

# df2 = pd.DataFrame(
#      np.random.randn(200, 3),
#      columns=['a', 'b', 'c'])

# c = alt.Chart(df).mark_circle().encode(
#      x='Name', y='Weight (kg)', size='Weight (kg)', color='Weight (kg)', tooltip=['Name', 'Weight (kg)'])
# st.write(c)
# fig = plt.figure(figsize=(10,5))
# plt.bar(df['Name'], df['Height (cm)'], color = 'blue')

# st.pyplot(fig)

st.scatter_chart(df, x= 'Weight (kg)' , y = 'Height (cm)' ,size = 'Weight (kg)' ,color = 'Name')

st.bar_chart(df, x = 'Name', y = 'Height (cm)', color = 'Name')
st.map(data=df , latitude=  'lat', longitude= 'lon', size=50000)

