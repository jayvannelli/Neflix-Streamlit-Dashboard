import streamlit as st
import pandas as pd

from streamlit_extras.dataframe_explorer import dataframe_explorer


@st.experimental_memo
def fetch_and_clean_movies_data():
    pull_1 = pd.read_csv("data/Best Movie by Year Netflix.csv").drop(columns='index')
    pull_2 = pd.read_csv("data/Best Movies Netflix.csv").drop(columns='index')
    return pull_1, pull_2


def main():
    best_movies_by_year, best_movies = fetch_and_clean_movies_data()

    best_movies_tab, best_movies_by_year_tab  = st.tabs(
        ["Best Movies", "Best Movies (By Year)"]
    )

    with best_movies_tab:
        filtered_best_movies = dataframe_explorer(best_movies)

        st.dataframe(filtered_best_movies, use_container_width=True)

    with best_movies_by_year_tab:
        st.write(best_movies_by_year)


if __name__ == "__main__":
    main()
