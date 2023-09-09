import streamlit as st
from streamlit_embedcode import github_gist

link = "https://gist.github.com/MuhammadFarooq2022/245ad82fb7197312bc087268a4176e87"

st.write('Embed github gist:')

github_gist(link)