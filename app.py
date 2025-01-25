#24Jan2025 untuk indra kerja biar mudah terus diupload di QCWeboard
import os
from PyPDF2 import PdfMerger
import streamlit as st
from PIL import Image

logo = Image.open("logokpd.png")
st.image(logo, width=36)
st.write("KPD", align="right")
st.title("Tools Penggabung File PDF")
st.write("Tools untuk menggabungkan beberapa file PDF menjadi satu file PDF.") #e-WeYe

uploaded_files = st.file_uploader("Unggah file PDF", accept_multiple_files=True)

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
            else:
                st.warning("Harap masukkan nama file keluaran.")

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)