import streamlit as st
import seaborn as sns

st.header("This vedio is brought to you by #Muhammad Farooq")
st.text("kia app ko maza a raha ha seekhnay main")

st.header("Hello Streamlit")

df = sns.load_dataset('iris')
st.write(df[['species', 'sepal_length', 'petal_length' ]].head(10))

st.bar_chart(df['sepal_length'])
st.line_chart(df['sepal_length'])