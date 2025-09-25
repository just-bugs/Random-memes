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

# --- CSS for UI ---
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

# --- Folder with memes ---
MEME_FOLDER = "./memes"
os.makedirs(MEME_FOLDER, exist_ok=True)

# --- Sidebar navigation ---
pages = {
    "generator": "🎉 Meme Generator",
    "upload": "📤 Upload Meme"
}
choice = st.sidebar.radio("📂 Navigation", list(pages.values()))

# --- Resolve choice back to key ---
if choice == pages["generator"]:
    page = "generator"
elif choice == pages["upload"]:
    page = "upload"

# --- Meme Generator Page ---
if page == "generator":
    st.title("Random Meme Generator 😂")
    st.subheader("Press the button to get a random meme!")

    meme_files = [f for f in os.listdir(MEME_FOLDER) if f.lower().endswith((".png", ".jpg", ".jpeg"))]

    if st.button("Generate Meme! 😂"):
        if meme_files:
            meme_path = os.path.join(MEME_FOLDER, random.choice(meme_files))
            meme_image = Image.open(meme_path)
            st.image(meme_image, use_container_width=True)
            st.success("Here's your meme! Enjoy! ")
        else:
            st.error("No memes found in your folder.")

    st.markdown("Made with ❤️ for meme lovers!")
    st.markdown("Created by [Kweku Dzata](https://github.com/just-bugs)")

# --- Upload Meme Page ---
elif page == "upload":
    st.title("Upload Your Meme 🤩")
    st.subheader("Contribute to the collection!")

    uploaded_file = st.file_uploader("Choose a meme image", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        save_path = os.path.join(MEME_FOLDER, uploaded_file.name)
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"✅ Meme '{uploaded_file.name}' uploaded successfully!")
