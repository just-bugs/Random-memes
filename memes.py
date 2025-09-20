import streamlit as st
import os
import random
from PIL import Image

# --- Page Config ---
st.set_page_config(
    page_title="Random Meme Generator",
    page_icon="🤣",
    layout="centered",
)

# --- CSS for funny UI ---
st.markdown("""
<style>
    .main {
        background-color: #f0f8ff;
        padding: 2rem;
    }
    .stButton>button {
        background-color: #ffcc00;
        color: black;
        font-size: 20px;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 20px;
        margin-top: 20px;
    }
    .stImage>img {
        border-radius: 15px;
        box-shadow: 5px 5px 15px grey;
    }
</style>
""", unsafe_allow_html=True)

# --- Title ---
st.title("Random Meme Generator 😂")
st.subheader("Press the button to get a random meme!")

# --- Folder with memes ---
MEME_FOLDER = "./memes"  # Replace with your folder path
meme_files = [f for f in os.listdir(MEME_FOLDER) if f.endswith((".png", ".jpg", ".jpeg"))]

# --- Button to generate meme ---
if st.button("Generate Meme! 😂"):
    if meme_files:
        meme_path = os.path.join(MEME_FOLDER, random.choice(meme_files))
        meme_image = Image.open(meme_path)
        st.image(meme_image, use_container_width=True)
        st.success("Here's your meme! Enjoy! 😎")
    else:
        st.error("No memes found in your folder.")

# --- Footer ---
st.markdown("Made with ❤️ for meme lovers!")
st.markdown("Made by [Kweku Dzata](https://www.instagram.com/kwekudzata/)")
