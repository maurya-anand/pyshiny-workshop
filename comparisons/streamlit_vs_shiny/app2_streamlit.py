import streamlit as st
import pandas as pd


df_penguins = pd.read_csv("../../data/penguins.csv")

st.title("Streamlit Reactivity Demo 2")
slider = st.slider("Number of rows to sample", 1, 100, 10)
dropped_species = st.multiselect("Drop Species", df_penguins["Species"].unique().tolist())
"Penguins dataset:"

sampled_df_penguins = df_penguins.sample(n = slider)
filtered_data = sampled_df_penguins.loc[~sampled_df_penguins['Species'].isin(dropped_species)]

st.dataframe(filtered_data)