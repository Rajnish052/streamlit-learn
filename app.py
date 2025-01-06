import streamlit as st

deliveryData= st.Page("pages/deliveryData.py", title = "deliveryData", icon = ":material/dashboard:")
friendsData =st.Page("pages/friendsData.py", title = "FriendsData", icon = ":material/dashboard:")

pg = st.navigation({"Analysis":[deliveryData,friendsData]})
pg.run()