import streamlit as st
import pandas as pd


@st.experimental_memo
def fetch_and_clean_data():
    pull_1 = pd.read_csv("data/raw_credits.csv").drop(columns='index')
    pull_2 = pd.read_csv("data/raw_titles.csv").drop(columns='index')
    return pull_1, pull_2


def main():
    raw_credits, raw_titles = fetch_and_clean_data()

    st.write(raw_titles, raw_credits)


if __name__ == "__main__":
    main()
