import reflex as rx
import pandas as pd

DEFAULT_ROWS = 10


class State(rx.State):
    penguins_table: pd.DataFrame = pd.read_csv("penguins.csv")
    filtered_data: pd.DataFrame = penguins_table.head(DEFAULT_ROWS)

    def filter_dataframe(self, n_rows: str):
        n_rows = int(n_rows)
        self.filtered_data = self.penguins_table.head(n_rows)


def index():
    return rx.vstack(
        rx.heading("Shiny Reactivity Demo", font_size="2em"),
        "Number of rows to show",
        rx.input(
            name="Number of rows to show",
            type="number",
            default_value=str(DEFAULT_ROWS),
            on_change=State.filter_dataframe,
        ),
        "Penguins dataset:",
        rx.data_table(data=State.filtered_data),
    )


app = rx.App()
app.add_page(index)
