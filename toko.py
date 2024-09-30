class Barang: #kelas utama/superclass
    def __init__(self, sku, nama, harga):
        self.sku = sku #invoke = memasukan nilai
        self.nama = nama
        self.harga = harga

class Stock(Barang): #inheritance, subclass "Barang"
    def __init__(self, sku, nama, harga, stok):
        super().__init__(sku, nama, harga) #super = merujuk ke/memanggil superclass aka barang
        self.stok = stok
    def tambah_stok(self, jumlah):
        self.stok += jumlah
        print(f'{jumlah} Unit  {self.nama} ditambahkan. stok sekarang: {self.stok}')
    def kurangi_stok(self, jumlah):
        if(jumlah <= self.stok):
            self.stok -= jumlah
            print(f'{jumlah} Unit  {self.nama} terjual. stok sekarang: {self.stok}')
        else:
            print(f'Stok tidak cukup untuk menjual {jumlah} unit {self.nama}')
    def detail(self):
        print(f'SKU \t: {self.sku}')
        print(f'NAMA \t: {self.nama}')
        print(f'HARGA \t: {self.harga}')
        print(f'STOK \t: {self.stok}')
        print('------')


class Transaksi: #polimorphishm
    def penjualan(self, barang, jumlah_beli):
        if(jumlah_beli <= barang.stok):
            total_harga = jumlah_beli * barang.harga
            barang.kurangi_stok(jumlah_beli)
            print(f'Penjualan {jumlah_beli} unit {barang.nama} seharga {total_harga} berhasil.')
        else:
            print(f'Penjualan {jumlah_beli} unit barang {barang.nama} gagal, karena stok tidak cukup.')


#Inisialisasi data barang 
barang_1 = Stock('00001', 'Gelas', 3000, 5) 
barang_2 = Stock('00002', 'Piring', 4600, 3)
barang_3 = Stock('00003', 'Mangkuk', 8000, 3)
barang_4 = Stock('00004', 'Tumbler', 20000, 3)

#Inisialisasi Class Transaksi
transaksi = Transaksi()

#Cetak Detail Barang
barang_1.detail()
barang_2.detail()
barang_3.detail()
barang_4.detail()

#Operasi penambahan stok barang
print('Operasi Tambah Barang :')
barang_1.tambah_stok(10)
print('')
print('Operasi Pembelian Barang Cukup Stok :')
transaksi.penjualan(barang_1, 5)
print('')
print('Operasi Pembelian Barang Tidak Cukup Stok :')
transaksi.penjualan(barang_2, 25)