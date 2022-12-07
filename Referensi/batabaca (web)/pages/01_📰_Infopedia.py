# IMPORT LIBRARY
import streamlit as st
from PIL import Image

# SET PAGE
pageicon = Image.open("aset_batik_icon.png")
st.set_page_config(page_title="Bata Baca Web App", page_icon=pageicon, layout="centered")

# ---- SIDEBAR ----
st.sidebar.header("Infopedia Batik")

jenis_info = st.sidebar.selectbox(
    'Pilih jenis infopedia mengenai batik di sini',
    ('Sejarah Batik Nusantara',
     'Batik Sumatera',
     'Batik Jawa',
     'Batik Kalimantan',
     'Batik Sulawesi',
     'Batik Bali, NTB, dan NTT',
     'Batik Maluku dan Papua'))

# MENAMPILKAN INFOPEDIA
if jenis_info == 'Sejarah Batik Nusantara':
    st.header('Sejarah Batik di Nusantara')
    st.markdown('<hr>', unsafe_allow_html=True)
    left_column_info1, mid_column_info1, right_column_info1 = st.columns([0.5, 7, 0.5])
    mid_column_info1.image('aset_batik_info1.jpg', use_column_width=True, caption="Gambar Motif Batik")
    st.markdown(
        '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Batik merupakan salah satu cagar budaya warisan Indonesia yang merupakan salah satu bentuk seni kuno yang adiluhung. Batik sendiri berasal dari bahasa Jawa yakni “amba” yang berarti tulis dan “nitik” yang berarti titik. Arti secara keseluruhan, membatik diatas kain menggunakan canting yang ujungnya kecil memberi kesan “orang sedang menulis titik-titik”.  Batik dikenal nenek moyang sejak abad XIII, dimana pada saat itu, batik dilukis atau ditulis diatas daun lontar. Van Roojen (2001) menyatakan bahwa batik klasik bersumber pada arus budaya yang mendasarinya, yakni pada masa kerajaan Mataram II (1575-1755) di Pulau Jawa.</div>',
        unsafe_allow_html=True)

    st.markdown(
        '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Perkembangan batik di Indonesia erat kaitannya dengan perkembangan Kerajaan Majapahit. Batik terus berkembang hingga pada zaman Kerajaan Mataram, Solo dan Yogyakarta. </div>',
        unsafe_allow_html=True)

    st.markdown(
        '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Batik pada awalnya hanya digunakan di lingkungan keraton saja, hal ini dapat dilihat bahwa motif batik di Indonesia dapat ditemukan di berbagai artefak budaya di Indonesia. Misalnya, motif dasar lereng ditemukan di patung emas syiwa yang dibuat pada abad IX, di Wonosobo. Dasar motif ceplok ditemukan pada pakaian patung Ganesha di Candi Banon dekat Borobudur yang dibuat pada abad IX. Motif liris juga ditemukan pada patung Manjusri, Semarang yang dibuat pada abad X.  </div>',
        unsafe_allow_html=True)

    st.markdown(
        '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Banyak pengikut raja yang tinggal di luar keraton yang membawa kesenian batik di daerahnya masing-masing. Batik selanjutnya melebarkan sayapnya keluar keraton seiring dengan perkembangan zaman dari kebutuhan individu menjadi kebutuhan industrial. Popularitas batik mulai meningkat pada akhir tahun ke-18 atau awal abad ke-19. Munculnya batik cap menandakan era baru dalam industrialisasi. Sebelumnya, membatik merupakan pekerjaan yang digunakan sebagai pekerjaan sampingan yang dilakukan di rumah. Dengan ditemukannya teknik membatik dengan sistem cap menyebabkan banyak tumbuh industri-industri kecil yang mampu memproduksi batik dalam jumlah yang banyak dalam waktu yang singkat. Tidak berhenti disitu, perkembangan industrialisasi dan globalisasi melahirkan teknik otomatisasi batik jenis baru, yakni batik printing. Batik printing sangat mempengaruhi arah industrial batik, hal ini dikarenakan prosesnya yang lebih cepat dan dan harganya yang relatif lebih murah. </div>',
        unsafe_allow_html=True)

elif jenis_info == 'Batik Sumatera':
    st.header('Yuk Berkenalan dengan Jenis-Jenis Batik di Pulau Sumatera!')
    st.markdown('<hr>', unsafe_allow_html=True)
    batik_sumatera = st.selectbox(
        'Pilih jenis daerah',
        ('Nanggroe Aceh Darussalam',
         'Sumatera Utara',
         'Sumatera Barat',
         'Sumatera Selatan',
         'Riau',
         'Jambi',
         'Bengkulu',
         'Bangka Belitung',
         'Lampung'))
    if batik_sumatera == 'Nanggroe Aceh Darussalam':
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Motif Batik Aceh menggunakan unsur alam dan budaya Aceh dalam paduan berbagai warnanya. Warna yang banyak diterapkan pada Batik Aceh lebih dominan pada warna-warna cerah seperti merah, hijau, merah muda, kuning, dan lain sebagainya. Pada motif Batik Aceh jarang menggunakan motif binatang karena larangan syariat Islam untuk menggambarkan makhluk bernyawa dalam pembuatan kain batik. Pengaruh Islam yang kuat tercermin pada motif ragam hias bentuk sulur, melingkar, dan garis-garis pada setiap motif. </div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Ceplok Gayo")
        _, mid_column_cepgayo, _ = st.columns([0.5, 7, 0.5])
        mid_column_cepgayo.image('aset/aceh/Ceplok Gayo.png', use_column_width=True, caption="Motif Batik Ceplok Gayo")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Motif ini berupa ceplok-ceplok gambar yang dikembangkan dari ukiran Motif Kerawang Gayo. Ceplok adalah istilah gambar utuh yang berdiri sendiri. Warna yang dipilih adalah warna-warni khas Aceh Gayo dengan latar hitam pekat, sehingga motif ceplokan terlihat kontras menonjol namun tetap harmonis dalam ikatan warna hitam. Motif ceplok warna-warni menggambarkan segala perbedaan yang ada dalam masyarakat adalah karunia yang harus disyukuri dan diterima secara wajar.   </div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Kerawang Gayo Tegak")
        _, mid_column_gayoteg, _ = st.columns([0.5, 7, 0.5])
        mid_column_gayoteg.image('aset/aceh/Kerawang Gayo Tegak.png', use_column_width=True, caption="Motif Batik Kerawang Gayo Tegak")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Motif ini berupa sulur-sulur yang sambung menyambung seakan tiada henti. Motif ini digambarkan dalam posisi tegak atau vertikal sebagai ungkapan untuk selalu teringat pada Tuhan Yang Maha Esa. Warna yang dipilih adalah warna putih, kuning, dan hitam. Putih melambangkan kesucian, kuning melambangkan kemuliaan, dan hitam melambangkan kekuatan dan kesungguhan. </div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Kerawang Datar")
        _, mid_column_kerdat, _ = st.columns([0.5, 7, 0.5])
        mid_column_kerdat.image('aset/aceh/kerawang Datar.png', use_column_width=True, caption="Motif Batik Kerawang Datar")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Motif ini berupa sulur-sulur yang sambung menyambung seakan tiada henti. Motif ini digambarkan dalam posisi mendatar sebagai ungkapan pakaian sehari-hari untuk bekerja dan bermasyarakat atau dalam ajaran Islam dikenal dengan istilah habluminannas. Warna yang dipilih adalah warna merah, putih, dan kuning yang merupakan salah satu warna cerah kesukaan masyarakat Aceh Gayo. Konsep penciptaan motif ini adalah menggambarkan keindahan seni budaya, serta semangat berkerja keras penuh kompetitif (warna merah) namun dalam tata aturan yang suci, luhur, dan mulia yaitu ajaran agama dan adat (warna putih dan kuning). </div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Parang Gayo")
        _, mid_column_pargay, _ = st.columns([0.5, 7, 0.5])
        mid_column_pargay.image('aset/aceh/Parang Gayo.png', use_column_width=True, caption="Motif Batik Parang Gayo")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Motif ini digambarkan dalam posisi miring kurang lebih 45 derajat seperti halnya Motif Parang dari Jawa. Warna yang dipilih adalah warna merah, putih, dan kuning yang merupakan salah satu warna cerah kesukaan masyarakat Aceh Gayo. Batik ini menggambarkan keindahan seni budaya, serta semangat berkerja keras (warna merah) namun tetap dalam tata aturan yang suci, luhur, dan mulia yaitu ajaran agama dan adat (warna putih dan kuning). Komposisi gambar dalam posisi miring menggambarkan gerak yang dinamis, sebagaimana makna garis miring sebagai simbol gerak atau tidak diam.  </div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Kerawang Lembut")
        _, mid_column_kerlem, _ = st.columns([0.5, 7, 0.5])
        mid_column_kerlem.image('aset/aceh/Kerawang Lembut.png', use_column_width=True,caption="Motif Batik Kerawang Lembut")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Bidang-bidang geometris yang dipadu alur-alur horizontal membentuk irama ritmis dengan pengisian warna yang dinamis. Dikomposisi pula dengan motif sulur-sulur dan ukel untuk mengisi bidangbidang geometris tersebut. Pengulangan-pengulangan unsur-unsur gambar dalam ukuran kecil tersebut mampu menghasilkan desain motif yang lebih lembut dan luwes. Warna yang dipilih adalah warna-warni khas Aceh Gayo  dengan latar kuning tua.  </div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Geometris Gayo")
        _, mid_column_geogay, _ = st.columns([0.5, 7, 0.5])
        mid_column_geogay.image('aset/aceh/Geometris Gayo.png', use_column_width=True, caption="Motif Batik Geometris Gayo")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Motif ini sumber inspirasinya dari motif bagian motif ukiran kerawang yang bentuknya geometris yang dipadu dengan motif sulur-sulur untuk mengisi bidang-bidang geometris tersebut. Motif terlihat rumit, ritmis, dan luwes sebagai bahan sandang. Motif dalam alur yang sama namun berbeda-beda warna dan bentuknya menyimbolkan juga aneka perbedaan dalam masyarakat, namun ritmis dan harmonis penuh toleransi dalam kehidupan bersama.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("#### Referensi")
        st.markdown(
            '<div style="text-align: justify; font-size:100%"> <ul> <li>Badudu, J.S. dan Zain, M.Z. 1996. Kamus Umum Bahasa Indonesia. Pustaka Sinar Harapan. Jakarta.</li> <li>Gustami, S.P. 2007. Butir-Butir Mutiara Estetika Timur, Ide Dasar Penciptaan Karya Seni Kriya Indonesia. Prasista. Yogyakarta.</li> <li>Suyanto, S. E. 2010. Nirmana Elemen-Elemen Seni Rupa dan Desain. Jalasutra. Yogyakarta.  </li> </ul>  </div>',
            unsafe_allow_html=True)
    elif batik_sumatera == 'Sumatera Utara':
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Meskipun tekstil tenun adalah tradisi yang paling umum di Sumatera Utara, pengrajin lokal seperti di Medan Tembung memproduksi batik dengan motif lokal. Tekstil batik di wilayah tersebut sebagian besar menggambarkan motif tekstil tenun Ulos, seperti hari hara sundung, motif pani patunda dari suku Simalungun, motif Melayu seperti pucuk rebung, semut beriring, desa nawalu, dan gorga sitompi dari suku Toba, dan motif mataniari dari Batak Mandailing. </div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Georga Simeol-meol")
        _, mid_column_simeol, _ = st.columns([0.5, 7, 0.5])
        mid_column_simeol.image('aset/sumut/Georga Simeol Meol.png', use_column_width=True,
                                caption="Motif Batik Georga Simeol-meol")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Gorga Simeol-meol adalah motif yang terdiri dari sulur tanaman ini dianggap sebagai simbol sukacita, serta doa untuk kesehatan dan umur panjang. Motif ini juga melambangkan harapan mendapatkan banyak anak untuk mempertahankan keturunannya. Motif filler mencerminkan solidaritas, menepati janji, dan gotong royong untuk kepentingan bersama, yang merupakan kode etik masyarakat Batak. </div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Desa Na Ualu")
        _, mid_column_naualu, _ = st.columns([0.5, 7, 0.5])
        mid_column_naualu.image('aset/sumut/Desa Na Ualu.png', use_column_width=True,
                                 caption="Motif Batik Desa Na Ualu")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Motif Desa Na Ualu adalah simbol dari delapan arah mata angin. Motif dari desa Na Ualu digunakan sebagai bagian dari pengaturan almanak dalam tradisi Batak kuno untuk menentukan waktu yang tepat untuk menanam padi, menangkap ikan, mengadakan pesta, dll. Simbol ini juga berkaitan dengan kegiatan ritual kehidupan seseorang, serta menceritakan kekayaan keluarga. </div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Desa Na Tolu")
        _, mid_column_natolu, _ = st.columns([0.5, 7, 0.5])
        mid_column_natolu.image('aset/sumut/Desa Na Tolu.png', use_column_width=True,
                                caption="Motif Batik Desa Na Tolu")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Pola Desa Na Tolu melambangkan filosofi keberadaan dan harmoni Batak dalam masyarakat Batak. Ini adalah kode yang melambangkan aturan saling menghormati, serta kode etik hubungan dengan anggota keluarga, khususnya klan pasangan dan mertua seseorang. </div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Penari Melayu")
        _, mid_column_penmay, _ = st.columns([0.5, 7, 0.5])
        mid_column_penmay.image('aset/sumut/Penari Melayu.png', use_column_width=True,
                                caption="Motif Batik Penari Melayu")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Penari Melayu menggambarkan tarian tradisional etnis Melayu di Sumatera Utara. Motif ini juga mewakili hubungan yang harmonis dan saling menghormati antara suami dan istri dalam keluarga. Setiap gender menjunjung tinggi tanggung jawab mereka dalam masyarakat.  </div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Referensi ")
        st.markdown(
            '<div style="text-align: justify; font-size:100%"> <ul> <li> Mengenal Batik Medan / Sumatra Utara - JNJ Batik. (2022). Retrieved 12 November 2022, from http://www.jnjbatik.com/blog/mengenal-batik-medan-sumatra-utara/ </li> </ul>  </div>',
            unsafe_allow_html=True)
    elif batik_sumatera == 'Sumatera Selatan':
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Menurut sejarawan Sumatera Selatan, RM Ali Hanafiah, tradisi Batik pada awalnya dibawa oleh orang Jawa yang menetap di Palembang. Produsen lokal mempertahankan produksi tekstil Batik, bersama dengan Kain Tenun Songket, yang merupakan kain khas yang dikembangkan di Palembang. Saat ini, ada dua jenis teknik produksi batik yang dikembangkan di wilayah ini yaitu, teknik pewarnaan tahan lilin dan teknik tie-dye(Photo: Genpi)  </div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Lasem")
        _, mid_column_lasem, _ = st.columns([0.5, 7, 0.5])
        mid_column_lasem.image('aset/sumsel/Motif Lasem.jpg', use_column_width=True,
                                caption="Motif Batik Lasem")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Batik Lasem atau sering disebut Batik Laseman merupakan batik bergaya pesisiran yang kaya motif dan warna. Nuansa multikultur sangat terasa pada lembaran Batik Lasem. Kombinasi motif dan warna Batik Lasem yang terpengaruh desain budaya Tionghoa, Jawa, Lasem, Belanda, Champa, Hindu, Buddha serta Islam tampak berpadu demikian serasi, anggun dan memukau. Ciri khusus Batik Lasem yang tidak akan temui pada batik manapun adalah warna merahnya yang terkenal dengan nama warna abang getih pithik atau warna darah ayam. Warna ini terbuat dari akar mengkudu dan ditambah air Lasem yang kandungan mineralnya sangat khas. Warna ini bahkan tidak dapat dibuat di labolatorium. </div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Songket")
        _, mid_column_songket, _ = st.columns([0.5, 7, 0.5])
        mid_column_songket.image('aset/sumsel/Motif Songket.jpg', use_column_width=True,
                                caption="Motif Batik Songket")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Kain songket khas Palembang dibuat dengan menggunakan benang katun atau sutera yang ditenun dengan hiasan benang emas. Sebelum ditenun, benang dicelupkan terlebih dahulu ke dalam warna dasar baru dijemur hingga kering dan dipintal. Warna yang paling sering digunakan dalam kain songket Palembang adalah warna merah dan emas. </div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
    elif batik_sumatera == 'Sumatera Barat':
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Ada dua jenis peninggalan tekstil di Sumatera Barat, yaitu tekstil tenun Songket dan Batik Tanah Liek. Pada zaman kuno, Batik digunakan dalam acara-acara tradisional oleh tokoh masyarakat seperti Datuak (pemimpin laki-laki) dan Bundo Kanduang (pemimpin perempuan dalam adat Minangkabau). Saat ini dua warisan tekstil menjadi aturan berpakaian dalam fungsi sosial kasual dan formal. Motif batik di Sumatera Barat mencerminkan gaya hidup pedesaan dan kearifan lokal masyarakat agraris. </div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Tanah Liek")
        _, mid_column_liek, _ = st.columns([0.5, 7, 0.5])
        mid_column_liek.image('aset/sumbar/Tanah Liek.png', use_column_width=True,
                               caption="Motif Batik Tanah Liek")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Batik Tanah Liek juga dikenal sebagai batik tanah liat, yang merupakan kain batik khas yang berasal dari Minangkabau. Batik ini menggunakan tanah liat sebagai pewarna di samping tanaman jengkol, rambutan, dan gambir. Kain itu pertama direndam selama seminggu dengan tanah liat, kemudian dicat dengan pewarna alami lainnya setelah dicuci. Warna dasar batik ini tidak biasa, yaitu coklat gelap teduh, namun memancarkan aura keanggunan. </div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Rangkiang")
        _, mid_column_rangkiang, _ = st.columns([0.5, 7, 0.5])
        mid_column_rangkiang.image('aset/sumbar/Batik Rangkiang.jpg', use_column_width=True,
                                 caption="Motif Batik Rangkiang")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Kata “Rangkiang” mengacu pada lumbung padi dalam bahasa Minangkabau. Ini melambangkan beras sebagai sumber makanan pokok bagi masyarakat. Motif ini menyiratkan aset yang dikelola dengan baik dan kehidupan yang makmur, karena melambangkan beras sebagai sumber makanan pokok bagi masyarakat nusantara. </div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Keluak Daun Pakis")
        _, mid_column_pakis, _ = st.columns([0.5, 7, 0.5])
        mid_column_pakis.image('aset/sumbar/Daun Pakis.jpg', use_column_width=True,
                                 caption="Motif Batik Keluak Daun Pakis")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Kata “Keluak” adalah bahasa Minang yang berarti bengkok atau kusut. Motif Keluak Daun Pakis terinspirasi oleh tanaman pakis kusut yang umum dan mudah ditemukan di Indonesia, terutama di tepi sungai. Tanaman pakis mewakili sikap bijak dan tenang dalam menghadapi tantangan dalam hidup. Ini adalah simbol kesuburan dan kemakmuran bagi kehidupan seseorang. </div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
    elif batik_sumatera == 'Jambi':
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Batik adalah warisan tekstil yang pada zaman kuno hanya dapat dimiliki oleh keluarga kerajaan atau bangsawan di Jambi. Dengan berakhirnya pemerintahan Kesultanan Jambi, produksi batik tulis batik Jambi menurun secara dramatis. Sejak 1980, perkembangan batik Jambi meningkat pesat. Penggunaan batik Jambi tidak lagi terbatas pada kalangan sosial tertentu. Batik Jambi memiliki karakteristik yang unik dan eksotik, baik dari segi warna maupun coraknya sendiri. Jambi menerima pengaruh dari budaya Arab dan Cina selama era kekaisaran Jambi pada abad ke-16-17. Pengaruh-pengaruh itu dapat berupa variasi kaligrafi dan motif tekstil batik. Motif utama dalam Batik Jambi menggambarkan karakter asli komunitas Melayu Jambi, yang sangat sederhana, tidak rumit dan cenderung konvensional. Beberapa daerah penghasil batik di Jambi termasuk Kota Jambi, Batanghari, Soralangun, Merangin, Tebo, dan Bungo.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Kapal Sanggat")
        _, mid_column_kapal, _ = st.columns([0.5, 7, 0.5])
        mid_column_kapal.image('aset/jambi/1-kapal-sangat.png', use_column_width=True,
                              caption="Motif Batik Kapal Sanggat")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Bentuk kapal yang berbeda, kapal yang pertama mempunyai tiga bendera. Sedangkan kapal yang kedua memiliki empat bendera. Tiga bendera mempunyai arti mewakili masyarakat peladang dan empat bendera mewakili masyarakat maritim atau pesisir. </div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Duren Pecah")
        _, mid_column_duren, _ = st.columns([0.5, 7, 0.5])
        mid_column_duren.image('aset/jambi/2-duren-pecah.png', use_column_width=True,
                                   caption="Motif Batik Duren Pecah")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Duren yang di maksud adalah buah durian. Buah durian yang terbagi menjadi dua memiliki arti dua. Belahan yang pertama memiliki arti iman dan taqwa sedangkan belahan yang kedua memiliki arti ilmu pengetahuan dan teknologi. Dua kesatuan yang tidak dapat dihilangkan yaitu iman taqwa dan ilmu pengetahuan berjalan seimbang. Maysarakat jambi menjalankan hidupnya berdasarkan iman dan taqwa di dukung dengan penguasaan ilmu dan teknologi. </div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Kuao Berhias")
        _, mid_column_kuao, _ = st.columns([0.5, 7, 0.5])
        mid_column_kuao.image('aset/jambi/3-kuao-berhias.png', use_column_width=True,
                               caption="Motif Batik Kuao Berhias")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Motif kuao berhias adalah seekor burung yang sedang bercermin. Dasarnya burungnya hanya satu seolah-oleh burung tersebut berkaca sehingga menjadi dua. Motif ini memiliki makna cerminan diri sendiri sehingga masyarakat jambi bisa mengintropeksi diri sendiri. Sebagai manusia kita harus memperbaiki diri sendiri setiap saat. </div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
    elif batik_sumatera == 'Riau':
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Mayarakat Riau mulai membatik menggunakan canting seperti masyarakat di jawa. Teknik dan cara membatik pun sama seperti yang di ajarkan dari jawa namun yang membedakan adalah motifnya saja.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Tekat")
        _, mid_column_tekat, _ = st.columns([0.5, 7, 0.5])
        mid_column_tekat.image('aset/riau/Batik Tekat.png', use_column_width=True,
                              caption="Motif Batik Tekat")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Motif batik ini adalah batik simetris. Namun biasanya batik ini menggunakan Teknik cap bukan batik tulis. Akan sangat sudah jika motif batik ini menggunakan  Teknik tulis sehingga di ciptakannya cap agar mempermudah proses pembuatannya.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Nyiur Melambai")
        _, mid_column_nyiur, _ = st.columns([0.5, 7, 0.5])
        mid_column_nyiur.image('aset/riau/Nyiur Melambai.png', use_column_width=True,
                                   caption="Motif Nyiur Melambai")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Motif nyiur melambai adalah motif daun yang melambai. Nyiur melambai menggambarkan bintang setaman merupakan lambang kesucian dan kesuburan rejeki. Bisa di lihat pada gambar di atas pada ujung setiap pola terdapat garis tabir mengikuti pola. Pola tabir adalah asli motif dari daerah Riau.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Tapuk Manggis")
        _, mid_column_tapuk, _ = st.columns([0.5, 7, 0.5])
        mid_column_tapuk.image('aset/riau/Tapuk Manggis.png', use_column_width=True,
                               caption="Motif Batik Tapuk Manggis")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Motif tapuk manggis juga ada di daerah riau. Warna dasar motif ini biasanya hijau tua atau merah tua dengan motif putih di atasanya. Motif batik ini simetris sehingga ada juga motif ini menggunakan Teknik cap agar mempermudah produksinya.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
    elif batik_sumatera == 'Bengkulu':
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Batik bengkulu biasanya disebut dengan kain besurek. Asal usul batik Bengkulu berasal dari tanah jawa. Kalua di jawa kain batik sangat populer dari zaman dahulu. Para pedagang dan zaman jajahan dulu lah yang membawa kain batik hingga sampai ke Bengkulu. Namun masyarakat Bengkulu memodifikasi motif-motif sendiri yang sesuai dengan adat dan budaya mereka. Sehingga kain batik Bengkulu berkembang hingga saat ini di kota Bengkulu.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Kaganga")
        _, mid_column_kaganga, _ = st.columns([0.5, 7, 0.5])
        mid_column_kaganga.image('aset/bengkulu/kaganga.png', use_column_width=True,
                                 caption="Motif Kaganga")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Batik ini terinspirasi dari motif bentuk huruf-huruf Kaganga yang dikenal sebagai aksara suku Rejang, Bengkulu. Motif ini kemudian dimodifikasi dengan memadu motif bunga Rafflesia Arnoldi yang habitat alaminya banyak dijumpai di Tanah Rejang.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Berimis")
        _, mid_column_berimis, _ = st.columns([0.5, 7, 0.5])
        mid_column_berimis.image('aset/bengkulu/berimis.png', use_column_width=True,
                                 caption="Motif Berimis")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Batik motif ini bermotif kulit remis dan burung walet dan dipadukan dengan susunan motif batik besurek. Batik ini sangat ciri khas Bengkulu yang berasal dari daerah Seluma. Yang membuat khas batik ini adalah cara menulis murni bukan di cetak. Bahan yang digunakan juga bahan yang bagus misalnya kain sutra atau catton sehingga mempunyai jual tinggi dan tentu sangat nyaman.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Besurek")
        _, mid_column_besurek, _ = st.columns([0.5, 7, 0.5])
        mid_column_besurek.image('aset/bengkulu/Besurek.jpg', use_column_width=True,
                                 caption="Motif Besurek")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Umumnya batik besurek memiliki motif dasar berupa kaligrafi, rembulan, melati, burung kuau, pohon hayat, kombinasi cengkeh dan bunga cempaka, dan perpaduan relung paku dengan burung punai. Biasanya, warna besurek didominasi beragam jenis merah.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
    elif batik_sumatera == 'Bangka Belitung':
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Baik batik maupun tradisi tekstil tenun Cual dianggap sebagai warisan budaya takbenda penting Bangka dan Belitung. Motif dan pola warnanya mencerminkan kearifan lokal masyarakat. Motifnya sebagian besar merupakan ilustrasi motif bunga dan keindahan alam daerah tersebut. Misalnya, motif bunga dalam tekstil tenun Cual menandakan keanggunan dan kemurnian seorang wanita, sedangkan motif naga didedikasikan untuk pria karena melambangkan martabat, kejantanan, dan kekuatan.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Kain Cual")
        _, mid_column_cual, _ = st.columns([0.5, 7, 0.5])
        mid_column_cual.image('aset/bangbel/kain_cual.png', use_column_width=True,
                                 caption="Motif Kain Cual")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Tradisi tekstil cual telah ada sejak abad ke-17. Kata Cual mengacu pada tenunan tekstil, yang pertama kali ditemukan oleh komunitas Muntok di Bangka Barat. Motif Cual Batik diambil dari tumbuhan dan hewan. Saat ini, produsen menggabungkan tulisan tangan Batik dalam produksi tekstil Cual. Motif Kain Cual dengan motif bunga melambangkan kemurnian, keanggunan, dan harapan baik bagi pengguna.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Biji Kopi")
        _, mid_column_kopi, _ = st.columns([0.5, 7, 0.5])
        mid_column_kopi.image('aset/bangbel/biji_kopi.png', use_column_width=True,
                                 caption="Motif Biji Kopi")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Motif biji kopi adalah motif yang merujuk pada distrik kopi lokal di Kabupaten Manggar di pulau Belitung. Selain pusat perkebunan kopi, Belitung Timur dikenal karena tradisi pembuatan kopi yang mengakar. Para Wisatawan dianjurkan mencicipi segelas kopi Bangka yang dibuat dengan kopi pilihan dan diracik dengan istimewa.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Daun Simpor")
        _, mid_column_simpor, _ = st.columns([0.5, 7, 0.5])
        mid_column_simpor.image('aset/bangbel/daun_simpor.png', use_column_width=True,
                                 caption="Motif Daun Simpor")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Motif ini terinspirasi oleh tanaman Simpor (Dillenia Suffruticosa) yang merupakan tanaman khas Belitung. Daun Simpor biasanya digunakan untuk membungkus makanan karena memiliki aroma yang khas. Tanaman Simpor melambangkan kebijaksanaan dan cinta universal. Perbedaan bentuk tanaman Simpor yang berbeda menandakan regenerasi kehidupan, keharmonisan, dan saling menghormati antara yang muda dan yang tua.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
    elif batik_sumatera == 'Lampung':
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Menurut sejarawan Sumatera, RM Ali Hanafiah, tradisi Batik pada awalnya dibawa oleh orang Jawa yang menetap di Lampung. Produsen lokal mempertahankan produksi tekstil Batik, bersama dengan kain tenun Tapis, yang merupakan kain khas yang dikembangkan di Lampung. Selain motif Pohon Kehidupan, salah satu motif batik paling terkenal di Lampung adalah Mahkota Siger. Mahkota Siger adalah simbol wanita bangsawan di Lampung pada zaman kuno. Motif mahkota juga mewujudkan motif Pohon Kehidupan dan mewakili kekuatan, kelembutan, dan keindahan seorang wanita sebagai tokoh penting dalam keluarga.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Mahkota Siger")
        _, mid_column_siger, _ = st.columns([0.5, 7, 0.5])
        mid_column_siger.image('aset/lampung/mahkota_siger.png', use_column_width=True,
                                 caption="Motif Mahkota Siger")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Siger adalah nama mahkota bagi wanita bangsawan Lampung di zaman kuno. Motif ini adalah simbol feminitas, kekuatan, dan keanggunan seorang wanita. Bagi masyarakat Lampung, perempuan sangat terlibat dalam semua kegiatan, terutama dalam kegiatan rumah tangga. Di belakang kelembutan wanita, ada kerja keras, kemandirian, kegigihan, dan kualitas feminin. Meskipun masyarakat Lampung sendiri mengikuti pola garis patrilineal atau bapak, sosok perempuan itu penting, baik sebagai inspirasi bagi anak-anak maupun pendorong kesuksesan hidup pasangan mereka.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Pohon Hayat")
        _, mid_column_hayat, _ = st.columns([0.5, 7, 0.5])
        mid_column_hayat.image('aset/lampung/pohon_hayat.png', use_column_width=True,
                                 caption="Motif Pohon Hayat")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Motif batik di Lampung didominasi oleh akulturasi budaya Buddha dan Islam, misalnya, Motif Hayat atau juga dikenal sebagai Pohon Kehidupan. Motif pohon kehidupan memiliki makna filosofis yang mendalam bagi masyarakat Lampung. Pohon kehidupan menandakan Pohon Surga, kekuatan abadi, maskulinitas, dan simbol kehidupan. Motif ini biasanya dipakai sebagai sarung untuk wanita.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Gajah Way Kambas")
        _, mid_column_wayk, _ = st.columns([0.5, 7, 0.5])
        mid_column_wayk.image('aset/lampung/way_kambas.png', use_column_width=True,
                                 caption="Motif Gajah Way Kambas")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Motifnya menggambarkan cagar alam Lampung, Way Kambas. Way Kambas adalah cagar alam yang dilindungi yang berfungsi sebagai pusat konservasi gajah. Untuk komunitas Hindu, gajah melambangkan Airlangga, yang merupakan dewa kebijaksanaan dan pengetahuan.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)

elif jenis_info == 'Batik Jawa':
    st.header('Yuk Berkenalan dengan Jenis-Jenis Batik di Pulau Jawa!')
    st.markdown('<hr>', unsafe_allow_html=True)
    batik_jawa = st.selectbox(
        'Pilih jenis daerah',
        ('DKI Jakarta',
         'Banten',
         'DIY Yogyakarta',
         'Jawa Barat',
         'Jawa Tengah',
         'Jawa Timur'))

    if batik_jawa == "DIY Yogyakarta":
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Sebagai daerah yang masih sangat kental akan kebudayaan Keratonnya, Yogyakarta memiliki kekhasan sendiri atas ragam batiknya. Penggunaan warna beserta motifnya sangat mewakili khas budaya Jawa yang anggun dan kalem.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Ceplok")
        _, mid_column_ceplok, _ = st.columns([0.5, 7, 0.5])
        mid_column_ceplok.image('aset/diy/cepok.jpg', use_column_width=True,
                                caption="Motif Ceplok")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Motif ceplok biasanya terdiri dari bentuk bunga mawar yang melingkar sebagai dasar. Disertai bintang ataupun bentuk kecil lainnya sehingga membentuk pola yang simetris secara keseluruhan. Motif ini juga disebut sebagai motif grompol yang berasal dari bahasa Jawa dan memiliki arti berkumpul atau bersatu. Motif ceplok atau grompol memiliki makna harapan orang tua terhadap berkumpulnya. Ini berkaitan dengan semua hal baik, seperti rezeki, kerukunan hidup, kebahagiaan, serta ketentraman untuk kedua mempelai dan keluarga pengantin. Warna coklat dipilih sebagai simbol dari warna tanah lempung yang subur sehingga diharapkan dapat membangkitkan rasa kebahagiaan, kerendahan hati, kesederhanaan dan sifat “membumi”.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Parang")
        _, mid_column_parang, _ = st.columns([0.5, 7, 0.5])
        mid_column_parang.image('aset/diy/Parang.jpg', use_column_width=True,
                                caption="Motif Parang")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Motif parang memiliki pola berupa garis-garis tegas yang disusun secara diagonal paralel. Garis-garis dalam motif parang diartikan sebagai ombak lautan yang menjadi pusat tenaga alam. Dalam hal ini, yang dimaksudkan adalah raja. Komposisi kemiringan pada motif parang juga melambangkan kewibawaan, kekuasaan, dan kebesaran. Serta bermakna gerak cepat sehingga pemakainya diharapkan dapat bergerak cepat.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Sido Mulyo")
        _, mid_column_sido, _ = st.columns([0.5, 7, 0.5])
        mid_column_sido.image('aset/diy/sidomulyo.png', use_column_width=True,
                              caption="Motif Sido Mulyo")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Sido Mulyo merupakan salah satu motif klasik yang khusus dipergunakan untuk pakaian pernikahan mempelai wanita dalam pernikahan keturunan raja dan bangsawan di Jawa.  Motif ini melambangkan harapan baik agar penggunanya mendapatkan kemuliaan, keluarga yang harmonis, dan status social yang dihormati.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
    elif batik_jawa == "DKI Jakarta":
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Batik Jakarta pertama kali dikenal dan dikembangkan bersama batik di daerah-daerah lain pada sekitar akhir abad ke-19, ketika batik dibawa perantau dari Jawa Tengah. Ciri khas batik daerah ini yaitu berwarna mencolok dan berbau kebudayaan Tionghoa.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Nusa Kelapa")
        _, mid_column_nusa, _ = st.columns([0.5, 7, 0.5])
        mid_column_nusa.image('aset/dki/Nusa Kelapa.jpg', use_column_width=True,
                              caption="Motif Nusa Kelapa")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Motif ini juga mengandung nilai sejarah karena menggambarkan Jakarta pada masa lalu sebagai daerah yang asri, dengan adanya pepohonan dan persawahan. Namun, akhirnya berubah menjadi kota besar dengan penduduk dan bangunan yang padat.  Sementara itu, nama motifnya diambil dari Peta Ceila yang dibuat pada 1482 hingga 1521 Masehi. Berdasarkan peta tersebut, diketahui bahwa nama asli Jakarta adalah Nusa Kelapa.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Rasamala")
        _, mid_column_rasamala, _ = st.columns([0.5, 7, 0.5])
        mid_column_rasamala.image('aset/dki/Rasamala.jpg', use_column_width=True,
                                  caption="Motif Rasamala")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Motif batik rasamala dikaitkan dengan masa ketika Belanda pertama kali mendarat di daerah Sunda Kelapa pada abad ke-16. Saat itu, Sunda Kelapa merupakan daerah hutan rawa liar yang ditutupi pohon rasamala. Orang Betawi menganggap pohon rasamala sebagai pohon yang keramat karena wanginya yang indah.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Ondel-Ondel Pucuk Rebung")
        _, mid_column_ondel, _ = st.columns([0.5, 7, 0.5])
        mid_column_ondel.image('aset/dki/Ondel ondel.jpeg', use_column_width=True,
                               caption="Motif Ondel-Ondel Pucuk Rebung")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Motif ondel-ondel pucuk rebung mengandung makna masyarakat Betawi yang dinilai jujur dan apa adanya.  Warna yang dipilih untuk membuat motif ini umumnya hijau dan biru, lalu gambar ondel-ondel akan ada di bagian tengah kain.  Sementara itu, gambar pucuk rebung akan diletakkan di bagian tepi kain, mengelilingi ondel-ondel.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
    elif batik_jawa == "Banten":
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Menurut Ir. Uke Kurniawan, seorang tokoh setempat di balik kebangkitan kembali Batik di Banten, falsafah motif batik Banten terkait dengan sejarah Kesultanan Banten. Sebagian besar motif yang ada berasal dari nama desa kuno, gelar kebangsawanan dan kerajaan di Kesultanan, serta nama aula yang terdapat pada Istana Kerajaan Banten. Batik Banten cenderung menggunakan kombinasi warna - warna pastel lembut.Warna - warna ini menggambarkan sifat rakyat Banten: halus dan lembut, tetapi berkemauan keras dan teguh memegang prinsip.Hanya motif batik etnis Baduy saja yang menggunakan kombinasi biru dan hitam yang gelap.< / div > ', unsafe_allow_html = True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Merak Srimanganti")
        _, mid_column_merak_srimanganti, _ = st.columns([0.5, 7, 0.5])
        mid_column_merak_srimanganti.image('aset/Banten/Srimanganti.png', use_column_width=True,
                                           caption="Motif Merak Srimanganti")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Nama motif Srimanganti berasal dari nama aula Istana yang bersambungan dengan gerbang, tempat tamu kerajaan menunggu sang Sultan siap menyambut mereka. Kata ‘sri’ berarti ‘raja’, sedangkan ‘manganti’ berarti ‘menanti’. Motif ini melambangkan kesempatan besar yang ada di depan nanti, yang merupakan jalan menuju masa depan yang gemilang.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Singayaksa")
        _, mid_column_singayaksa, _ = st.columns([0.5, 7, 0.5])
        mid_column_singayaksa.image('aset/Banten/Singayaksa.png', use_column_width=True,
                                    caption="Motif Singayaksa")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Motif Singayaksa berasal dari nama tempat Sultan Hasanuddin berdoa kepada Allah agar memberinya petunjuk mengenai tempat terbaik baginya untuk mendirikan istananya. Motif ini melambangkan harapan untuk mendapatkan petunjuk dari Ilahi dalam hidup, sehingga dapat mengambil keputusan dengan baik dan benar.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Tangerang Herang")
        _, mid_column_tangerang_herang, _ = st.columns([0.5, 7, 0.5])
        mid_column_tangerang_herang.image('aset/Banten/Tangerang Herang.png', use_column_width=True,
                                          caption="Motif Tangerang Herang")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Motif Tangerang Herang merupakan perlambangan kota Tangerang. Ia merupakan gabungan dari beberapa motif, yakni Gedung paviliun, sepuluh pintu, perahu, dan bunga melati. Gedung paviliun melambangkan Gedung pemerintah pusat kota Tangerang, sedangkan kesepuluh pintu melambangkan Sepuluh Pintu Air Tangerang. Perahu melambangkan Perahu Naga, yang merupakan salah satu jenis olahraga yang dilakukan di Sungai Cisadane. Bunga melati memperingati kepahlawanan Nyi Mas Melati, pahlawan wanita setempat yang berjuang melawan penjajah Belanda pada abad ke-19.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
    elif batik_jawa == "Jawa Barat":
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Jawa Barat memiliki warisan budaya yaitu batik yang sangat memukau dan memesona. Motif batik Jawa Barat memiliki karakter dan ciri khas tersendiri yaitu didominasi oleh motif flora dan fauna dengan warna yang lebih cerah dan beragam. Motif batik Jawa Barat sangat dipengaruhi oleh budaya dan keadaan alam dari daerah batik tersebut berasal.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Megamendung")
        _, mid_column_mega, _ = st.columns([0.5, 7, 0.5])
        mid_column_mega.image('aset/jabar/megamendung.jpg', use_column_width=True,
                              caption="Motif Megamendung")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Ide motif tersebut berasal dari penggambaran awan di langit bernuansa biru yang memiliki kesan cerah, dan hitam yang melambangkan mendung. Pola tersebut rupanya disukai masyarakat baik dalam maupun luar negeri. Menurut sejarah, konon batik megamendung ditemukan ketika seseorang melihat bentuk awan pada genangan air setelah hujan dan pada saat itu cuaca sedang mendung. Namun ada teori lain menyebutkan bahwa motif ini terbentuk karena pengaruh adanya bangsa Cina yang masuk ke Cirebon.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Ganasan")
        _, mid_column_ganasan, _ = st.columns([0.5, 7, 0.5])
        mid_column_ganasan.image('aset/jabar/ganasan.jpg', use_column_width=True,
                                 caption="Motif Ganasan")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Batik tersebut dinamai Batik Ganasan yang terinspirasi dari ikon kota Subang, yaitu buah nanas. Batik Ganasan bukan hanya merupakan kekayaan seni yang memiliki keindahan, tetapi di dalamnya terkandung nilai-nilai luhur dan filosofi. Nanas merupakan buah tunggal pada pohon yang memiliki banyak cabang, diartikan bahwa meskipun terdapat perbedaan dari segi bahasa budaya, agama, dan geografis di Kabupaten Subang, tapi tetap mempunyai satu tujuan yang sama. Batik ni dibuat dengan beragam macam warna. Tak heran bila peminatnya sampai ke mancanegara.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Kujang Kijang")
        _, mid_column_kujang, _ = st.columns([0.5, 7, 0.5])
        mid_column_kujang.image('aset/jabar/kujang.png', use_column_width=True,
                                caption="Motif Kujang Kijang")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Motif kujang terinspirasi dari senjata tradisional Jawa Barat, sedangkan kijang melambangkan ciri khas Kota Bogor atau Kerajaan Pakuan. Menjulang tinggi yang mencerminkan cita-cita. Batik ini sangat popular dan banyak jenisnya. Motif ini dapat di gunakan untuk pakaian batik sekolah, dinas, kampus, upacara pernikahan, upacara adat. Sehingga masyarakat bogor wajib mempunyai batik dengan motif ini.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
    elif batik_jawa == "Jawa Tengah":
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Banyak daerah di Jawa Tengah yang memiliki batik dengan ciri khas nya masing-masing. Dari  barat hingga timur  Jawa Tengah, semuanya memiliki pola yang unik. Pola ini menunjukkan bahwa karena apa yang digambarkan merupakan ciri khas  masing-masing daerah.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Kawung")
        _, mid_column_kawung, _ = st.columns([0.5, 7, 0.5])
        mid_column_kawung.image('aset/jateng/kawung.jpg', use_column_width=True,
                                caption="Motif Kawung")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Kawung juga termasuk desain yang sangat tua, terdiri dari lingkaran yang saling berinterseksi. Lingkaran-lingkaran, terkadang diisi dengan dua atau lebih tanda silang atau ornamen lain seperti garis-garis berpotongan atau titik-titik. Dalam pewarnaan batik kawung tidak terbatas pada tiga warna (coklat, putih dan hitam atau biru) tetapi didasarkan pada bentuk filosofisnya.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Asam Arang")
        _, mid_column_asam, _ = st.columns([0.5, 7, 0.5])
        mid_column_asam.image('aset/jateng/asam.jpg', use_column_width=True,
                              caption="Motif Asam Arang")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Semarang juga cukup dikenal dengan kekayaan alamnya. Salah satunya pohon asam. Motif batik Semarang kali ini yakni mengusung konsep asam arang. Asam di sini mengacu pada habitat pohon asam, serta asam dalam bahasa Jawa artinya jarang. Sehingga, filosofi batik ini merujuk pada pohon asam yang tumbuh saling berjauhan. Dengan mengenakan motif ini, kebaikan dan manfaat akan mengalir pada si pemakainya.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Lawang Sewu")
        _, mid_column_lawang, _ = st.columns([0.5, 7, 0.5])
        mid_column_lawang.image('aset/jateng/lawang.jpg', use_column_width=True,
                                caption="Motif Lawang Sewu")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Dikenal juga dengan sebutan batik Lawang Sewu Kekiteran Asem, ini merupakan motif varian dari Tugumuda Kekiteran Sulur. Pada motif ini, menunjukkan bangunan Lawang Sewu sebagai tempat bersejarah di Kota Semarang sejak dahulu kala. Arti dari motif batik ini melambangkan semangat pelestarian warisan budaya dan juga pelestarian lingkungan.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
    elif batik_jawa == "Jawa Timur":
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Jenis batik khas Jawa Timur memiliki keragaman motif yang dipengaruhi oleh budaya asing seperti Tionghoa, Jepang, dan India. Jenis batik khas Jawa Timur lebih kaya akan nuansa alam seperti bunga, laut, bambu, hingga binatang.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Mata")
        _, mid_column_mata, _ = st.columns([0.5, 7, 0.5])
        mid_column_mata.image('aset/jatim/Motif mata.jpg', use_column_width=True,
                              caption="Motif Mata")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Merupakan salah satu batik asli Madura. mengapa diberi nama motif mata? Hal tersebut dikarenakan, mata burung perkutut sebagai objek utamanya. Batik ini memiliki warna dominan, yaitu kuning, hijau, dan merah muda.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Sekar Jati")
        _, mid_column_jati, _ = st.columns([0.5, 7, 0.5])
        mid_column_jati.image('aset/jatim/sekar jati.png', use_column_width=True,
                              caption="Motif Sekar Jati")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Kata “Sekarjati” merupakan gabungan dari kata “sekar” (“bunga”) dan “jati”. Pohon jati merupakan aset ekonomi yang penting bagi masyarakat Bojonegoro. Motif ini melambangkan harapan agar penggunanya memiliki sifat yang tegar seperti jati, dan membawa pengaruh baik ke masyarakat seperti bunga.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Samudra")
        _, mid_column_samudra, _ = st.columns([0.5, 7, 0.5])
        mid_column_samudra.image('aset/jatim/Samudra.png', use_column_width=True,
                                 caption="Motif Samudra")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Ada pula tema yang dapat digariskan pada tekstil dengan menggunakan teknik batik. Motif batik ini menggambarkan kuatnya tekad seseorang yang berlayar agar dapat mengejar tujuan hidupnya. Lukisan ini juga menggambarkan doa dan harapan agar seseorang yang merantau dapat menjemput keberhasilan.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)

elif jenis_info == 'Batik Kalimantan':
    st.header('Yuk Berkenalan dengan Jenis-Jenis Batik di Pulau Kalimantan!')
    st.markdown('<hr>', unsafe_allow_html=True)
    batik_kalimantan = st.selectbox(
        'Pilih jenis daerah',
        ('Kalimantan Barat',
         'Kalimantan Tengah',
         'Kalimantan Selatan',
         'Kalimantan Timur',
         'Kalimantan Utara'))

    if batik_kalimantan == 'Kalimantan Barat':
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Batik Kalimantan Barat mewakili kehidupan masyarakat multi kultural di daerah tersebut. Motif batik yang ada mewakili identitas masing-masing suku, yang terutama didominasi budaya Tidayu, yakni gabungan warisan budaya Tionghoa (Cina), Dayak, dan Melayu. Hal ini ikut mengakibatkan munculnya kesan kosmopolitan pada batik Kalimantan Barat, yang seringkali menggambarkan harmoni antara alam dan manusia dalam kegiatan sehari-hari. Batik motif awan, misalnya, dikatakan terinspirasi oleh ornamentasi Melayu di daerah ini.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Dayak Kamang")
        _, mid_column_dayang, _ = st.columns([0.5, 7, 0.5])
        mid_column_dayang.image('aset/kalbar/dayak_kamang.png', use_column_width=True,
                               caption="Motif Batik Dayak Kamang")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Motif Kamang pada umumnya ditemukan pada perisai suku Dayak, karena diyakini akan meningkat­kan daya magis dan semangat orang yang menggunakannya. Kamang adalah ruh leluhur pria, seringkali digambarkan hanya mengenakan cawat dan duduk bersila. </div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Insang Ikan")
        _, mid_column_insang, _ = st.columns([0.5, 7, 0.5])
        mid_column_insang.image('aset/kalbar/insang_ikan.png', use_column_width=True,
                               caption="Motif Batik Insang Ikan")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Insang ikan merupakan motif yang sering dipergunakan oleh kaum Melayu yang tinggal di sepanjang tepian Sungai Kapuas. Ia melambangkan rasa syukur manusia kepada Tuhan. Insang merupakan bagian tubuh ikan yang paling penting, yang memungkinkan ikan untuk bernapas dan hidup. </div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Awan Berarak")
        _, mid_column_awan, _ = st.columns([0.5, 7, 0.5])
        mid_column_awan.image('aset/kalbar/awan_berarak.png', use_column_width=True,
                               caption="Motif Batik Awan Berarak")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Awan Berarak merupakan kombinasi motif Dayak dengan Melayu. Motif ini menggambarkan seseorang yang sopan santun dan lembut, khas sifat orang Melayu. Sebagai gambaran dari anggunnya awan yang berarak di langit, ia juga menggambarkan tingginya kedudukan keluarga kerajaan yang mendukung dan melindungi rakyat. Motif ini khusus untuk dipergunakan keluarga penguasa Kerajaan Amantubilah Mempawah di Pontianak. </div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
    elif batik_kalimantan == 'Kalimantan Tengah':
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Lahirnya batik Kalimantan Tengah merupakan kiprah dari istri Gubernur Suparmanto, Gubernur Kalimantan Tengah masa jabatan 1989-1993. Batik Kalimantan Tengah diciptakan dengan menggabungkan karya dua budaya, yakni teknik batik dari Jawa dengan motif Dayak (Ngaju) dari Kalimantan Tengah. Batik ini kemudian dikenal sebagai batik Benang Bintik. Batik merupakan salah satu oleh-oleh khas Kalimantan Tengah. Kain ini juga sering digunakan dalam perayaan budaya Dayak sebagai pengingat akan nenek moyang suku Dayak dan kearifan lokal mereka.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Anggrek Tewu")
        _, mid_column_anggrek, _ = st.columns([0.5, 7, 0.5])
        mid_column_anggrek.image('aset/kalteng/anggrek_tewu.png', use_column_width=True,
                                caption="Motif Batik Anggrek Tewu")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Motif ini dibuat berdasarkan kearifan lokal dan falsafah di balik bunga Anggrek Tewu (“Anggrek Tebu”). Rakyat Kotawaringin Timur ingin meneladani gaya hidup anggrek tebu: Bunga ini terus bertumbuh dengan menempelkan diri pada pohon tanpa membunuh induk semangnya, melambangkan harmoni sosial masyarakat yang hidup bersama dan saling bermanfaat satu sama lain, tanpa saling menyakiti. Bunga ini melambangkah harapan Kotawaringin Timur untuk menjadi wilayah yang berkembang paling baik di Kalimantan Tengah. </div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Enggang Dayak")
        _, mid_column_enggang, _ = st.columns([0.5, 7, 0.5])
        mid_column_enggang.image('aset/kalteng/enggang_dayak.png', use_column_width=True,
                                caption="Motif Batik Enggang Dayak")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Motif Burung enggang melambangkan kedekatan masyarakat Dayak Indonesia dengan alam. Segala bagian tubuh burung enggang melambangkan kehebatan dan keagungan suku ini, sedangkan burung itu sendiri melambangkan perdamaian dan persatuan: Sayapnya yang kokoh melambangkan pemimpin yang selalu melindungi rakyatnya, sedangkan ekornya yang panjang dianggap sebagai tanda kemakmuran suku Dayak. Selain itu, burung enggang juga digunakan sebagai teladan kehidupan berkeluarga dan bermasyarakat. Ia melambangkan kasih tanpa syarat terhadap pasangan dan pendidikan anak sehingga menjadi manusia yang matang dan mandiri. </div>',
            unsafe_allow_html=True)
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Sangat perlu ditekankan bahwa suku Dayak Kalimantan sangat dekat dengan burung enggang. Burung ini selalu tampil dalam berbagai mitos dan kisah rakyat Dayak yang berbeda di semua daerah di pulau ini. Diantaranya, rakyat setempat meyakini bahwa burung enggang merupakan Panglima para Burung. Ia dianggap memiliki kekuatan supernatural dan hanya akan muncul di masa perang. Secara umum, burung ini dianggap sakral dan orang dilarang memburu, apalagi memakannya. </div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Kaharingan")
        _, mid_column_khringan, _ = st.columns([0.5, 7, 0.5])
        mid_column_khringan.image('aset/kalteng/kaharingan.png', use_column_width=True,
                              caption="Motif Batik Kaharingan")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Motif ini mewakili Kaharingan, yang merupakan nama lain “Pohon Kehidupan” dalam sistem keyakinan suku Dayak. Batang pohon ini melambangkan hubungan vertikal antara manusia dan Tuhan yang diyakini¬nya, sedangkan dahan dan daunnya melambangkan hubungan horizontal antar manusia serta antara manusia dengan makhluk-makhluk lain di bumi. </div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
    elif batik_kalimantan == 'Kalimantan Selatan':
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Kain batik tradisional dari suku Banjar di Kalimantan Selatan disebut “Sasirangan”. Kain ini diyakini dapat menyembuhkan penyakit jika dikenakan. Warna kain yang diberikan pada pasien untuk dikenakan berbeda tergantung pengobatan yang ingin dilakukan. Misalnya, warna kuning digunakan untuk menyembuhkan penyakit kuning, merah untuk mengobati sakit kepala atau insomnia, hijau untuk lumpuh atau stroke; hitam untuk demam dan gatal-gatal, ungu berguna untuk menyembuhkan sakit perut, sedangkan cokelat menyembuhkan penyakit mental atau stress.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Gigi Haruan Lidi")
        _, mid_column_gigi, _ = st.columns([0.5, 7, 0.5])
        mid_column_gigi.image('aset/kalsel/gigi_haruan_lidi.png', use_column_width=True,
                                 caption="Motif Batik Gigi Haruan Lidi")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Motif Gigi Haruan Lidi diambil dari nama ikan Haruan atau ikan gabus dan ular Lidi. Baik Haruan maupun Lidi memiliki gigi tajam, dan gigi ini merupakan simbol ketajaman pikiran. Selain itu, menurut hikayat Banjar, baik ular Lidi maupun ikan Haruan merupakan hewan yang cerdas dan pemberani, karena mereka tahu caranya mengeluarkan diri dari kesulitan di alam dan tidak menyerah ketika diburu hingga akhir hayatnya. Kaum Banjar menghormati mereka karena kelicikannya, karena mereka sangat sulit disudutkan dan ditangkap. Falsafah dibalik motif ini adalah bahwa manusia harus cerdas dan dapat membaca situasi, dan tetap berani hingga akhir. </div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Tampuk Manggis")
        _, mid_column_tamgis, _ = st.columns([0.5, 7, 0.5])
        mid_column_tamgis.image('aset/kalsel/tampuk_manggis.png', use_column_width=True,
                                 caption="Motif Batik Tampuk Manggis")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Motif Sasirangan Tampuk Manggis menggambarkan falsafah buah manggis, yang merupakan simbol kesetaraan dan kejujuran. Buah manggis menggambarkan dengan jelas berapa jumlah daging buah yang dimilikinya dari jumlah “kelopak” di kulit bagian bawahnya, dan ketika matang, daging buah tersebut semua sama ukurannya. Motif ini menyiratkan bahwa manusia harus mengembangkan sifat jujur dan tulus, menyamakan perilaku luarnya dengan pikiran dalamnya. </div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Bayam Raja")
        _, mid_column_bayam, _ = st.columns([0.5, 7, 0.5])
        mid_column_bayam.image('aset/kalsel/bayam_raja.png', use_column_width=True,
                                  caption="Motif Batik Bayam Raja")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Motif Sasirangan Raja Bayam menggambarkan status sosial penggunanya dan melambangkan kewibawaan para leluhur. Rancangan motif ini berupa garis vertikal berlekuk yang memisahkan satu motif dari lainnya. </div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
    elif batik_kalimantan == 'Kalimantan Timur':
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Batik Kalimantan Timur seringkali menggunakan berbagai gradasi warna jingga, hijau, merah jambu, dan merah. Motif-motifnya terutama terpengaruh oleh budaya Dayak, menggambarkan pandangan dan falsafah mereka mengenai alam dan dunia sekitarnya. Misalnya, motif Batang Garing. Motif ini merupakan penggambaran visual batang pohon, yang berbentuk kerucut atau mirip kepala tombak. Menurut masyarakat Dayak, motif ini menggambarkan Dewa Ranying Mahatala Langit, pencipta segala makhluk hidup. Ia juga menggambarkan harmoni antara alam dengan manusia, antar-manusia, dan antara manusia dengan Tuhan.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Rutun Penyu")
        _, mid_column_rutun, _ = st.columns([0.5, 7, 0.5])
        mid_column_rutun.image('aset/kaltim/rutun_penyu.png', use_column_width=True,
                              caption="Motif Batik Rutun Penyu")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Motif ini melambangkan kesederhanaan dan kerendahan hati. Menjalani hidup haruslah selaras dengan aliran alam semesta. Hidup akan menjadi lebih mudah jika kita tetap bersikap sewajarnya dan alami sesuai perintah Tuhan, dan mengambil langkah untuk mengikuti ketentuan tersebut. </div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Tengkawang Ampiek")
        _, mid_column_ampiek, _ = st.columns([0.5, 7, 0.5])
        mid_column_ampiek.image('aset/kaltim/tengkawang_ampiek.png', use_column_width=True,
                                caption="Motif Batik Tengkawang Ampiek")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Motif ini menggambarkan ukiran kayu, yang disebut “ampiek” dalam bahasa Kutai. “Tengkawang” adalah pohon sejenis meranti merah (Dipterocarpaceae). Tanaman ini memiliki banyak manfaat bagi kesehatan, dan biasanya dipakai sebagai bahan makanan, kosmetika, maupun obat-obatan. Dengan banyaknya manfaat yang dihasilkannya, kaum Dayak juga banyak menggunakan daun pohon ini dalam upacara dan ritual mereka. Tanaman ini merupakan lambang kesuburan dan kebaikan alam semesta, yang merupakan aspek terpenting bagi suku Dayak. </div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Kuntul Perak")
        _, mid_column_perak, _ = st.columns([0.5, 7, 0.5])
        mid_column_perak.image('aset/kaltim/kuntul_perak.png', use_column_width=True,
                               caption="Motif Batik Kuntul Perak")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Kuntul perak (Egretta intermedia) merupakan hewan asli Kalimantan dan merupakan lambang dari kota Bontang. Motif ini menghargai keindahan burung kuntul, dan melambangkan rakyat Bontang yang pekerja keras, ramah, ceria, dan berpikiran terbuka seperti halnya burung perlambang jiwa mereka ini. </div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
    elif batik_kalimantan == 'Kalimantan Utara':
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Kalimantan Utara dikenal karena kain tenunannya.  Tetapi, tradisi batik baru-baru ini dikembangkan oleh pengrajin setempat.  Rancangan yang ada diadaptasi dari hiasan dan tradisi budaya suku Dayak.  Motif-motif ini menggambarkan pelajaran hidup, nilai falsafah, dan kearifan lokal yang ada.  Batik Tarakan pada umumnya dibuat dengan menggunakan bahan dan warna alami, dan sangat ramah lingkungan. </div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Bunga Raye")
        _, mid_column_raye, _ = st.columns([0.5, 7, 0.5])
        mid_column_raye.image('aset/kalut/bunga_raye.png', use_column_width=True,
                               caption="Motif Batik Bunga Raye")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Motif Bunga Raye melambangkan kesatuan antara suku Dayak Tidung dengan suku Bulungan, sehingga bermakna persatuan di balik perbedaan. Motif ini juga menggambarkan harapan akan keselamatan dan kesembuhan dari segala penyakit. </div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Bultiya")
        _, mid_column_bultiya, _ = st.columns([0.5, 7, 0.5])
        mid_column_bultiya.image('aset/kalut/bultiya.png', use_column_width=True,
                                caption="Motif Batik Bultiya")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Kata “Bultiya” merupakan singkatan nama tiga suku besar di Kalimantan Utara, yakni suku Bulungan, Tidung, dan Dayak. Motif ini diciptakan oleh Ridwansyah, seorang pengrajin batik dari Kabupaten Bulungan. Ia menciptakan motif ini untuk menghargai dan membantu memperkuat hubungan serasi antar suku di Kabupaten Bulungan, Kalimantan Utara. </div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Dayak Taghol")
        _, mid_column_taghol, _ = st.columns([0.5, 7, 0.5])
        mid_column_taghol.image('aset/kalut/dayak_taghol.png', use_column_width=True,
                               caption="Motif Batik Dayak Taghol")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Motif Dayak Taghol merupakan pola khas berupa empat garis lengkung dan titik-titik.  Motif ini melambangkan perisai, yang merupakan simbol daya tahan dan keutuhan di masyarakat. </div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)

elif jenis_info == 'Batik Sulawesi':
    st.header('Yuk Berkenalan dengan Jenis-Jenis Batik di Pulau Sulawesi!')
    st.markdown('<hr>', unsafe_allow_html=True)
    batik_sulawesi = st.selectbox(
        'Pilih jenis daerah',
        ('Sulawesi Utara',
         'Sulawesi Selatan',
         'Sulawesi Tengah',
         'Sulawesi Tenggara',
         'Sulawesi Barat',
         'Gorontalo'))
    if batik_sulawesi == 'Sulawesi Barat':
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Batik Sulawesi Barat menggambarkan kehidupan maritim lokal. Masyarakat Mandar pada umumnya bekerja di sektor kelautan, yaitu perikanan dan pengolahan; dan pengangkutan hasil pertanian melalui laut. Kehidupan maritim digambarkan oleh berbagai motif batik, seperti motif ikan arwana dan motif insang.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Perahu Sandeq")
        _, mid_column_sandeq, _ = st.columns([0.5, 7, 0.5])
        mid_column_sandeq.image('aset/sulbar/sandeq.png', use_column_width=True,
                                caption="Motif Perahu Sandeq")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Perahu Sandeq adalah simbol kekuatan bahari di wilayah Sulawesi Barat. Kehebatan para pelaut Mandar dibuktikan dengan pembangunan kapal legendarisnya. Sandeq mampu menahan gelombang besar dan oleh karenanya, Sandeq dianggap sebagai mahakarya pembuatan kapal di zaman kuno. Nenek moyang Mandar menggunakan perahu untuk berlayar melintasi benua di Asia dan Afrika.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Mandar Batik")
        _, mid_column_mandar, _ = st.columns([0.5, 7, 0.5])
        mid_column_mandar.image('aset/sulbar/Mandar.png', use_column_width=True,
                                caption="Motif Mandar Batik")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Mandar Batik menggambarkan rumah Raja Mamuju dengan karakteristik utama tangga di sebelah kiri bangunan rumah kayu. Motif mungkin memiliki kombinasi yang bervariasi seperti dengan perahu Sandeq, burung Maleo, drum dan lanskap Mandar..</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Lipaq Sabe")
        _, mid_column_lipaq, _ = st.columns([0.5, 7, 0.5])
        mid_column_lipaq.image('aset/sulbar/Lipak Sabe.png', use_column_width=True,
                               caption="Motif Lipaq Sabe")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Lipaq Sabe atau Lipaq Saqbe mengandung motif geometris klasik sederhana, dihiasi dengan berbagai simbol suku. Tekstil ini diklasifikasikan sebagai tekstil tenun, yang hanya dikenakan pada acara-acara tertentu seperti pernikahan, upacara tradisional, upacara keagamaan. Terkadang digunakan untuk salat Jumat di masjid.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
    elif batik_sulawesi == 'Sulawesi Tengah':
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Tradisi batik dan tenun Bomba di Palu berasal dari tradisi antar generasi. Orang Palu membuat benang sutra yang ditenun dengan alat tenun tradisional menjadi kain. Mereka juga memproduksi kain batik menggunakan pewarna alami yang berasal dari getah pohon. Batik Bomba dari waktu ke waktu mengalami perkembangan, seperti mulai dari penciptaan banyak motif yang menggambarkan budaya, tanaman, dan kadang-kadang motif yang menggambarkan puisi atau syair rindu nelayan tentang cinta dan kehidupan.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Taiganja")
        _, mid_column_taiganja, _ = st.columns([0.5, 7, 0.5])
        mid_column_taiganja.image('aset/sulteng/Taiganja.png', use_column_width=True,
                                  caption="Motif Taiganja")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Taiganja adalah liontin emas berharga yang menunjukkan status sosial keluarga Kaili. Pusaka ini sering digunakan sebagai mahar pernikahan dan sebagai benda sakral dalam upacara tradisional. Taiganja menggambarkan rahim seorang wanita, yang oleh masyarakat setempat dipercaya sebagai awal kehidupan manusia. Motif ini mewakili kesuburan dan menggambarkan perasaan cinta dan ketulusan hati.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Bunga Cengkeh")
        _, mid_column_bceng, _ = st.columns([0.5, 7, 0.5])
        mid_column_bceng.image('aset/sulteng/cengkeh.png', use_column_width=True,
                               caption="Motif Bunga Cengkeh")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Motif bunga cengkeh menggambarkan komoditas utama Kabupaten Tolitoli. Motif ini memiliki makna penyembuhan dan harapan baik untuk kesehatan dan kesejahteraan bagi pemakainya.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Bomba Mawar")
        _, mid_column_bomba, _ = st.columns([0.5, 7, 0.5])
        mid_column_bomba.image('aset/sulteng/Bomba Mawar.png', use_column_width=True,
                               caption="Motif Bomba Mawar")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;"> Motif ini berarti cinta sakral bagi keluarga, kerajaan, dan Tuhan; Ini juga menggambarkan keterbukaan dan kebersamaan dalam kehidupan sosial masyarakat Palu.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
    elif batik_sulawesi == 'Sulawesi Utara':
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Minahasa adalah sebuah kabupaten di Sulawesi Utara. Minahasa terkenal dengan keindahan kain tenunnya dan batik Minahasa. Batik Minahasa mengadopsi aksara suku asli dan motif-motif kuno. Motif-motif tersebut mengacu pada nilai-nilai budaya dan tradisi yang berkembang di setiap aspek kehidupan sosial masyarakat Minahasa.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Cengkih Berbunga")
        _, mid_column_cengber, _ = st.columns([0.5, 7, 0.5])
        mid_column_cengber.image('aset/sulut/Motif Cengkih Berbunga.jpg', use_column_width=True,
                                 caption="Motif Cengkih Berbunga")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Tanaman cengkih masih menjadi produk perkebunan andalan masyarakat Sulawesi Utara. Hampir seluruh bagian tanaman mengandung minyak atsiri dan bagian tanaman yang paling berharga adalah bunga. Ketika cengkih berbunga adalah saat hati petani cengkih berbunga-bunga harapan kesejahteraan.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Tari Kabasaran")
        _, mid_column_tarkab, _ = st.columns([0.5, 7, 0.5])
        mid_column_tarkab.image('aset/sulut/Tari Kabasaran.png', use_column_width=True,
                                caption="Motif Tari Kabasaran")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Motifnya menggambarkan tarian Kabasaran, yang merupakan tarian sakral yang ditampilkan dalam upacara adat Minahasa. Di zaman kuno, tarian ini dilakukan untuk dapat membunuh atau mengusir dari roh jahat yang mengganggu upacara.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Pinawetangan")
        _, mid_column_pinawetangan, _ = st.columns([0.5, 7, 0.5])
        mid_column_pinawetangan.image('aset/sulut/Pinawetangan.png', use_column_width=True,
                                      caption="Motif Pinawetangan")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Pola Batik Pinawetengan diambil dari prasasti prasejarah di Sulawesi Utara, yang disebut Watu Pinawetengan, yang ada sejak 1000 SM. Situs budaya ini ditemukan oleh J.G.F. Riedel pada tahun 1881. Situs ini adalah tempat di mana nenek moyang orang Minahasa membagi wilayah mereka menjadi sembilan kelompok sub-etnis Minahasa saat ini. Motif utama kain Pinawetengan adalah bunga matahari yang merupakan ikon Desa Pinawetengan, di mana situs Watu Pinawetengan berada.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
    elif batik_sulawesi == 'Sulawesi Tenggara':
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Sulawesi Tenggara memiliki batik tenun dengan motif Tolaki. Batik tenun Tolaki adalah primadona di Sulawesi Tenggara. Motif Tolaki memiliki ciri khas, berupa benang emas yang membentuk garis-garis halus, dan ada aksen floral yang kecil.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Ake Patra")
        _, mid_column_akepatra, _ = st.columns([0.5, 7, 0.5])
        mid_column_akepatra.image('aset/sultenggara/Ake Patra.png', use_column_width=True,
                                  caption="Motif Ake Patra")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Ake terkait dengan keilahian dan komposisi alam semesta. Itu adalah simbol pencerahan Allah bagi Raja. Motif ini biasanya diproduksi pada tekstil tenun, tetapi baru-baru ini para produsen di Sulawesi Tenggara juga mencoba mengembangkan versi Batik dari motif ini.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Wakatobi")
        _, mid_column_wakatobi, _ = st.columns([0.5, 7, 0.5])
        mid_column_wakatobi.image('aset/sultenggara/Wakatobi.png', use_column_width=True,
                                  caption="Motif Wakatobi")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Motif batik ini melambangkan keindahan pesisir pulau Wakatobi. Simbol daun Patra mengacu pada kesadaran diri dan keilahian. Motif Batik ini diciptakan oleh produsen lokal sebagai motif Batik khas Daerah Khusus Wakatobi, Sulawesi Tenggara.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Kalo Sara")
        _, mid_column_kalo, _ = st.columns([0.5, 7, 0.5])
        mid_column_kalo.image('aset/sultenggara/Kalo Sara.png', use_column_width=True,
                              caption="Motif Kalo Sara")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Kalo Sara adalah motif sakral untuk etnis Tolaki. Ini dianggap sebagai cara hidup, penciptaan tatanan sosial dan moral dalam masyarakat. Motif ini jug merepresentasikan solusi untuk mengatasi konflik sosial-budaya di komunitas Tolaki. Motif ini dapat ditemukan dalam arsitektur tradisional, juga dalam Batik, dan tekstil tenun.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
    elif batik_sulawesi == 'Sulawesi Selatan':
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Batik Sulawesi Selatan memiliki beberapa motif seperti motif Toraja dan Bugis. Batik ini umumnya diproduksi dengan menggunakan teknik pembuatan batik yang sama seperti batik Jawa. Namun, Batik dari Tana Toraja tidak mendapat pengaruh seni pembuatan Batik dari India seperti wilayah Nusantara lainnya. Namun, orang Toraja secara mengejutkan membuat batik menggunakan pewarnaan lilin yang berasal dari kearifan lokal mereka sejak sebelum berabad-abad.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Tongkonan")
        _, mid_column_tongkonan, _ = st.columns([0.5, 7, 0.5])
        mid_column_tongkonan.image('aset/sulsel/Tongkonan.png', use_column_width=True,
                                   caption="Motif Tongkonan")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Rumah tradisional Toraja disebut Tongkonan. Tongkonan adalah tempat bagi orang-orang di desa untuk berkonsultasi dan menyelesaikan masalah komunitas. Hampir semua rumah Toraja menghadap ke utara karena diyakini bahwa utara adalah arahan Tuhan. Orang Toraja percaya bahwa ketika penghuni menginjakkan kaki di luar rumah, mereka akan dibimbing oleh kehendak ilahi dan keberuntungan.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Lontara")
        _, mid_column_lontara, _ = st.columns([0.5, 7, 0.5])
        mid_column_lontara.image('aset/sulsel/Lontara.png', use_column_width=True,
                                 caption="Motif Lontara")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Aksara Lontara adalah aksara kuno khas komunitas Bugis dan Makassar. Sejarah mencatat bahwa aksara Lontara adalah pengembangan dari aksara Kawi yang sudah ada di Nusantara sekitar abad ke-8.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif La Galigo")
        _, mid_column_lagaligo, _ = st.columns([0.5, 7, 0.5])
        mid_column_lagaligo.image('aset/sulsel/La Galigo.png', use_column_width=True,
                                  caption="Motif La Galigo")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">La Galigo adalah karya sastra Epic Bugis yang memiliki 300.000 cerita epik. Epik ini bahkan dianggap lebih panjang dari kisah Mahabharata India. Salah satu epik La Galigo menggambarkan asal-usul Sangiang Serri, tradisi persembahan seremonial yang dilakukan oleh petani sebelum musim tanam. Perajin batik lokal terinspirasi dari cerita La Galigo untuk menciptakan motif batik.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
    elif batik_sulawesi == 'Gorontalo':
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Batik Gorontalo dibuat dari hasil akulturasi antara batik dan sulaman karawo. Sejak abad ke-16, masyarakat Gorontalo mengembangkan warisan tekstilnya sendiri yaitu, sulaman Karawo. Selama era kolonial (abad 17-19), banyak tradisi dihapuskan oleh kolonial. Komunitas perempuan yang melarikan diri dari invasi dan tinggal di hutan mampu melestarikan tradisi dan mewariskannya dari generasi ke generasi.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Jagung")
        _, mid_column_jagung, _ = st.columns([0.5, 7, 0.5])
        mid_column_jagung.image('aset/gor/jagung.png', use_column_width=True,
                                caption="Motif Jagung")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Filosofi motif jagung menggambarkan mimpi dan semangat hidup yang tidak pernah mati. Motif ini juga berarti bahwa orang yang berpikir positif akan lebih bahagia dan memiliki kualitas hidup yang lebih baik. Hidupnya digerakkan oleh semangat yang baik dan kepercayaan diri untuk mencapai kesuksesan.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Karawo Pinang")
        _, mid_column_pinang, _ = st.columns([0.5, 7, 0.5])
        mid_column_pinang.image('aset/gor/karawo pinang.png', use_column_width=True,
                                caption="Motif Karawo Pinang")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Motif Pinang menggambarkan pohon pinang palem. Motif ini dianggap sebagai pola asli tekstil sulaman Karawo. Arti dari motif ini adalah seseorang yang berpikiran lurus, protektif, perfeksionis, dan memiliki karakter pejuang. Tekstil Karawo Gorontalo disajikan dalam 4 warna tradisional. Kuning melambangkan kemakmuran, hijau berarti kesuburan, merah berarti keberanian, dan ungu dianggap sebagai simbol kekhidmatan.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Teluk Tomini")
        _, mid_column_tomini, _ = st.columns([0.5, 7, 0.5])
        mid_column_tomini.image('aset/gor/Teluk Tomini.png', use_column_width=True,
                                caption="Motif Teluk Tomini")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Motif ini menggambarkan keindahan kehidupan bawah laut di Teluk Tomini. Motif batik menggambarkan makhluk air dan ikan berwarna-warni yang menjadi kekayaan hayati daerah ini.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)

elif jenis_info == 'Batik Bali, NTB, dan NTT':
    st.header('Yuk Berkenalan dengan Jenis-Jenis Batik di Pulau Bali, NTB, NTT, dan sekitarnya!')
    st.markdown('<hr>', unsafe_allow_html=True)
    batik_balintbntt = st.selectbox(
        'Pilih jenis daerah',
        ('Bali',
         'Nusa Tenggara Barat',
         'Nusa Tenggara Timur'))
    if batik_balintbntt == 'Bali':
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Motif dan hiasan batik di Bali pada umumnya terkait dengan hewan di pulau ini, baik hewan nyata seperti rusa, bangau, dan kura-kura; atau hewan mitos seperti naga, barong, kala, dan singa bersayap. Selain itu juga tetumbuhan khas di Bali yaitu Bunga Kamboja dan Bunga Sepatu. Seperti karya seninya yang lain, lukisan Bali menggambarkan keseharian masyarakat seperti misalnya menari, prosesi kremasi, menanam padi, atau ritual keagamaan. Bukan tanpa alasan Bali disebut “Pulau Dewata”. Mereka menomorsatukan spiritualitas dalam segala hal – baik memasak, melukis, memahat, menenun, menari, menanam padi, atau apapun. Mereka bermeditasi ketika bekerja, dan menganggap segala hal yang mereka lakukan sebagai bentuk ibadah.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Merak Abyorhokokai")
        _, mid_column_merak_abyorhokokai, _ = st.columns([0.5, 7, 0.5])
        mid_column_merak_abyorhokokai.image('aset/Bali/Merak Abyorhokokai.png', use_column_width=True,
                                            caption="Motif Merak Abyorhokokai")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Batik bermotif merak ini menggambarkan keindahan burung tersebut sebagai titik fokus kain, dan gambar ini semakin diperindah dengan hiasan kelopak bunga yang lembut yang tampilannya mirip bunga kersen. Motif ini merupakan pengaruh dari budaya Jepang, dan menggambarkan semangat Bali sebagai Pulau Dewata.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Buketan Bali")
        _, mid_column_buketan_bali, _ = st.columns([0.5, 7, 0.5])
        mid_column_buketan_bali.image('aset/Bali/Buketan Bali.png', use_column_width=True,
                                      caption="Motif Buketan Bali")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Buketan Bali merupakan desain karangan bunga. Nama ini berasal dari bahasa Perancis, dan pertama kali diproduksi di Indonesia pada tahun 1880 oleh seorang pengusaha batik wanita dari Belanda bernama Cristina Van Zuylen. Batik adalah sesuatu yang keren dan eksotis, dan bahasa Perancis selalu menandakan sesuatu yang dianggap unik dan berkelas tinggi di Eropa abad ke-17, termasuk di Belanda. Motif ini berupa karangan atau rangkaian yang disusun di sepanjang sisi kain, seringkali dengan ditambahi hiasan tambahan berupa kupu-kupu atau burung phoenix untuk menambah nilai artistiknya.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Barong Bali")
        _, mid_column_barong_bali, _ = st.columns([0.5, 7, 0.5])
        mid_column_barong_bali.image('aset/Bali/Barong Bali.png', use_column_width=True,
                                     caption="Motif Barong Bali")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Barong merupakan hewan mitos yang memiliki kekuatan supernatural. Hewan ini merupakan gabungan dari macan atau singa (badan, kaki, dan matanya), elang, gajah, dan naga (mulut menyeringai dengan lidah panjang). Hewan ini seringkali ditemukan dalam karya seni Jawa dan Bali sebagai perlambang kekuatan, kebenaran, dan kejantanan. Barong juga merupakan lambang falsafah bahwa manusia memiliki dua sisi. Kita harus mengendalikan hasrat buruk dan menahan diri dari godaan agar dapat berkembang sempurna sebagai manusia yang dewasa dan bjiak.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
    if batik_balintbntt == 'Nusa Tenggara Barat':
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Motif batik sasambo tampaknya abstrak, indah, dan mistis. Motifnya memiliki nilai historis, artistik, dan filosofis yang luar biasa. Motifnya mengilustrasikan adat dan budaya setempat. Misalnya, motif bayam air yang menggambarkan makanan khas Lombok; Motif Lombok, mutiara, dan tembikar; Motif Rumah Panggung mewakili rumah tradisional pulau Sumbawa; Motif lumbung Raja Bima, Kerang, Daun Pepaya, daun Bebele, dan Tokek.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Bale Lumbu")
        _, mid_column_bale_lumbu, _ = st.columns([0.5, 7, 0.5])
        mid_column_bale_lumbu.image('aset/ntb/Bale Lumbu.png', use_column_width=True,
                                    caption="Motif Bale Lumbu")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Motif ini menandakan kesejahteraan masyarakat Sasak kuno. Bale juga melambangkan bentuk rumah tradisional masyarakat Sembalun, Lombok Timur. Bale juga berfungsi sebagai lumbung makanan tradisional yang digunakan oleh masyarakat desa Lombok.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Tenun Bima")
        _, mid_column_tenun_bima, _ = st.columns([0.5, 7, 0.5])
        mid_column_tenun_bima.image('aset/ntb/Tenun Bima.png', use_column_width=True,
                                    caption="Motif Tenun Bima")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Motif-motif diadopsi dari tekstil tenun Bima. Pola ini kurang lebih mendapat pengaruh besar dari budaya Islam. Hal unik lainnya tentang batik ini adalah pemilihan warna dan garis geometris segitiga. Kombinasi warna memiliki setidaknya 3 warna dengan dasar hitam atau putih.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Tari Peresean")
        _, mid_column_tari_peresean, _ = st.columns([0.5, 7, 0.5])
        mid_column_tari_peresean.image('aset/ntb/Tari Peresean.png', use_column_width=True,
                                       caption="Motif Tari Peresean")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Motif ini menggambarkan pertunjukan tari Peresean yang biasanya dilakukan pada peringatan Hari Proklamasi, atau hari libur besar lainnya. Peresean adalah permainan yang mengadu kekuatan antar pemain. Dalam tarian ini, para pemain diperbolehkan saling memukul dengan menggunakan rotan hingga lawan menyerah. Terkadang pemain menggunakan ilmu sihir untuk memenangkan permainan, misalnya, Bau Balung. Bau Balung adalah sihir yang dapat menyebabkan lawan kehilangan energi. Motif Peresean digambarkan dalam motif batik sebagai apresiasi yang dibuat untuk melestarikan seni pertunjukan khusus ini di Lombok, Nusa Tenggara Barat.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
    if batik_balintbntt == 'Nusa Tenggara Timur':
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Karena Nusa Tenggara Timur dikenal sebagai daerah tekstil tenun utama di Indonesia, produsen lokal mengembangkan industri Batik dengan bantuan pengrajin batik dari Jawa. Motif batik sebagian besar mencerminkan tokoh mitos, hewan, tanaman, dan ide-ide abstrak yang mengekspresikan penghargaan dan harapan baik. Setiap pulau mengembangkan motif lokal mereka. Misalnya, Pulau Sumba terkenal dengan motif binatang dan Pulau Rote dengan motif daun.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Kuda Sepasang")
        _, mid_column_kuda_sepasang, _ = st.columns([0.5, 7, 0.5])
        mid_column_kuda_sepasang.image('aset/ntt/Kuda Sepasang.png', use_column_width=True,
                                       caption="Motif Kuda Sepasang")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Bagi masyarakat Kupang, memiliki kuda yang kuat adalah simbol martabat dan harga diri. Motif kuda juga melambangkan kebanggaan, kekuatan, dan keberanian. Sepasang kuda melambangkan kehidupan pernikahan yang harmonis. Arti dari motif ini adalah untuk saling mencintai, untuk menciptakan hubungan yang bahagia, penuh kasih dan kepedulian antara suami dan istri.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Pucuk Mekar")
        _, mid_column_pucuk_mekar, _ = st.columns([0.5, 7, 0.5])
        mid_column_pucuk_mekar.image('aset/ntt/Pucuk Mekar.png', use_column_width=True,
                                     caption="Motif Pucuk Mekar")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Motif ini menggambarkan tanaman yang mulai mekar saat musim hujan dimulai. Motif ini mencerminkan kegembiraan dan syukur kepada Tuhan atas rahmat hujan. Nusa Tenggara Timur, secara umum, dikenal sebagai daerah kering Indonesia. Karena itu, tetesan hujan dianggap sebagai hadiah besar dan simbol berkah melimpah bagi masyarakat Kupang.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Kuda Kupang")
        _, mid_column_kuda_kupang, _ = st.columns([0.5, 7, 0.5])
        mid_column_kuda_kupang.image('aset/ntt/Kuda Kupang.png', use_column_width=True,
                                     caption="Motif Kuda Kupang")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Kuda melambangkan kekayaan dan dianggap sebagai hewan yang sangat membantu untuk kegiatan sehari-hari masyarakat seperti sarana transportasi darat, kegiatan upacara tradisional, dll. Kuda juga melambangkan kebanggaan, kekuatan, dan keberanian. Motif ini menyiratkan pesona pribadi pemakainya, serta makna lain seperti persahabatan, harmoni, gairah, dan ketekunan dalam mengejar tujuan mereka. Motif ini berisi nilai-nilai luhur karakter berbudi luhur yang membawa manfaat bagi kemakmuran sosial dan kebahagiaan.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)

elif jenis_info == 'Batik Maluku dan Papua':
    st.header('Yuk Berkenalan dengan Jenis-Jenis Batik di Pulau Maluku, Papua, dan sekitarnya!')
    st.markdown('<hr>', unsafe_allow_html=True)
    batik_malukupapua = st.selectbox(
        'Pilih jenis daerah',
        ('Maluku',
         'Papua',
         'Papua Barat'))
    if batik_malukupapua == 'Papua':
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Motif batik Papua cenderung mewakili pemandangan alamnya. Beberapa motif seperti motif Tifa, motif Asmat (lambang patung kayu dari suku Asmat), atau motif Tifa (alat musik tradisional dari Papua) mendominasi motif batik Papua. Sementara motif Surga dan motif Asmat adalah motif Batik khas yang mewakili identitas Papua, motif Tifa Kamaro Timika mengacu pada makna filosofis tertentu. Motif ini berarti rumah yang penuh dengan kebahagiaan.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Asmat Papua")
        _, mid_column_asmat_papua, _ = st.columns([0.5, 7, 0.5])
        mid_column_asmat_papua.image('aset/Papua/Asmat Papua.png', use_column_width=True,
                                     caption="Motif Asmat Papua")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Motif batik menggambarkan motif kesukuan suku Asmat yang pada umumnya ditemukan pada patung kayu. Batik Asmat biasanya dibuat menggunakan pewarna alami dari tanah terakota. Motif batik jenis ini umumnya diproduksi di banyak daerah di Papua, termasuk provinsi Papua Barat.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Kamaro Timika")
        _, mid_column_kamaro_timika, _ = st.columns([0.5, 7, 0.5])
        mid_column_kamaro_timika.image('aset/Papua/Kamaro Timika.png', use_column_width=True,
                                       caption="Motif Kamaro Timika")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Motif ini terinspirasi dari simbol suci komunitas Kamaro di Timika Papua. Polanya memiliki berbagai makna yang berbeda, diantaranya seperti ikatan kuat antara komunitas, persaudaraan, dan perlindungan terhadap nasib buruk.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Tifa")
        _, mid_column_tifa, _ = st.columns([0.5, 7, 0.5])
        mid_column_tifa.image('aset/Papua/Tifa.png', use_column_width=True,
                              caption="Motif Tifa")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Motif ini berasal dari alat musik tradisional Papua, Tifa. Tifa adalah sejenis alat musik perkusi dari kayu berbentuk tabung. Satu sisi instrumen ditutup dengan kulit binatang kering. Bentuk dan fungsinya sekilas hampir sama dengan instrumen drum, tetapi suara yang dihasilkan terdengar lebih ringan. Tifa digunakan untuk mengiringi upacara tradisional dan tarian tradisional.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
    elif batik_malukupapua == 'Maluku':
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Maluku dikenal luas sebagai penghasil rempah-rempah. Permintaan rempah-rempah yang tinggi pada abad ke-15 hingga ke-19 mendorong orang Portugis, Belanda, dan Inggris untuk mengendalikan perdagangan rempah-rempah. Tidak mengherankan bila cengkeh dan pala menjadi motif khas batik Maluku. Selain itu, motif mereka juga mencerminkan kekayaan dan keanekaragaman budaya di Maluku.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Pala Salawaku")
        _, mid_column_salawaku, _ = st.columns([0.5, 7, 0.5])
        mid_column_salawaku.image('aset/maluku/pala_salawaku.png', use_column_width=True,
                                    caption="Motif Pala Salawaku")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Motif ini menggambarkan senjata tradisional yang unik dari wilayah Maluku, yang disebut Salawaku. Belati salawaku digunakan di banyak lingkungan sosial lokal, karena melambangkan identitas masyarakat Maluku seperti dalam tarian tradisional, ritual, dan pola tekstil. Sementara kata ‘Pala’ mengacu pada pala sebagai salah satu komoditas utama Maluku.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Pantai Ambon")
        _, mid_column_ambon, _ = st.columns([0.5, 7, 0.5])
        mid_column_ambon.image('aset/maluku/pantai_ambon.png', use_column_width=True,
                               caption="Motif Pantai Ambon")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Batik kota Ambon menggambarkan kekayaan alam dan kehidupan bahari teluk Ambon. Warna-warna cerah dan pola asimetris mencerminkan dinamisme dan keterbukaan masyarakat pesisir.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Pattimura")
        _, mid_column_pattimura, _ = st.columns([0.5, 7, 0.5])
        mid_column_pattimura.image('aset/maluku/pattimura.png', use_column_width=True,
                                            caption="Motif Pattimura")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Pattimura adalah nama pahlawan Indonesia yang berperang melawan kolonialisme di abad ke-18. Motif Pattimura diilustrasikan dalam kombinasi dengan motif suku khas lainnya di wilayah Maluku. Motif ini berarti kerja sama dalam masyarakat dan kepahlawanan.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
    elif batik_malukupapua == 'Papua Barat':
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Umumnya, motif khas Papua Barat sebagian besar mirip dengan yang dikembangkan di provinsi Papua. Motif-motifnya cenderung mewakili pemandangan alamnya seperti terumbu karang Raja Ampat yang terkenal dan taman laut. Beberapa motif yang paling terkenal dari Papua Barat adalah seperti motif burung Paradise, Honai (rumah tradisional masyarakat Papua), atau motif Tifa (alat musik tradisional dari Papua). Motif Tifa Honai mengacu pada makna filosofis tertentu. Motif ini berarti rumah yang penuh dengan kebahagiaan.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Raja Ampat")
        _, mid_column_raja_ampat, _ = st.columns([0.5, 7, 0.5])
        mid_column_raja_ampat.image('aset/Papuabarat/Raja Ampat.png', use_column_width=True,
                                    caption="Motif Raja Ampat")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Motif Raja Ampat menggambarkan kehidupan bahari di kepulauan Raja Ampat di Papua Barat. Raja Ampat adalah cagar alam yang indah yang terdiri dari sekelompok pulau membentuk lanskap unik dengan air pirus kristal. Tempat ini juga terkenal dengan terumbu karang dan taman lautnya yang indah.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Honai")
        _, mid_column_honai, _ = st.columns([0.5, 7, 0.5])
        mid_column_honai.image('aset/Papuabarat/Honai.png', use_column_width=True,
                               caption="Motif Honai")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Honai merupakan motif yang terinspirasi dari rumah tradisional masyarakat Papua yang tinggal di pegunungan. Honai adalah rumah berbentuk bulat dengan atap yang terbuat dari kayu dan jerami. Honai melambangkan persatuan di antara suku-suku. Motif ini juga mewakili simbol kepribadian, integritas budaya, dan martabat suku.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.write("### Motif Burung Cendrawasih")
        _, mid_column_burung_cendrawasih, _ = st.columns([0.5, 7, 0.5])
        mid_column_burung_cendrawasih.image('aset/Papuabarat/Burung Cendrawasih.png', use_column_width=True,
                                            caption="Motif Burung Cendrawasih")
        st.markdown(
            '<div style="text-align: justify; font-size:100%; text-indent: 4em;">Burung Cendrawasih merupakan motif yang menggambarkan burung endemik di tanah Papua. Cendrawasih adalah salah satu spesies burung langka, dilindungi oleh pemerintah Indonesia. Burung ini dipercaya sebagai burung surga yang menghubungkan kehidupan di bumi dengan surga. Motif ini juga dianggap sebagai motif sakral dan mewakili identitas masyarakat Papua, baik di provinsi Papua maupun Papua Barat.</div>',
            unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)


elif jenis_info == 'Coming Soon':
    st.header('Coming Soon!')
    st.markdown('<hr>', unsafe_allow_html=True)