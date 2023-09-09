# Import libraries
import streamlit as st
from PIL import Image

st.write('''# Add media files in streamlit web_app''')

# Add Image
st.write('''## Image''')
image1 = Image.open('snowleopard.jpg')
st.image(image1)

# Add video
st.write('''## Video''')
video1 = open('Leo.mp4', 'rb')
st.video(video1)

# Add Audio
st.write('''## Audio''')
audio1 = open('Leo.mp3', 'rb')
st.audio(audio1)