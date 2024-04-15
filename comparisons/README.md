# Shiny Comparisons

Run from the root workshop directory.

## Shiny examples

```bash
shiny run comparisons/dir/app_shiny.py --reload
```

## Dash examples

```bash
python comparisons/dir/app_dash.py
```

## Streamlit examples

```bash
streamlit run comparisons/dir/app_streamlit.py
```

## Reflex example

This needs a separate environment to run.
You can use for example `poetry` for dependency management.
Then run example with **from the `comparisons/reflex_vs_shiny/`** directory:

```bash
poetry run reflex run
```