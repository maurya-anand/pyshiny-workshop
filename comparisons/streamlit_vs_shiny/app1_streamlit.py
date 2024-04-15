import streamlit as st
import pandas as pd

st.title("Streamlit Reactivity Demo")
slider = st.slider("Number of rows to show", 1, 100, 10)

"Penguins dataset:"

df_penguins = pd.read_csv("data/penguins.csv")

filtered_data = df_penguins.head(slider)

st.dataframe(filtered_data)