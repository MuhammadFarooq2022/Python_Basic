import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
from pandas_profiling import ProfileReport, profile_report
from streamlit_pandas_profiling import st_profile_report

# Webapp ka Title
st.markdown('''
# **Exploratory data Analysis web application**
This app is developed by codanics youtube channel called **EDA App**
 ''')

# How to upload a file from PC

with st.sidebar.header("Upload your Dataset (.csv)"):
    uploaded_file = st.sidebar.file_uploader("Upload your file", type=['CSV'])
    df = sns.load_dataset('titanic')
    st.sidebar.markdown("[Example CSV file](df)")

# Profiling report for panads

if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DF**')
    st.write('---')
    st.header('**Profiling report with pandas**')
    st_profile_report(pr)
else:
    st.info('Awaiting for CSV file, upload kar bi do ka kaam nahi lena?')
    if st.button('Press to use example data'):
        # example dataset
        @st.cache
        def load_data():
            a = pd.DataFrame( np.random.rand(100, 5),
                                columns=["age", 'banana', 'codanics', 'Deutchland', 'Ear' ])
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write('---')
        st.header('**Pandas Profiling Report**')
        st_profile_report(pr)
