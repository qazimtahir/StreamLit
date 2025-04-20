import streamlit as st

st.title("This is a title")

st.subheader("This is a subheader")

st.write("Hello from Streamlit!")

st.text("This is a text")

st.markdown("This is a markdown")

st.code("This is a code")

subject = st.selectbox("Which is your favourite programing language?", ["TypeScript", "Python", "JavaScript", "Java", "C#", "AI", "Agentic AI"])

st.write(f"You selected {subject}")

agree = st.checkbox("I agree")

if agree:
    st.write("Okay!")
else:
    st.write("Please agree to continue")

