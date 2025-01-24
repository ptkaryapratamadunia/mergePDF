# merging_pdf_tools
Tools ini secara umum dibuat untuk mempermudah user menggabungkan 2 atau lebih file PDF.
Khusus di bagian Admin QC yang memerlukan tools ini untuk menginput data NG ke App QC WEB BOARD.
Dibuat dengan pemrogaman sederhana menggunakan python dan framework streamlit.
Semoga bermanfaat.

e-WeYe @2025

----- explaination of step establishing this web tools ---------
Penjelasan Kode:

Import Library:

streamlit as st: Untuk membuat antarmuka web.
PyPDF2.PdfMerger: Untuk menggabungkan file PDF.
os: Untuk operasi sistem, dalam hal ini menghapus file sementara.
Judul Aplikasi:

st.title("Penggabung File PDF"): Menampilkan judul aplikasi.
Pengunggahan File:

uploaded_files = st.file_uploader(...): Membuat area untuk mengunggah file.
accept_multiple_files=True: Memungkinkan pengunggahan beberapa file sekaligus.
Proses Penggabungan:

if uploaded_files:: Memeriksa apakah ada file yang diunggah.
if st.button("Gabungkan PDF"):: Membuat tombol "Gabungkan PDF".
if len(uploaded_files) < 2:: Memvalidasi apakah setidaknya dua file telah diunggah. Jika tidak, akan menampilkan pesan error.
merger = PdfMerger(): Membuat objek PdfMerger.
for pdf_file in uploaded_files:: Melakukan iterasi pada setiap file yang diunggah dan menambahkannya ke objek merger dengan merger.append(pdf_file).
Nama File Keluaran dan Penyimpanan:

output_filename = st.text_input(...): Membuat input teks untuk nama file keluaran.
if output_filename:: Memeriksa apakah nama file keluaran telah diisi.
merger.write(output_filename): Menulis (menyimpan) file PDF yang telah digabungkan dengan nama yang diberikan.
st.success(...): Menampilkan pesan sukses.
Tombol Unduh:

st.download_button(...): Membuat tombol untuk mengunduh file yang telah digabungkan.
os.remove(output_filename) : Menghapus file sementara setelah didownload
Penanganan Error:

try...except: Menangani kemungkinan error selama proses penggabungan.
Cara Menjalankan Aplikasi:

Pastikan Anda telah menginstal library yang dibutuhkan: pip install streamlit PyPDF2.
Simpan kode di atas sebagai file Python, misalnya app.py.
Buka terminal atau command prompt, lalu navigasi ke direktori tempat Anda menyimpan file app.py.
Jalankan perintah streamlit run app.py.
Aplikasi akan terbuka di browser Anda. Anda dapat mengunggah file PDF, memberikan nama file keluaran, dan mengunduh file PDF yang telah digabungkan.

Penting: Kode ini menggunakan library PyPDF2. Library ini memiliki beberapa keterbatasan dalam menangani beberapa jenis file PDF yang kompleks. Jika Anda mengalami masalah dengan file PDF tertentu, Anda mungkin perlu mempertimbangkan library yang lebih canggih seperti PyMuPDF (fitz).
