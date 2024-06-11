import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, selectbox, and subheader
st.title("Weather Forecast")
place = st.text_input("Place: ")
days = st.slider("Forecast Days",
                 min_value=1, max_value=5,
                 help="Select the number for days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    # Get the temperature/sky data
    try:
        filtered_data = get_data(place, days)

        # Create temperature plot
        if option == "Temperature":
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={
                "x": "Date",
                "y": "Temperatures (C)"
            })
            st.plotly_chart(figure)

        if option == "Sky":
            images = {
                "Clear": "images/clear.png",
                "Clouds": "images/cloud.png",
                "Rain": "images/rain.png",
                "Snow": "images/snow.png"
            }
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[sky] for sky in sky_conditions]
            st.image(image_paths, width=50)
    except KeyError:
        st.warning("Enter a valid place")