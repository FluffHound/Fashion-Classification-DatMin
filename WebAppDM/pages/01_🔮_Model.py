import streamlit as st
import numpy as np
import tensorflow as tf
import cv2
from tensorflow import keras
from keras.utils import load_img, img_to_array
from keras.applications.inception_v3 import preprocess_input
from PIL import Image

# SET PAGE
# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
pageicon = Image.open("aset_batik_icon.png")
st.set_page_config(page_title="Bata Baca Web App", page_icon=pageicon, layout="centered")

# SET TITLE
st.title('Yuk Kenali Motif Batikmu!')

# DESCRIPTION
st.markdown('<div style="text-align: justify; font-size:160%"> Apakah kalian memiliki batik yang yang belum diketahui jenis motifnya? Nah, untuk menjawab rasa penasaran itu, yuk <i>upload</i> foto motif batik yang kalian punya disini! Kalian bisa langsung meng-<i>upload</i> batik kalian atau dapat menggunakan live foto pada <i>website</i> kami! <i>Lets try</i>!!! </div>',
            unsafe_allow_html=True)
st.write('')

# LOAD MODEL
# model = keras.models.load_model('Model_InceptionV3.h5')
# Decorator to cache non-data objects
@st.experimental_singleton
def InceptionV3():
    # Load large model
    model = keras.models.load_model('Model_InceptionV3.h5')
    return model

# Model is now cached
model = InceptionV3()

# LABELS
labels = ['Batik Bali', 'Batik Betawi', 'Batik Cendrawasih', 'Batik Dayak', 'Batik Geblek Renteng',
          'Batik Ikat Celup', 'Batik Insang', 'Batik Kawung', 'Batik Lasem', 'Batik Megamendung',
          'Batik Pala', 'Batik Parang', 'Batik Poleng', 'Batik Sekar Jagad', 'Batik Tambal']

# CHOOSE FILE
option = st.selectbox(
    'How would you like to upload your file?',
    ('Upload a File', 'Camera'))

if option == 'Upload a File':
    uploaded_files = st.file_uploader("Upload a Batik File Image", type=['img', 'png', 'jpg', 'jpeg'])
    if uploaded_files is not None:
        # load an image from file
        image = load_img(uploaded_files, target_size=(224, 224))
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
        mid_column_chart1.image(uploaded_files, use_column_width=True, caption="Motif Batik")
        text_res = "Motif Batik di atas tergolong ke motif : "
        result = text_res + result
        st.success(result)
else:
    # camera = st.button("Take a picture from Camera")
    picture = st.camera_input("Take a picture")
    if picture is not None:
        # load an image from file
        image = load_img(picture, target_size=(224, 224))
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
        mid_column_chart1.image(picture, use_column_width=True, caption="Motif Batik")
        text_res = "Motif Batik di atas tergolong ke motif : "
        result = text_res + result
        st.success(result)