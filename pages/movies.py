import streamlit as st
import pandas as pd


@st.experimental_memo
def fetch_and_clean_movies_data():
    pull_1 = pd.read_csv("data/Best Movie by Year Netflix.csv").drop(columns='index')
    pull_2 = pd.read_csv("data/Best Movies Netflix.csv").drop(columns='index')
    return pull_1, pull_2


def main():
    best_movies_by_year, best_movies = fetch_and_clean_movies_data()

    st.write(best_movies_by_year, best_movies)


if __name__ == "__main__":
    main()

