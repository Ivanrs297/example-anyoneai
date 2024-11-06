import streamlit as st
from sklearn.datasets import load_iris

data = load_iris(as_frame = True)
df = data.frame


st.title("Example for asdfsda")
st.header("Hello Ivan from AnyoneAI")
st.subheader("This is a subheader")
st.write("sadlfkjnsdklfj lksjhadf lkjsdflj")

st.dataframe(df)