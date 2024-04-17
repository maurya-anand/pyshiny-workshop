from shiny import ui, reactive, render, App
import pandas as pd

df_penguins = pd.read_csv("../../data/penguins.csv")

app_ui = ui.page_fluid(
    ui.panel_title("Shiny Reactivity Demo"),
    "Penguins dataset:",
    ui.input_numeric("n_rows", "Number of rows to sample", value=10),
    ui.output_data_frame("penguins_table")
)


def server(input):
    @reactive.calc
    def filtered_data():
        return df_penguins.head(input.n_rows())

    @render.data_frame
    def penguins_table():
        return filtered_data()

app = App(app_ui, server)