#24Jan2025 untuk indra kerja biar mudah terus diupload di QCWeboard
import os
from PyPDF2 import PdfMerger
import streamlit as st
from PIL import Image


def show_footer():	
    #Footer diisi foto ditaruh ditengah
    st.markdown("---")


    kaki_kiri,kaki_kiri2, kaki_tengah,kaki_kanan2, kaki_kanan=st.columns((1,0.5,2,0.5,1))

    with kaki_kiri:
        st.write("")

    with kaki_kiri2:
        st.write("")

    with kaki_tengah:
    
        logo = Image.open("eweye.png")
        st.image(logo, use_container_width=True) 
        st.write("© 2025 e-WeYe. All rights reserved.")

    with kaki_kanan2:
        st.write("")

    with kaki_kanan:
        st.write("")

# ---- MAIN PAGE ----

header_L, header_R = st.columns([1, 4])

with header_L:
    st.write("")

with header_R:
    st.image("bismillah.png", width=360)

kiri, kanan = st.columns([9, 1])

with kanan:

    logo = Image.open("logokpd.png")
    st.image(logo, width=27)
    # st.write("KPD", align="right")

with kiri:

    st.title("Tools Penggabung File PDF")

st.write("Tools untuk menggabungkan beberapa file PDF menjadi satu file PDF.") #e-WeYe


uploaded_files = st.file_uploader("Unggah file PDF minimal 2 file", accept_multiple_files=True)

if uploaded_files:
    if st.button("Gabungkan PDF"):
        if len(uploaded_files) < 2:
            st.error("Harap unggah setidaknya dua file PDF. - e-WeYe")
        else:
            merger = PdfMerger()
            for pdf_file in uploaded_files:
                merger.append(pdf_file)

            output_filename = st.text_input("Nama file hasil penggabungan", "file_gabungan.pdf")
            if output_filename:
                try:
                    merger.write(output_filename)
                    st.success(f"File PDF berhasil digabungkan dan disimpan sebagai {output_filename}")
                    with open(output_filename, "rb") as f:
                        st.download_button(
                            label="Download File Gabungan",
                            data=f,
                            file_name=output_filename,
                            mime="application/pdf"
                        )
                    os.remove(output_filename) #menghapus file setelah didownload
                except Exception as e:
                    st.error(f"Terjadi kesalahan: {e}")

                show_footer()


            else:
                st.warning("Harap masukkan nama file keluaran.")

    show_footer()


# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)