# IMPORT LIBRARY
import streamlit as st
from PIL import Image
import plotly.express as px
import pandas as pd
import numpy as np

# SET PAGE
pageicon = Image.open("aset_batik_icon.png")
st.set_page_config(page_title="Bata Baca Web App", page_icon=pageicon, layout="centered")

# MENAMPILKAN INFOPEDIA
#Judul 
# st.write('# Image Classification on Fashion')
# image = Image.open('FashioniFy.png')
# st.image(image,caption=None, width=500)

# pageicon = Image.open("FashioniFy.png")
# st.set_page_config(page_title="Bata Baca Web App", page_icon=pageicon, layout="centered")
intro_col_left, intro_col_right = st.columns(2)
intro_col_left.image('./assets/FashioniFy.png')
intro_col_right.markdown('<div style="text-align: center; font-size:300%"> <b>Web App Image Classification on Fashion</b> </div>',
            unsafe_allow_html=True)
st.markdown('<hr>', unsafe_allow_html=True)
st.markdown(
        '<div style="text-align: justify; font-size:110%; text-indent: 4em;"> Website ini digunakan untuk mengklasifikasikan gambar fashion untuk mengetahui kelas masing-masing label. Adapun Dataset yang berasal dari brand ternama seperti Gucci, Dior, Louis Vuitton, Prada, dan Uniqlo. Dataset yang didapatkan terdiri atas 4750 dataset dengan distribusi data sebagai berikut: </div>',
        unsafe_allow_html=True)

# ====================
# ===== Bar Chart ====
# ====================
# Add histogram data
data = [423, 263, 392, 220, 255, 396, 310, 665, 403, 628, 531, 250, 268, 357, 266, 677]
cols = ['Bags','Belts','Boots','Dresses','Hats','Jackets & Coats','Jewelry','Knitwear','Loafers','Pants','Sandals','Scarves','Skirt','Sneakers','Sunglasses','T-Shirts']
df_plot = pd.DataFrame(zip(data, cols), columns=['data', 'labels'])

# Create barplot with custom bin_size
fig = px.bar(df_plot, x='labels', y='data')

# Plot!
st.plotly_chart(fig, use_container_width=True)
# # SAMPEL DATASET 
st.markdown(
        '<div style="text-align: justify; font-size:110%; text-indent: 4em;"> Adapun sampel dataset dapat dilihat pada gambar berikut</div>',
        unsafe_allow_html=True)


intro_col_left1, intro_col_right1, intro_col_left2, intro_col_right2 = st.columns(4)
st.markdown('<hr>', unsafe_allow_html=True)
intro_col_left1.image('./assets/bag.jpg', caption="Bags")
intro_col_right1.image('./assets/belt.png', caption="Belt")
intro_col_left2.image('./assets/Boots.png', caption="Boots")
intro_col_right2.image('./assets/dress.png', caption="Dresses")

intro_col_left1.image('./assets/topi.png', caption="Hats")
intro_col_right1.image('./assets/jackets and coats.png', caption="Jackets and Coats")
intro_col_left2.image('./assets/jewelry.png', caption="Jewelry")
intro_col_right2.image('./assets/knitwear.png', caption="Knitwear")

intro_col_left1.image('./assets/loafers.png', caption="Loafers")
intro_col_right1.image('./assets/pants.png', caption="Pants")
intro_col_left2.image('./assets/sendals.png', caption="Sandals")
intro_col_right2.image('./assets/scarves.png', caption="Scarves")

intro_col_left1.image('./assets/skirt.png', caption="Skirt")
intro_col_right1.image('./assets/sneakers.png', caption="Sneaker")
intro_col_left2.image('./assets/sunglasses.png', caption="Sunglasses")
intro_col_right2.image('./assets/T-shirt.png', caption="T-shirt")
