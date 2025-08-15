import streamlit as st

st.title("🎈 Make app great again")
st.write(
    "Let's start building!"
)

st.subheader("1.image section")
st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYWhvN3EydGxnYmY5cWl4aHQzbXFmaDN5M2NiZnJ6YnAxczFyejM3NCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/WrIiyrvaFSeyVlxwtx/giphy.gif", caption="You're the best", use_container_width=True)

st.subheader("2. code section")
st.code("""
import streamlit as st
st.title('Hello World')
""", language="python")

