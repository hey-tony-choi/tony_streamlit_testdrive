import streamlit as st

st.title("🎈 My second app")
st.write(
    "Let's start building!"
)

st.subheader("image section")
st.image("https://static.streamlit.io/examples/cat.jpg", caption="귀여운 고양이", use_container_width=True)

st.code("""
import streamlit as st
st.title('Hello World')
""", language="python")

