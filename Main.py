import streamlit as st
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events

loc_button = Button(label="Get Location")
loc_button.js_on_event("button_click", CustomJS(code="""
    navigator.geolocation.getCurrentPosition(
        (loc) => {
            document.dispatchEvent(new CustomEvent("GET_LOCATION", {detail: {lat: loc.coords.latitude, lon: loc.coords.longitude}}))
        }
    )
    """))
result = streamlit_bokeh_events(
    loc_button,
    events="GET_LOCATION",
    key="get_location",
    refresh_on_update=False,
    override_height=75,
    debounce_time=0)

if result:
    if "GET_LOCATION" in result:
        st.write(result.get("GET_LOCATION"))

import streamlit as st
import geocoder

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