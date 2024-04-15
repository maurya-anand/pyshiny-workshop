from dash import Dash, html, dcc, Output, Input, dash_table
import pandas as pd

df_penguins = pd.read_csv("data/penguins.csv")

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Dash Reactivity Demo"),
    html.P("Penguins dataset:"),
    html.P("Number of rows to sample:"),
    dcc.Input(
        id='numeric-input',
        type='number',
        value=10,
    ),
    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df_penguins.columns]
    )
])

@app.callback(
    Output('table', 'data'),
    Input('numeric-input', 'value')
)
def update_table(n):
    return df_penguins.head(n).to_dict('records')

if __name__ == '__main__':
    app.run_server(debug=True)