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

#--------------------------------
import streamlit as st
from flask import request
import geocoder

def get_client_ip():
    if request:
        return request.remote_addr
    return None


st.title("Geolocation Capture")
st.write("This app captures the geolocation of the user.")

# Get the IP address of the client machine
client_ip = get_client_ip()

if client_ip:
    # Retrieve geolocation information based on the IP address
    g = geocoder.ip(client_ip)

    # Display the geolocation information
    st.write("Geolocation:")
    st.write("Latitude:", g.lat)
    st.write("Longitude:", g.lng)
    st.write("City:", g.city)
    st.write("Country:", g.country)
else:
    st.write("Unable to retrieve client IP address.")

#Plots map
df_map = pd.DataFrame({"lat":[g.lat], "lon":[g.lng]})
st.map(df_map)