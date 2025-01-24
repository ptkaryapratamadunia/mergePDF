#24Jan2025 untuk indra kerja biar mudah terus diupload si QCWeboard
import os
from PyPDF2 import PdfMerger
import streamlit as st

st.title("Tools Penggabung File PDF")
st.write("Dengan tools ini, Anda dapat menggabungkan beberapa file PDF menjadi satu file PDF.") #e-WeYe

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