from shiny import ui, reactive, render
from shiny.express import input
import pandas as pd

df_penguins = pd.read_csv("data/penguins.csv")

ui.panel_title("Shiny Reactivity Demo")
ui.input_numeric("n_rows", "Number of rows to sample", value=10)

"Penguins dataset:"

@reactive.calc
def filtered_data():
    return df_penguins.head(input.n_rows())

@render.data_frame
def penguins_table():
    return filtered_data()
