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