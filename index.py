import streamlit as st
import matplotlib.pyplot as plt
from matplotlib import dates
from datetime import datetime
from matplotlib import rcParams
import math
from API import owm
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
    t0 = st.number_input("Original Time in hours",0.1,step=0.01,format="%.2f")
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

    for i in range(5):
        plt.text(days[i], min_t[i] - 1.5, min_t[i],
                 horizontalalignment='center',
                 verticalalignment='bottom',
                 color='black')
    for i in range(5):
        plt.text(days[i], max_t[i] + 0.5, max_t[i],
                 horizontalalignment='center',
                 verticalalignment='bottom',
                 color='black')
    # plt.show()
    # plt.savefig('figure_line.png')
    st.pyplot()
    plt.clf()


def plot_bars(days, min_t, max_t):
    # print(days)
    days = dates.date2num(days)
    rcParams['figure.figsize'] = 6, 4
    min_temp_bar = plt.bar(days - 0.2, min_t, width=0.4, color='r')
    max_temp_bar = plt.bar(days + 0.2, max_t, width=0.4, color='b')
    plt.xticks(days)
    x_y_axis = plt.gca()
    xaxis_format = dates.DateFormatter('%d/%m')

    x_y_axis.xaxis.set_major_formatter(xaxis_format)
    plt.xlabel('Dates(dd/mm)')
    plt.ylabel('Temperature')
    plt.title('6-Day Weather Forecast')

    for bar_chart in [min_temp_bar, max_temp_bar]:
        for index, bar in enumerate(bar_chart):
            height = bar.get_height()
            xpos = bar.get_x() + bar.get_width() / 2.0
            ypos = height
            label_text = str(int(height))
            plt.text(xpos, ypos, label_text,
                     horizontalalignment='center',
                     verticalalignment='bottom',
                     color='black')
    st.pyplot()
    plt.clf()


def weather_detail(place, unit, g_type):
    mgr = owm.weather_manager()
    days = []
    dates_2 = []
    min_t = []
    max_t = []
    forecaster = mgr.forecast_at_place(place, '3h')
    forecast = forecaster.forecast
    obs = mgr.weather_at_place(place)
    weather = obs.weather
    temperature = weather.temperature(unit='celsius')['temp']
    if unit == 'Celsius':
        unit_c = 'celsius'
    else:
        unit_c = 'fahrenheit'

    for weather in forecast:
        day = datetime.utcfromtimestamp(weather.reference_time())
        date1 = day.date()
        if date1 not in dates_2:
            dates_2.append(date1)
            min_t.append(None)
            max_t.append(None)
            days.append(date1)
        temperature = weather.temperature(unit_c)['temp']
        if not min_t[-1] or temperature < min_t[-1]:
            min_t[-1] = temperature
        if not max_t[-1] or temperature > max_t[-1]:
            max_t[-1] = temperature

    obs = mgr.weather_at_place(place)
    weather = obs.weather
    weather_exp = st.expander(label='Current Weather')
    with weather_exp:
        st.title(f"Weather at {place[0].upper() + place[1:]} currently: ")
        if unit_c == 'celsius':
            st.write(f"#### 🌡️ Temperature: {temperature} °C")
        else:
            st.write(f"#### 🌡️  Temperature: {temperature} F")
        st.write(f"#### ☁️ Sky: {weather.detailed_status}")
        st.write(f"#### 🌪  Wind Speed: {round(weather.wind(unit='km_hour')['speed'])} km/h")
        st.write(f"#### ⛅️Sunrise Time :     {weather.sunrise_time(timeformat='iso')} GMT")
        st.write(f"#### ☁️  Sunset Time :      {weather.sunset_time(timeformat='iso')} GMT")

    # Expected Temperature Alerts
    alert_exp = st.expander(label='Expected Temperature Changes/Alerts:')
    with alert_exp:
        if forecaster.will_have_fog():
            st.write("### ▶️FOG ALERT🌁!!")
        if forecaster.will_have_rain():
            st.write("### ▶️RAIN ALERT☔!!")
        if forecaster.will_have_storm():
            st.write("### ▶️STORM ALERT⛈️!!")
        if forecaster.will_have_snow():
            st.write("### ▶️ SNOW ALERT❄️!!")
        if forecaster.will_have_tornado():
            st.write("### ▶️TORNADO ALERT🌪️!!")
        if forecaster.will_have_hurricane():
            st.write("### ▶️HURRICANE ALERT🌀")
        if forecaster.will_have_clear():
            st.write("### ▶️CLEAR WEATHER PREDICTED🌞!!")
        if forecaster.will_have_clouds():
            st.write("### ▶️CLOUDY SKIES⛅")

    st.write('                ')
    st.write('                ')
    plot(days, min_t, max_t)
    return min_t[0],max_t[0]


def plot(days, min_t, max_t):
    if g_type == "Line Graph":
        plot_line(days, min_t, max_t)
    elif g_type == "Bar Graph":
        plot_bars(days, min_t, max_t)

def get_ev(tmin,tmax,rs):
    if tmax>35:
        alpha=1.1+0.05*(tmax-35)
    elif tmax<5:
        alpha=0.01*math.exp(0.18*(tmax+20))
    else:
        alpha=1.1
    
    e=alpha*(3.87*0.001*rs*(0.6*tmax+0.4*tmin+29))
    return e

def get_time(e,t,h):
    time=t*(1+(e/h))
    return time

def relay(time,debug=True):
    st.write(f"the delay is set for {time*3600}")
    if not debug:
        sec=(time)*3600 #converting in sec
        RELAY_1_GPIO = 17 #pin board numbers 11
        GPIO.setup(RELAY_1_GPIO, GPIO.OUT) # GPIO Assign mode
        GPIO.output(RELAY_1_GPIO, GPIO.HIGH) # on
        time.sleep(sec)
        GPIO.output(RELAY_1_GPIO, GPIO.LOW) # out

        
if auto:
                with st.form("Time"):
                    time=st.slider("Enter time in Hours",min_value=0.01,max_value=10.,step=0.01,format="%.2f") 
                    done = st.form_submit_button("ok")
                relay(time)   

if b:
    if place != "":
        try:
            tmin,tmax=weather_detail(place, unit, g_type)
            rec_time=get_time(get_ev(tmin,tmax,solar_r),t0,h)
            st.write(f"the time for irrigation is {rec_time}")
            relay(rec_time)

        except NotFoundError:
            st.write("Please enter a Valid city name")
