import streamlit as st
from PIL import Image

#テキスト関連
st.title('Streamlit 超入門')
st.caption("This is a caption")

#画像
image =Image.open('./data/image.jpg')
st.image(image,width=300, caption='dog')