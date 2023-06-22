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

def get_client_ip():
    try:
        # Retrieve the client IP address
        client_ip = st.experimental_get_request_headers().get("X-Forwarded-For", "").split(",")[0].strip()
        if not client_ip:
            client_ip = st.experimental_get_request_ip()
        return client_ip
    except AttributeError:
        return None


st.title("Geolocation Capture")
st.write("This app captures the geolocation of the user.")

# Get the IP address of the client machine
client_ip = get_client_ip()

if client_ip:
    # Display the IP address
    st.write("Client IP:", client_ip)
else:
    st.write("Unable to retrieve client IP address.")


#Plots map
df_map = pd.DataFrame({"lat":[g.lat], "lon":[g.lng]})
st.map(df_map)