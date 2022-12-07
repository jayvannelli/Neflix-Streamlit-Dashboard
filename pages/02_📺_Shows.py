import streamlit as st
import pandas as pd


@st.experimental_memo
def fetch_and_clean_shows_data():
    pull_1 = pd.read_csv("data/Best Show by Year Netflix.csv").drop(columns='index')
    pull_2 = pd.read_csv("data/Best Shows Netflix.csv").drop(columns='index')
    return pull_1, pull_2


def main():
    best_shows_by_year, best_shows = fetch_and_clean_shows_data()

    best_shows_tab, best_shows_by_year_tab = st.tabs(
        ["Best Shows", "Best Shows (By Year)"]
    )

    with best_shows_tab:
        st.write(best_shows)

    with best_shows_by_year_tab:
        st.write(best_shows_by_year)


if __name__ == "__main__":
    main()
