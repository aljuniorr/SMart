from tabulate import tabulate

listBarang = [
    {
        'nama': 'Beras',
        'satuan': 'Kilogram',
        'stok': 20,
        'harga': 10000
    },
    {
        'nama': 'Garam',
        'satuan': 'Ons',
        'stok': 15,
        'harga': 5000
    },
    {
        'nama': 'Minyak',
        'satuan': 'Liter',
        'stok': 25,
        'harga': 15000
    },
    {
        'nama': 'Bayam',
        'satuan': 'Ikat',
        'stok': 20,
        'harga': 3000
    }
]

cart = []

def tampilkan_daftar_barang():
    table = []
    for i, barang in enumerate(listBarang):
        table.append([i+1, barang['nama'], barang['satuan'], barang['stok'], barang['harga']])
    print('\t\tDaftar Barang')
    print(tabulate(table, headers=['No', 'Nama', 'Satuan', 'Stok', 'Harga'], tablefmt='grid'))

def tampilkan_cart():
    table = []
    for item in cart:
        table.append([item['nama'], item['qty'], item['harga'], item['qty'] * item['harga']])
    print('\nCart Barang:')
    print(tabulate(table, headers=['Nama', 'Qty', 'Harga', 'Total Harga'], tablefmt='grid'))

def tambah_barang():
    namaBarang = input('Masukkan Nama Barang : ').capitalize()
    satuanBarang = input('Masukan Satuan Barang : ').capitalize()
    stokBarang = int(input('Masukkan Stok Barang : '))
    hargaBarang = int(input('Masukkan Harga Barang : '))
    print('')
    listBarang.append({
        'nama': namaBarang,
        'satuan': satuanBarang,
        'stok': stokBarang,
        'harga': hargaBarang
    })
    tampilkan_daftar_barang()

def hapus_barang():
    tampilkan_daftar_barang()
    nomorBarang = int(input('Masukkan Nomor Barang Yang Ingin Dihapus : ')) - 1
    del listBarang[nomorBarang]
    tampilkan_daftar_barang()

def edit_barang():
    tampilkan_daftar_barang()
    nomorBarang = int(input('Masukkan Nomor Barang Yang Ingin Diubah : ')) - 1
    if 0 <= nomorBarang < len(listBarang):
        barang = listBarang[nomorBarang]
        print('Barang Yang Diubah : {}'.format(barang['nama']))
        barang['nama'] = input('Masukkan Nama Barang Baru : ').capitalize()
        barang['satuan'] = input('Masukan Satuan Barang Baru : ').capitalize()
        barang['stok'] = int(input('Masukkan Stok Barang Baru : '))
        barang['harga'] = int(input('Masukkan Harga Barang Baru : '))
        print('Barang telah berhasil diubah!')
        tampilkan_daftar_barang()
    else:
        print('Nomor Barang Tidak Valid')

def beli_barang():
    tampilkan_daftar_barang()
    while True:
        nomorBarang = int(input('Masukkan Nomor Barang Yang Ingin Dibeli : ')) - 1
        if 0 <= nomorBarang < len(listBarang):
            qtyBarang = int(input('Masukkan Jumlah Yang Ingin Dibeli : '))
            if qtyBarang > listBarang[nomorBarang]['stok']:
                print('Stok Tidak Cukup, Stok {} Tinggal {}'.format(listBarang[nomorBarang]['nama'], listBarang[nomorBarang]['stok']))
            else:
                cart.append({
                    'nama': listBarang[nomorBarang]['nama'],
                    'qty': qtyBarang,
                    'harga': listBarang[nomorBarang]['harga'],
                    'nomor': nomorBarang
                })
            tampilkan_cart()
            checker = input('Mau Beli Yang Lain? (Ya/Tidak) = ').lower()
            if checker == 'tidak':
                break
        else:
            print('Nomor Barang Tidak Valid')

    print('\nDaftar Belanja :')
    print('Nama\t| Qty\t| Harga\t| Total Harga')
    totalHarga = 0
    for item in cart:
        print('{}\t| {}\t| {}\t| {}'.format(item['nama'], item['qty'], item['harga'], item['qty'] * item['harga']))
        totalHarga += item['qty'] * item['harga']
    while True:
        print('------------------------------------------- \nTotal Yang Harus Dibayar : {}'.format(totalHarga))
        jmlUang = int(input('Masukkan Jumlah Uang : '))
        if jmlUang > totalHarga:
            kembali = jmlUang - totalHarga
            print('Uang Kembali Anda : {}'.format(kembali))
            print('\nTerima kasih Sudah Belanja Di SMart, Sampai Jumpa!')
            for item in cart:
                listBarang[item['nomor']]['stok'] -= item['qty']
            cart.clear()
            break
        elif jmlUang == totalHarga:
            print('\nTerima kasih Sudah Belanja Di SMart, Sampai Jumpa!')
            for item in cart:
                listBarang[item['nomor']]['stok'] -= item['qty']
            cart.clear()
            break
        else:
            kekurangan = totalHarga - jmlUang
            print('Uang Anda Kurang Sebesar {}'.format(kekurangan))

def main():
    while True:
        pilihanMenu = input('''
=============================================
          Selamat Datang di SMart
    Tempat Terbaik Untuk Belanja Sembako
=============================================
    Menu 1 : Tampilkan Barang Sembako
    Menu 2 : Tambah Barang Sembako
    Menu 3 : Hapus Data Barang Sembako
    Menu 4 : Ubah Data Barang Sembako
    Menu 5 : Beli Barang Sembako
    Menu 6 : Keluar
                            
Masukkan angka Menu yang ingin dijalankan : ''')
        print('')

        if pilihanMenu == '1':
            tampilkan_daftar_barang()
        elif pilihanMenu == '2':
            tambah_barang()
        elif pilihanMenu == '3':
            hapus_barang()
        elif pilihanMenu == '4':
            edit_barang()
        elif pilihanMenu == '5':
            beli_barang()
        elif pilihanMenu == '6':
            break

if __name__ == '__main__':
    main()