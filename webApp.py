import streamlit as st
from PIL import Image

st.title('Webshutter')
with st.expander('Start Camera'):
    camera_image = st.camera_input('Camera')


# filter1 = st.selectbox('Which Filter Do You Want?')

if camera_image:
    img = Image.open(camera_image)
    mode = st.selectbox(
        'Which Mode do you want to choose?',
        ("1", "L", "RGB", "RGBA", "CMYK", "YCbCr"))
    converted_img = img.convert(mode)
    st.image(converted_img)
    name = st.text_input('Name For the Photo:', placeholder='Enter Name here.....', key='name')
    if name:
        st.text(f'{name}.png')
    st.button('Download', key='download')
    if st.session_state['download']:
        img.save(f'{name}.png')

