import streamlit as st
import geocoder
import pandas as pd

st.title("Geolocation Capture")
st.write("This app captures the geolocation of the user.")

# Get the geolocation
g = geocoder.ip('me')

# Display the geolocation information
st.write("Geolocation:")
st.write("Latitude:", g.lat)
st.write("Longitude:", g.lng)
st.write("City:", g.city)
st.write("Country:", g.country)

#Plots map
df_map = pd.DataFrame({"lat":[g.lat], "lon":[g.lng]})
st.map(df_map)