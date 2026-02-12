## TEGAR RIDWAN

import tkinter as tk
from tkinter import BOTH, LEFT, Button, messagebox as mb
import hashlib
from tkinter.ttk import Label
import mysql.connector
import os

folder = os.path.dirname(__file__)

main_app = None

def GetConnection():
    return mysql.connector.connect(
        host='localhost',
        db='db_vending',
        user='root',
        password='',
        port=3306
    )

# pop up edit
def edit_barang(id, nama_lama, harga_lama, file_lama, dashboard):
    edit_popup = tk.Toplevel(dashboard)
    edit_popup.title("Edit Barang")
    edit_popup.geometry("300x300")
    edit_popup.grab_set()

    frData = tk.Frame(edit_popup, padx=10, pady=10)
    frData.pack(fill='both', expand=True)

    #tempat input nama
    tk.Label(frData, text="Nama Barang Baru").grid(row=0, column=0, padx=5, pady=5, sticky='w')
    nama_entry = tk.Entry(frData, width=30)
    nama_entry.insert(0, nama_lama)
    nama_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frData, text="Barang Baru").grid(row=2, column=0, padx=5, pady=5, sticky='w')
    file_entry = tk.Entry(frData, width=30)
    file_entry.insert(0, file_lama)
    file_entry.grid(row=2, column=1, padx=5, pady=5)

    #tempat input harga
    tk.Label(frData, text="Harga Baru").grid(row=1, column=0, padx=5, pady=5, sticky='w')
    harga_entry = tk.Entry(frData, width=30)
    harga_entry.insert(0, harga_lama)
    harga_entry.grid(row=1, column=1, padx=5, pady=5)

    #fungsi simpan
    def simpan_barang():
        nama_baru = nama_entry.get()
        harga_baru = harga_entry.get()
        barang_baru = file_entry.get()
        
        if not nama_baru or not harga_baru.isdigit() or not barang_baru:
            mb.showwarning("input salah","nama dan harga tidak boleh kosong", parent=edit_popup)

        try:
            #update sql
            conn = GetConnection()
            cursor = conn.cursor()
            query = "UPDATE barang SET nama=%s, harga=%s, nama_file=%s WHERE id=%s"
            cursor.execute(query, (nama_baru, int(harga_baru), barang_baru, id))
            conn.commit()
            cursor.close()
            conn.close()

            mb.showinfo("Berhasil", "Data barang berhasil diperbarui.", parent=dashboard)
            edit_popup.destroy()

            dashboard.destroy()
            menu_dashboard()

        except mysql.connector.Error as err:
            mb.showerror("Error DB", f"Gagal memperbarui data: {err}", parent=edit_popup)
            
    #tombol
    frButton = tk.Frame(edit_popup)
    frButton.pack(pady=10)
    tk.Button(frButton, text="Simpan", command=simpan_barang).pack(side=tk.LEFT, padx=5)
    tk.Button(frButton, text="Batal", command=edit_popup.destroy).pack(side=tk.LEFT, padx=5)
                

def menu_dashboard():
    conn = GetConnection()
    query = "SELECT id, nama, harga, nama_file FROM barang"
    cursor = conn.cursor()
    cursor.execute(query)
    items = cursor.fetchall()
    cursor.close()
    conn.close()

    print(f"Jumlah item yang diambil dari DB: {len(items)}")
    print(f"Data Item: {items}")

    dashboard = tk.Toplevel()
    dashboard.title("Admin Page")
    dashboard.geometry("600x850")




    image_references = {}
    halaman_sekarang = [0] 

    #memuat gambar
    def layout_gambar(nama_file):
        path = os.path.join(folder, "Pict", nama_file)
        before = tk.PhotoImage(file=path)
        after = before.subsample(5, 5)
        return after
    
    
    # row_num = 0

    #frame untuk menampilkan barang
    item_frame = tk.Frame(dashboard)
    item_frame.pack(pady=10, padx=10, fill='x')

    #frame untuk navigasi
    nav_frame = tk.Frame(dashboard, bg="lightgray")
    nav_frame.pack(fill="x", padx=10, pady=10)

    label_page = tk.Label(nav_frame, text="PAGE")
    label_page.grid(row=0, column=1, padx=10)

    def tampilkan_halaman(nomor_halaman):
        #hapus widget lama
        for widget in item_frame.winfo_children():
            widget.destroy()


        #menghitung indeks
        items_per_page = 6
        indeks_awal = nomor_halaman * items_per_page
        indeks_akhir = indeks_awal + items_per_page
        halaman_items = items[indeks_awal:indeks_akhir]

        #menghitung halaman
        total_items = len(items)
        total_halaman = (total_items + items_per_page - 1 ) // items_per_page

        row_num = 0

        # nama = tk.Label(text="Nama Barang")
        # nama.grid(row=0, column=1, padx=5, pady=5)

        # harga = tk.Label(text="Harga Barang")
        # harga.grid(row=1, column=1, padx=5, pady=5)
     
        #menampilkan item
        for item_id, nama_barang, harga_barang, file_gambar in halaman_items:

         #ambil gambar
            if file_gambar:
                try :
                    img = layout_gambar(file_gambar) ##cek apakah file gambar ada
                except tk.TclError as e:
                    print(f"Error loading image for {nama_barang}: {e}")
                    img = None
                if img:
                    image_references[f"img_{item_id}"] = img
                 
                 #gambar
                    label_img = tk.Label(item_frame, image=img)
                    label_img.image = img
                    label_img.grid(row=row_num, column=0, padx=5, pady=5)
                 
                 #nama barang
                    label_nama = tk.Label(item_frame, text=nama_barang)
                    label_nama.grid(row=row_num, column=1, padx=5, pady=5)

                 #harga barang
                    label_harga = tk.Label(item_frame, text=f"Rp {harga_barang:,}".replace(",", "."))
                    label_harga.grid(row=row_num, column=2, padx=5, pady=5)

                 #tombol edit
                    btn_edit = tk.Button(item_frame, text="Edit", width=10, 
                                 command=lambda id=item_id, nama=nama_barang, harga=harga_barang, files=file_gambar, dash=dashboard: edit_barang(id, nama, harga, files, dash))
                    btn_edit.grid(row=row_num, column=3, padx=10, pady=5)

                    row_num += 1
        # total_halaman
        label_page.config(text=f"Halaman {nomor_halaman + 1} dari {total_halaman}")

    def prev_halaman():
        if halaman_sekarang[0] > 0:
            halaman_sekarang[0] -= 1
            tampilkan_halaman(halaman_sekarang[0])

    def next_halaman():
        items_per_page = 6
        total_items = len(items)
        total_halaman = (total_items + items_per_page - 1) // items_per_page
        if halaman_sekarang[0] < total_halaman - 1:
            halaman_sekarang[0] += 1
            tampilkan_halaman(halaman_sekarang[0])
                
    #tombol navigasi
    btn_prev = tk.Button(nav_frame, text="<", command=prev_halaman)
    btn_prev.grid(row=0, column=0, padx=10)

    btn_next = tk.Button(nav_frame, text=">", command=next_halaman)
    btn_next.grid(row=0, column=2, padx=10)

    #agar berada di tengah
    nav_frame.grid_columnconfigure(1, weight=1)

    tampilkan_halaman(0)
                

    dashboard.image_references = image_references


    #  label1 = tk.Label(dashboard, image=img_air)
    #  Label.image = img_air
    #  label1.grid(row=0,  padx=5, pady=5)

    #  nama1 = tk.Label(dashboard, text="Air Mineral")
    #  nama1.grid(row=0, column=1, padx=5, pady=5)
    #  harga1 = tk.Label(dashboard, text="5000")
    #  harga1.grid(row=1, column=1, padx=2, pady=2)

    #  label2 = tk.Label(dashboard, image=img_nescafe)
    #  label2.image = img_nescafe
    #  label2.grid(row=2, padx=5, pady=5)

    #  label3 = tk.Label(dashboard, image=img_pepsi)
    #  label3.image = img_pepsi
    #  label3.grid(row=3, padx=5, pady=5)

    #  label4 = tk.Label(dashboard, image=img_pillows)
    #  label4.image = img_pillows
    #  label4.grid(row=4,  padx=5, pady=5)

    #  label5 = tk.Label(dashboard, image=img_chikibalss)
    #  label5.image = img_chikibalss
    #  label5.grid(row=5,  padx=5, pady=5)

    #  label6 = tk.Label(dashboard, image=img_chitato)
    #  label6.image = img_chitato
    #  label6.grid(row=6,  padx=5, pady=5)

    #  label7 = tk.Label(dashboard, image=img_fanta)
    #  label7.image = img_fanta
    #  label7.grid(row=7,  padx=5, pady=5)

    #  label8 = tk.Label(dashboard, image=img_wallens)
    #  label8.image = img_wallens
    #  label8.grid(row=8,  padx=5, pady=5)

    #  label9 = tk.Label(dashboard, image=img_cheetos)
    #  label9.image = img_cheetos
    #  label9.grid(row=9,  padx=5, pady=5)

    def logout():
         root.username_entry.delete(0, tk.END)
         root.password_entry.delete(0, tk.END)
         root.username_entry.focus_set()
         dashboard.destroy()
         root.deiconify()
         mb.showinfo("Logout", "Anda telah logout dari sistem", parent=root)
    btn_logout = tk.Button(dashboard, text="Logout", command=logout)
    btn_logout.pack(pady=10)


def login():
    namaUser = root.username_entry.get()
    password = root.password_entry.get()
    if not namaUser:
         mb.showwarning("Login Gagal", "Username tidak boleh kosong", parent=root)
    elif not password:
         mb.showwarning("Login Gagal", "Password tidak boleh kosong", parent=root)
         return

    password = hashlib.md5(password.encode()).hexdigest()
    conn = GetConnection()
    query = "SELECT * FROM admin WHERE username=%s AND password=%s"
    cursor = conn.cursor()
    cursor.execute(query, (namaUser, password))
    result = cursor.fetchone()
    if  result:     
        mb.showinfo("Login Berhasil", "Selamat, login berhasil", parent=root)
        root.withdraw()
        menu_dashboard()
    else:
        mb.showwarning("Login Gagal", "Username atau password salah", parent=root)
        root.username_entry.focus_set()

def open_admin(parent):
    global root, main_app
    main_app = parent
    root = tk.Toplevel(parent)
    root.title("Sistem Admin")
    root.resizable(False, False)
    root.geometry("300x250")


    frameUtama = tk.Frame(root, bd=10)
    frameUtama.pack(fill='both', expand=True)

    frData = tk.Frame(frameUtama, bd=5)
    frData.pack(fill='both', expand=True)

    Label(frData, text="Username").grid(row=0, column=0, padx=10, pady=10)
    root.username_entry = tk.Entry(frData)
    root.username_entry.grid(row=0, column=1, padx=10, pady=10)

    Label(frData, text="Password").grid(row=1, column=0, padx=10, pady=10)
    root.password_entry = tk.Entry(frData, show="*")
    root.password_entry.grid(row=1, column=1, padx=10, pady=10)

    frButton = tk.Frame(frameUtama, bd=5)
    frButton.pack(fill='both', expand=True)

    root.btnBatal = Button(frButton, text="Batal", width=10, command=root.destroy)
    root.btnBatal.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
    root.btnLogin = Button(frButton, text="Login", width=10, command=login)
    root.btnLogin.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
