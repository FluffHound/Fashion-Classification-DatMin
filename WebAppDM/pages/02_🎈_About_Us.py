import streamlit as st
from PIL import Image

# # SET PAGE
# pageicon = Image.open(r"E:\1.Kuliah\3. Semester 5 TSD\3. Data Mining\UAS HM\batabaca\aset_batik_icon.png")
# st.set_page_config(page_title="Bata Baca Web App", page_icon=pageicon, layout="centered")

# # SET TITLE AND LOGO IMAGE
# intro_col_left, intro_col_right = st.columns(2)
# intro_col_left.image('Bata Baca.png')
# intro_col_right.markdown('<div style="text-align: justify; font-size:250%"> <b>Web App Klasifikasi Gambar Motif Batik</b> </div>',
#             unsafe_allow_html=True)

# # DESCRIPTION
# st.markdown('<div style="text-align: justify; font-size:160%; text-indent: 4em;"> Web App ini merupakan suatu aplikasi web di mana kita bisa mengklasifikasikan suatu gambar motif batik ke dalam suatu jenis batik tertentu. Tidak hanya itu, aplikasi web ini juga memiliki fitur infopedia yang diharapkan dapat menambah wawasan pengguna mengenai budaya batik yang ada di Indonesia. </div>',
#             unsafe_allow_html=True)
# st.markdown('<div style="text-align: justify; font-size:160%; text-indent: 4em;"> Bata Baca merupakan kependekan dari Batik Kita Batik Cita. Web App ini merepresentasikan batik kita (Indonesia) yang memiliki fitur untuk mendeteksi motif batik suatu daerah di Indonesia. Dengan adanya Web App ini, kami punya harapan atau cita agar batik dapat lebih dikenal dan dilestarikan oleh masyarakat. </div>',
#             unsafe_allow_html=True)

# ANGGOTA TIM
st.write('# KELOMPOK 1 DATA MINING SD|A2')

# # DESCRIPTION
st.markdown('<div style="text-align: justify; font-size:140%; text-indent: 4em;"> Web App Image Classification on Fashion dibuat untuk memenuhi Proyek Akhir Data Mining II kelas SD-A2. Adapun Anggota kelompok 1 adalah sebagai berikut: </div>',
            unsafe_allow_html=True)
# st.markdown('<div style="text-align: justify; font-size:160%; text-indent: 4em;"> Bata Baca merupakan kependekan dari Batik Kita Batik Cita. Web App ini merepresentasikan batik kita (Indonesia) yang memiliki fitur untuk mendeteksi motif batik suatu daerah di Indonesia. Dengan adanya Web App ini, kami punya harapan atau cita agar batik dapat lebih dikenal dan dilestarikan oleh masyarakat. </div>',


col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

foto_hanif = Image.open('foto_hanif.jpeg').resize((400,400))
foto_alya = Image.open('foto_alya2.jpeg').resize((400,400))
foto_ergid = Image.open('ergid.png').resize((400,400))
foto_razin = Image.open('foto_razin.png').resize((400,400))

# For columns 1 : Introduce Adam Maurizio Winata
col1.write('### Muhammad Hanif Sudibyo')
col1.image(foto_hanif, caption = "Data Scientist")

# For columns 2 : Introduce Annaura Nabilla Masduki
col2.write('### Najma Attaqiya Alya')
col2.image(foto_alya, caption = "Data Scientist")

# For columns 3 : Introduce Muhammad Hanif Sudibyo
col3.write('### Ergidya Liviani')
col3.image(foto_ergid, caption = "Data Scientist")

# For columns 4 : Introduce Najma Attaqiya Alya
col4.write('### Razin Isyraq Thirafi')
col4.image(foto_razin, caption = "Data Scientist")