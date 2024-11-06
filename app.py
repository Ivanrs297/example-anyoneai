import streamlit as st
from sklearn.datasets import load_wine

data = load_wine(as_frame = True)
df = data.frame


st.title("Example for Streamlit")
st.header("Hello Ivan from AnyoneAI")
st.subheader("This is a subheader")
st.write("This is an example for Wine Dataset")

st.dataframe(df)