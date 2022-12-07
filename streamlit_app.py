import streamlit as st
import pandas as pd
import pandas_profiling

from streamlit_pandas_profiling import st_profile_report


@st.experimental_memo
def fetch_and_clean_data():
    pull_1 = pd.read_csv("data/raw_credits.csv").drop(columns='index')
    pull_2 = pd.read_csv("data/raw_titles.csv").drop(columns='index')
    return pull_1, pull_2


def main():
    raw_credits, raw_titles = fetch_and_clean_data()

    d = {
        "Titles": raw_titles,
        "Credits": raw_credits,
    }

    with st.sidebar:
        st.title("Credits & Titles Data")

        with st.form("report_selection_form"):
            report_selection = st.selectbox("Select DataFrame to generate profile report for:",
                                            options=["Titles", "Credits"])

            submit_button = st.form_submit_button("Load profile report")

    if submit_button:
        pr = gen_profile_report(d[report_selection], explorative=True)
        st_profile_report(pr)


@st.cache(allow_output_mutation=True)
def gen_profile_report(df, *report_args, **report_kwargs):
    return df.profile_report(*report_args, **report_kwargs)


if __name__ == "__main__":
    main()
