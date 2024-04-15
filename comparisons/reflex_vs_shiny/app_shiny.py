from shiny import ui, reactive, render, App
import pandas as pd

app_ui = ui.page_fluid(
    ui.panel_title("Shiny Reactivity Demo"),
    ui.input_numeric("n_rows", "Number of rows to show", value=10),
    "Penguins dataset:",
    ui.output_data_frame("penguins_table"),
)

def server(inputs, outputs, session):
    @reactive.calc
    def data():
        return pd.read_csv("penguins.csv")

    @reactive.calc
    def filtered_data():
        return data().head(inputs.n_rows())
    
    @render.data_frame
    def penguins_table():
        return filtered_data()

app = App(app_ui, server)
