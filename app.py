
import streamlit as st

st.set_page_config(
    page_title="Veggie AI Studio",
    page_icon="🍅",
    layout="centered"
)

st.title("🍅 Veggie AI Studio")
st.subheader("Create your own animated vegetable comedy videos!")

st.write("Welcome to your personal AI video studio.")

character = st.selectbox(
    "Choose your vegetable character",
    ["Tomato", "Onion", "Potato", "Chilli"]
)

st.write(f"Your selected character: {character}")

story = st.text_area(
    "Enter your funny story",
    placeholder="Example: Tomato and Onion are fighting over who is the king of the kitchen..."
)

if st.button("Create my video"):
    if story.strip():
        st.success("Your story is ready for the animation stage!")
    else:
        st.warning("Please enter a story first.")
