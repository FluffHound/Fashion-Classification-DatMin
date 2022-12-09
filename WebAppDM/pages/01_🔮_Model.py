import streamlit as st
import numpy as np
from tensorflow import keras
from keras.utils import load_img, img_to_array
from keras.applications.inception_v3 import preprocess_input
from PIL import Image

# SET PAGE
# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
pageicon = Image.open("./WebAppDM/assets/FashioniFy.png")
st.set_page_config(page_title="Fashionify Web App", page_icon=pageicon, layout="centered")

# SET TITLE
st.markdown("<h1 style='text-align: center;'>Prediksi Kategori Pakaian Disini</h1>", unsafe_allow_html=True)

# DESCRIPTION
# ___dataset___
st.markdown("""<div style="text-align: justify; font-size:120%">
Dataset merupakan gambar display berbagai tipe kategori produk yang diambil dari website pihak ketiga, yaitu Dior, Louis Vuitton, Gucci, Prada, dan Uniqlo. Data diambil menggunakan metode scraping pada beberapa halaman website sesuai dengan kategori yang telah ditentukan.
</div>""", unsafe_allow_html=True)

st.markdown("""<div style="text-align: justify; font-size:120%">
<br>
Kategori dataset yang digunakan diantaranya:
</div>""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""<div style="text-align: justify; font-size:120%">
        <ul>
            <li>Bags</li>
            <li>Belts</li>
            <li>Boots</li>
            <li>Dresses</li>
            <li>Hats</li>
            <li>Jackets</li>
            <li>Jewelry</li>
            <li>Knitwear</li>
        </ul>
    </div>""", unsafe_allow_html=True)

with col2:
    st.markdown("""<div style="text-align: justify; font-size:120%">
        <ul>
            <li>Loafers</li>
            <li>Pants</li>
            <li>Sandals</li>
            <li>Scarves</li>
            <li>Skirts</li>
            <li>Sneakers</li>
            <li>Sunglasses</li>
            <li>T-Shirts</li>
        </ul>
        <br>
    </div>""", unsafe_allow_html=True)

# ___model___
st.markdown("""
<div style="text-align: justify; font-size:120%">
    Upload gambar fashion menggunakan metode upload gambar atau ambil foto menggunakan kamera device:
    <br>
</div>""", unsafe_allow_html=True)

# LOAD MODEL
# model = keras.models.load_model('Model_InceptionV3.h5')
@st.experimental_singleton # Decorator to cache non-data objects
def InceptionV3():
    # Load large model
    model = keras.models.load_model('model_inception.h5')
    return model

# Model is now cached
model = InceptionV3()

# LABELS
labels = ['Bags','Belts','Boots','Dresses','Hats','Jackets & Coats','Jewelry','Knitwear','Loafers',
 'Pants','Sandals','Scarves','Skirt','Sneakers','Sunglasses','T-Shirts']

# CHOOSE FILE
option = st.selectbox(
    'Metode unggah gambar',
    ('Upload File', 'Ambil Gambar'))

if option == 'Upload File':
    uploaded_files = st.file_uploader("Upload gambar produk", type=['img', 'png', 'jpg', 'jpeg'])
    if uploaded_files is not None:
        # load an image from file
        image = load_img(uploaded_files, target_size=(400, 400))
        # convert the image pixels to a numpy array
        image_pixels = img_to_array(image)
        # reshape data for the model
        image_reshape = image_pixels.reshape((1, image_pixels.shape[0], image_pixels.shape[1], image_pixels.shape[2]))
        # prepare the image for the Inception model
        image_preprocess = preprocess_input(image_reshape)
        # predict the probability across all output classes
        yhat = model.predict(image_preprocess)
        index = np.argmax(yhat)
        result = labels[index]
        left_column_chart1, mid_column_chart1, right_column_chart1 = st.columns([0.5, 7, 0.5])
        mid_column_chart1.image(uploaded_files, use_column_width=True, caption="Gambar Produk")
        text_res = "Label hasil prediksi model: "
        result = text_res + result
        st.success(result)
else:
    # camera = st.button("Take a picture from Camera")
    picture = st.camera_input("Take a picture")
    if picture is not None:
        # load an image from file
        image = load_img(picture, target_size=(400, 400))
        # convert the image pixels to a numpy array
        image_pixels = img_to_array(image)
        # reshape data for the model
        image_reshape = image_pixels.reshape((1, image_pixels.shape[0], image_pixels.shape[1], image_pixels.shape[2]))
        # prepare the image for the VGG model
        image_preprocess = preprocess_input(image_reshape)
        # predict the probability across all output classes
        yhat = model.predict(image_preprocess)
        index = np.argmax(yhat)
        result = labels[index]
        left_column_chart1, mid_column_chart1, right_column_chart1 = st.columns([0.5, 7, 0.5])
        mid_column_chart1.image(picture, use_column_width=True, caption="Gambar Produk")
        text_res = "Label hasil prediksi model: "
        result = text_res + result
        st.success(result)