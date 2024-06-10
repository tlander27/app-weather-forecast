import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Weather Forecast")
place = st.text_input("Place: ")
days = st.slider("Forecast Days",
                 min_value=1, max_value=5,
                 help="Select the number for days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

def get_data(days):
    dates = ["2022-10-25", "2022-10-27", "2022-10-30"]
    temperatures = [10, 8, 15]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures

d, t = get_data(days)

figure = px.line(x=d, y=t, labels={
    "x": "Date",
    "y": "Temperatures (C)"
})

st.plotly_chart(figure)