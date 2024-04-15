from shiny import ui, reactive, render
from shiny.express import input
import pandas as pd

df_penguins = pd.read_csv("data/penguins.csv")

ui.panel_title("Shiny Reactivity Demo 2")
ui.input_numeric("n_rows", "Number of rows to sample", value=10)
ui.input_selectize("dropped_species", "Drop Species", choices=df_penguins["Species"].unique().tolist(), multiple=True)
"Penguins dataset:"


@reactive.calc
def sampled_df_penguins():
    return df_penguins.sample(n = input.n_rows())
    

@reactive.calc
def filtered_data():
    df = sampled_df_penguins()
    df = df.loc[~df['Species'].isin(input.dropped_species())]
    return df

@render.data_frame
def penguins_table():
    return filtered_data()
