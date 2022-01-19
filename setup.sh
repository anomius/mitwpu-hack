#!/bin/sh
python -m venv venv 
source venv/bin/activate
pip install -r requirements.txt
streamlit run index.py
 