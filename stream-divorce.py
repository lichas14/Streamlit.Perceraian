import pickle 
import numpy as np
import streamlit as st

model = pickle.load(open('divorece_model.sav', 'rb'))

st.title('Prediksi Perceraian')
st.subheader('- tanggapan skala 0 - 5 poin :')
st.text('0=Tidak pernah, 1=Pernah, 2=Kadang, 3=Sering, 4=Selalu.')
col1, col2, col3 = st.columns (3)

with col1:
Q1 = st.text_input('Jika salah satu dari kami meminta maaf saat diskusi kami memburuk, diskusi berakhir.')
with col1:
Q2 = st.text_input('Saya tahu kita bisa mengabaikan perbedaan kita, bahkan jika terkadang keadaan menjadi sulit.')
with col1:
Q3 = st.text_input('Ketika kami membutuhkannya, kami dapat berdiskusi dengan pasangan saya dari awal dan memperbaikinya.')
with col1:
Q4 = st.text_input('Ketika saya berdiskusi dengan pasangan saya, menghubungi dia pada akhirnya akan berhasil.')
with col1:
Q5 = st.text_input('Waktu yang saya habiskan bersama istri saya spesial bagi kami.')
with col1:
Q6 = st.text_input('Kami tidak punya waktu di rumah sebagai mitra.')
with col1:
Q7 = st.text_input('Kami seperti dua orang asing yang berbagi lingkungan yang sama di rumah daripada keluarga.')
with col1:
Q8 = st.text_input('Saya menikmati liburan kami dengan istri saya.')
with col1:
Q9 = st.text_input('Saya senang bepergian dengan istri saya.')
with col1:
Q10 = st.text_input('Sebagian besar tujuan kita sama dengan pasangan saya.')
with col1:
Q11 = st.text_input('Saya pikir suatu hari nanti, ketika saya melihat ke belakang, saya melihat bahwa pasangan saya dan saya telah rukun satu sama lain.')
with col1:
Q12 = st.text_input('Pasangan saya dan saya memiliki nilai yang sama dalam hal kebebasan pribadi.')
with col1:
Q13 = st.text_input('Pasangan saya dan saya memiliki selera hiburan yang sama.')
with col1:
Q14 = st.text_input('Sebagian besar tujuan kita untuk orang (anak-anak, teman, dll.) Adalah sama.')
with col1:
Q15 = st.text_input('Impian kami dengan pasangan saya serupa dan harmonis.')
with col1:
Q16 = st.text_input('Kami cocok dengan pasangan saya tentang apa itu cinta.')
with col1:
Q17 = st.text_input('Kami berbagi pandangan yang sama tentang menjadi bahagia dalam hidup kami dengan pasangan saya.')
with col1:
Q18 = st.text_input('Pasangan saya dan saya memiliki gagasan yang sama tentang bagaimana pernikahan seharusnya.')
with col1:
Q19 = st.text_input('Pasangan saya dan saya memiliki gagasan yang sama tentang bagaimana seharusnya peran dalam pernikahan.')
with col2:
Q20 = st.text_input('Pasangan saya dan saya memiliki nilai kepercayaan yang sama.')
with col2:
Q21 = st.text_input('Saya tahu persis apa yang disukai istri saya.')
with col2:
Q22 = st.text_input('Saya tahu bagaimana pasangan saya ingin dirawat ketika dia sakit.')
with col2:
Q23 = st.text_input('Saya tahu makanan favorit pasangan saya.')
with col2:
Q24 = st.text_input('Saya dapat memberi tahu Anda jenis stres apa yang dihadapi pasangan saya dalam hidupnya.')
with col2:
Q25 = st.text_input('Saya memiliki pengetahuan tentang dunia batin pasangan saya.')
with col2:
Q26 = st.text_input('Saya tahu kecemasan dasar pasangan saya.')
with col2:
Q27 = st.text_input('Saya tahu apa sumber stres pasangan saya saat ini.')
with col2:
Q28 = st.text_input('Saya tahu harapan dan keinginan pasangan saya.')
with col2:
Q29 = st.text_input('Saya sangat mengenal pasangan saya.')
with col2:
Q30 = st.text_input('Saya mengenal teman-teman pasangan saya dan hubungan sosial mereka.')
with col2:
Q31 = st.text_input('Saya merasa agresif ketika saya berdebat dengan pasangan saya.')
with col2:
Q32 = st.text_input('Saat berdiskusi dengan pasangan saya, saya biasanya menggunakan ekspresi seperti kamu selalu atau kamu tidak pernah.')
with col2:
Q33 = st.text_input('Saya dapat menggunakan pernyataan negatif tentang kepribadian pasangan saya selama diskusi kami.')
with col2:
Q34 = st.text_input('Saya dapat menggunakan ekspresi ofensif selama diskusi kami.')
with col2:
Q35 = st.text_input('Saya dapat menghina pasangan saya selama diskusi kami.')
with col2:
Q36 = st.text_input('Saya bisa mempermalukan saat kita berdiskusi.')
with col2:
Q37 = st.text_input('Diskusi saya dengan pasangan saya tidak tenang.')
with col2:
Q38 = st.text_input('Saya benci cara pasangan saya membuka topik.')
with col3:
Q39 = st.text_input('Diskusi kami sering terjadi secara tiba-tiba.')
with col3:
Q40 = st.text_input('Kami baru saja memulai diskusi sebelum saya tahu apa yang terjadi.')
with col3:
Q41 = st.text_input('Ketika saya berbicara dengan pasangan saya tentang sesuatu, ketenangan saya tiba-tiba hilang.')
with col3:
Q42 = st.text_input('Ketika saya berdebat dengan pasangan saya, saya hanya keluar dan tidak mengatakan sepatah kata pun.')
with col3:
Q43 = st.text_input('Saya kebanyakan diam untuk sedikit menenangkan lingkungan.')
with col3:
Q44 = st.text_input('Kadang-kadang saya pikir itu baik bagi saya untuk meninggalkan rumah untuk sementara waktu.')
with col3:
Q45 = st.text_input('Saya lebih suka diam daripada berdiskusi dengan pasangan saya.')
with col3:
Q46 = st.text_input('Bahkan jika saya benar dalam diskusi, saya tetap diam untuk menyakiti pasangan saya.')
with col3:
Q47 = st.text_input('Saat saya berdiskusi dengan pasangan saya, saya diam saja karena takut tidak bisa mengendalikan amarah saya.')
with col3:
Q48 = st.text_input('Saya merasa benar dalam diskusi kami.')
with col3:
Q49 = st.text_input('Saya tidak ada hubungannya dengan apa yang dituduhkan kepada saya.')
with col3:
Q50 = st.text_input('Saya sebenarnya bukan orang yang bersalah atas apa yang dituduhkan kepada saya.')
with col3:
Q51 = st.text_input('Saya bukan orang yang salah tentang masalah di rumah.')
with col3:
Q52 = st.text_input('Saya tidak akan ragu untuk memberi tahu pasangan saya tentang kekurangannya.')
with col3:
Q53 = st.text_input('Ketika saya berdiskusi, saya mengingatkan pasangan saya tentang kekurangannya.')
with col3:
Q54 = st.text_input('Saya tidak takut untuk memberi tahu pasangan saya tentang ketidakmampuannya.')
with col3:
prediksi_percerraian = ''

if st.button('Prediksi'):
    prediksi_percerraian = model.predict([[Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16, Q17, Q18, Q19, Q20, Q21, Q22, Q23, Q24, Q25, Q26, Q27, Q28, Q29, Q30, Q31, Q32, Q33, Q34, Q35, Q36, Q37, Q38, Q39, Q40, Q41, Q42, Q43, Q44, Q45, Q46, Q47, Q48, Q49, Q50, Q51, Q52, Q53, Q54]])
    
    if (prediksi_percerraian[0]==1):
        prediksi_percerraian = 'Pasangan Melakukan Perceraian'
    else:
        prediksi_percerraian = ' Pasangan Tidak Melakukan Perceraian'
        
st.success(prediksi_percerraian)