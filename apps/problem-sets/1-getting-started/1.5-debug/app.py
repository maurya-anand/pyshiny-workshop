from shiny.express import ui, render
import pandas as pd
from pathlib import Path

infile = Path(__file__).parent / "penguins.csv"
penguins = pd.read_csv(infile)


@render.plot
def penguins_df():
    return penguins
