import streamlit as st
import pandas as pd


@st.experimental_memo
def fetch_and_clean_movies_data():
    pull_1 = pd.read_csv("data/Best Movie by Year Netflix.csv").drop(columns='index')
    pull_2 = pd.read_csv("data/Best Movies Netflix.csv").drop(columns='index')
    return pull_1, pull_2


def main():
    best_movies_by_year, best_movies = fetch_and_clean_movies_data()

    best_movies_tab, best_movies_by_year_tab = st.tabs(
        ["Best Movies", "Best Movies (By Year)"]
    )

    with best_movies_tab:
        st.write(best_movies)

    with best_movies_by_year_tab:

        def analyze_data(grp):
            return grp.mean()

        d = best_movies_by_year.groupby(
            ["MAIN_GENRE", "MAIN_PRODUCTION"], as_index=False)['SCORE']\
            .apply(analyze_data)

        st.write(d)

        st.write(best_movies_by_year)


if __name__ == "__main__":
    main()
