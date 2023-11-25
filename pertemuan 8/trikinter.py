import tkinter as tk
import sqlite3
from tkinter import messagebox

# Parameter nya tergantung isi dari content 
def simpan_data_ke_sqlLite(nilai1, nilai2, prodi_terpilih):
    # Connect Database
    con = sqlite3.connect("kelasB.db")
    cursore = con.cursor()

    # Membuat Table jika Table belum di buat
    cursore.execute('''CREATE TABLE IF NOT EXISTS hasil_prediksi 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nilai1 INTEGER,
                    nilai2 INTEGER,
                    namaMhs TEXT)''')
    
    # Insert Data kedalam Table hasil_prediksi
    cursore.execute('''INSERT INTO hasil_prediksi(nilai1,nilai2,namaMhs) VALUES (?,?,?)''', (nilai1,nilai2,prodi_terpilih))

    con.commit()
    con.close()


# Fungsi Untuk Menampilkan
def show():
    namaMhs = entry_mhs.get()
    matkul1 = entry_matkul1.get()
    matkul2 = entry_matkul2.get()

    hasilMhs = f"Nama Mahasiswa: {namaMhs}"
    hasil1 = f"Mata Kuliah 1: {matkul1}"
    hasil2 = f"Mata Kuliah 2: {matkul2}"

    label_hasilMhs.config(text=hasilMhs)
    label_hasil1.config(text=hasil1)
    label_hasil2.config(text=hasil2)

    if not matkul1 and not matkul2 and not namaMhs:
        frame_hasil.pack_forget()
    else:
        frame_hasil.pack()
        simpan_data_ke_sqlLite(matkul1,matkul2,namaMhs)
        messagebox.showinfo("Info","Data Tersimpan")





# Buat Jendela Halaman
root = tk.Tk()
root.title("Prediksi Prodi Pilihan")
root.geometry("500x500")
root.resizable(False,False)

# Label Judul
label_judul = tk.Label(root, text="Prediksi Prodi Pilihan", font=("Times",14,"bold"))
label_judul.pack(pady=20)

# Buat Frame inputan
frame_input = tk.LabelFrame(root, labelanchor="n",pady=10, padx=10)
frame_input.pack()


# Label Nama Mahasiswa
label_nama_mhs = tk.Label(frame_input, text="Nama Mahasiswa: ")
label_nama_mhs.grid(row=0, column=0, pady=10)
entry_mhs = tk.Entry(frame_input)
entry_mhs.grid(row=0,column=1)

# Label Nama Mata Kuliah 1
label_nama_matkul1 = tk.Label(frame_input, text="Nama Mata kuliah Matematika: ")
label_nama_matkul1.grid(row=1, column=0, pady=10)
entry_matkul1 = tk.Entry(frame_input)
entry_matkul1.grid(row=1,column=1)

# Label Nama Mata Kuliah 2
label_nama_matkul2 = tk.Label(frame_input, text="Nama Mata kuliah Kimia: ")
label_nama_matkul2.grid(row=2, column=0, pady=10)
entry_matkul2 = tk.Entry(frame_input)
entry_matkul2.grid(row=2,column=1)

# Tombol Hasil
btn_hasil = tk.Button(root, text="Submit", command=show)
btn_hasil.pack(pady=10)

frame_hasil = tk.LabelFrame(root,labelanchor="n", padx=10,pady=10)
frame_hasil.pack_forget()

# Label Hasil
label_hasilMhs = tk.Label(frame_hasil, text="")
label_hasilMhs.pack()

label_hasil1 =  tk.Label(frame_hasil,text="")
label_hasil1.pack()

label_hasil2 =  tk.Label(frame_hasil,text="")
label_hasil2.pack()

# Jalankan Aplikasi
root.mainloop()