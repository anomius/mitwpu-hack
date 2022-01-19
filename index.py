import streamlit as st
import matplotlib.pyplot as plt
from matplotlib import dates
from datetime import datetime
from matplotlib import rcParams
import math
from api import owm
import time
from pyowm.commons.exceptions import NotFoundError
#import RPi.GPIO as GPIO

# Streamlit Display
st.set_page_config(layout="centered")
st.title("Smart Irrigation System")

#                  ┌───────web-server────────┐
#   ┌───────┐      │                         │
#   │ input ├───┬──┼────┐  ┌────────┐        │
#   └───────┘   │  │    └──► get_ev │        │                   ┌──────────────┐
#               │  │       └───┬────┘ ┌──────┼───────────────────┤    Relay     │
# ┌─────────────┤  │           │      │      │                   ├──────────────┤
# │ open-weather│  │       ┌───┴────┐ │      │                   │┼┼┼┼┼┼┼┼┼┼┼┼┼┼│
# │     api     │  │       │get_time├─┘      │                   ├──────────────┤
# └─────────────┘  │       └────────┘        ├───────────────────┤              │
#                  │                         │                   │ rassberry-pi │
#                  └─────────────────────────┘                   │              │
#                                                                └──────────────┘

with st.form("my_form"):
    st.header("🌐 Enter the name of City and Select Temperature Unit")
    place  = st.text_input("NAME OF THE CITY ", " ")
    unit   = st.selectbox(" SELECT TEMPERATURE UNIT 🌡 ", ("Celsius", "Fahrenheit"))
    g_type = st.selectbox("SELECT GRAPH TYPE 📉 ", ("Line Graph", "Bar Graph"))
    solar_r= st.number_input("Solar Radiance in",00.1,step=0.1,format="%.2f")
    radiance_unit=st.selectbox("Unit of radiance ", ("MJ/m^2day", "kWh/m^2day"))
    t0 = st.number_input("Orignal Time in hours",0.1,step=0.01,format="%.2f")
    h  = st.number_input("Irrigation Hight in mm",1,step=1,format="%i")

    auto=st.checkbox("Manual")

    b = st.form_submit_button("Submit")
if radiance_unit=="kWh/m^2day":
    solar_r=solar_r*3.6

# To deceive error of pyplot global warning
st.set_option('deprecation.showPyplotGlobalUse', False)

def plot_line(days, min_t, max_t):
    days = dates.date2num(days)
    rcParams['figure.figsize'] = 6, 4
    plt.plot(days, max_t, color='black', linestyle='solid', linewidth=1, marker='o', markerfacecolor='green',
             markersize=7)
    plt.plot(days, min_t, color='black', linestyle='solid', linewidth=1, marker='o', markerfacecolor='blue',
             markersize=7)
    plt.ylim(min(min_t) - 4, max(max_t) + 4)
    plt.xticks(days)
    x_y_axis = plt.gca()
    xaxis_format = dates.DateFormatter('%d/%m')

    x_y_axis.xaxis.set_major_formatter(xaxis_format)
    plt.grid(True, color='brown')
    plt.legend(["Maximum Temperature", "Minimum Temperature"], loc=1)
    plt.xlabel('Dates(dd/mm)')
    plt.ylabel('Temperature')
    plt.title('6-Day Weather Forecast')