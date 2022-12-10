import streamlit as st
import pandas as pd

st.write("""#first
Hello """)
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
