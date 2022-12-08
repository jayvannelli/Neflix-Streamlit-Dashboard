import streamlit as st
import pandas as pd


st.set_page_config(page_title="Netflix Kaggle Dataset App",
                   page_icon=":popcorn:",
                   layout="wide")


@st.experimental_memo
def fetch_and_clean_data():
    pull_1 = pd.read_csv("data/raw_credits.csv").drop(columns='index')
    pull_2 = pd.read_csv("data/raw_titles.csv").drop(columns='index')
    return pull_1, pull_2


def main():

    st.title("Raw Titles & Credits Datasets")

    raw_credits, raw_titles = fetch_and_clean_data()

    credits_tab, titles_tab = st.tabs(["Credits", "Titles"])

    with credits_tab:
        st.write(raw_credits)

    with titles_tab:
        st.write(raw_titles)

        d = raw_titles.groupby("release_year", sort=False)
        st.write(d.first())


if __name__ == "__main__":
    main()
