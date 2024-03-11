class BukuNode:
    def __init__(self, buku):
        self.buku = buku
        self.next = None

class LinkedListBuku:
    def __init__(self):
        self.head = None

    def tambah_buku(self, buku):
        new_node = BukuNode(buku)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def hapus_buku(self, judul):
        if not self.head:
            print("Daftar buku kosong.")
            return
        if self.head.buku.nama == judul:
            self.head = self.head.next
            return
        prev_node = self.head
        current_node = self.head.next
        while current_node:
            if current_node.buku.nama == judul:
                prev_node.next = current_node.next
                return
            prev_node = current_node
            current_node = current_node.next
        print("Buku tidak ditemukan dalam daftar.")

    def tampilkan_daftar_buku(self):
        if not self.head:
            print("Daftar buku kosong.")
            return
        current_node = self.head
        while current_node:
            current_node.buku.display_info()
            current_node = current_node.next
        
    def quicksort(self, head):
        if head is None or head.next is None:
            return head

        pivot = head
        smaller_head = None
        equal_head = pivot
        larger_head = None
        current = head.next

        while current is not None:
            next_node = current.next
            if current.buku.nama < pivot.buku.nama:
                current.next = smaller_head
                smaller_head = current
            elif current.buku.nama == pivot.buku.nama:
                current.next = equal_head
                equal_head = current
            else:
                current.next = larger_head
                larger_head = current
            current = next_node

        smaller_head = self.quicksort(smaller_head)
        larger_head = self.quicksort(larger_head)

        if smaller_head is not None:
            temp = smaller_head
            while temp.next is not None:
                temp = temp.next
            temp.next = equal_head
        else:
            smaller_head = equal_head

        pivot.next = larger_head if larger_head is not None else None
        return smaller_head

    def sort_ascening(self):
        self.head = self.quicksort(self.head)

    def sort_descending(self):
        self.sort_ascening()
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sort_stok_ascening(self):
        self.head = self.quicksort_stok(self.head, reverse=False)

    def sort_stok_descending(self):
        self.head = self.quicksort_stok(self.head, reverse=True)

    def quicksort_stok(self, head, reverse=False):
        if head is None or head.next is None:
            return head

        pivot = head
        smaller_head = None
        equal_head = pivot
        larger_head = None
        current = head.next

        while current is not None:
            next_node = current.next
            if (not reverse and current.buku.stok < pivot.buku.stok) or (reverse and current.buku.stok > pivot.buku.stok):
                current.next = smaller_head
                smaller_head = current
            elif current.buku.stok == pivot.buku.stok:
                current.next = equal_head
                equal_head = current
            else:
                current.next = larger_head
                larger_head = current
            current = next_node

        smaller_head = self.quicksort_stok(smaller_head, reverse)
        larger_head = self.quicksort_stok(larger_head, reverse)

        if smaller_head is not None:
            temp = smaller_head
            while temp.next is not None:
                temp = temp.next
            temp.next = equal_head
        else:
            smaller_head = equal_head

        pivot.next = larger_head if larger_head is not None else None
        return smaller_head

class Buku:
    def __init__(self, nama, penerbit, stok, rak, tanggal_terbit):
        self.nama = nama
        self.penerbit = penerbit
        self.stok = stok
        self.rak = rak
        self.tanggal_terbit = tanggal_terbit

    def display_info(self):
        print(f"Nama Buku: {self.nama}")
        print(f"Penerbit: {self.penerbit}")
        print(f"Stok: {self.stok}")
        print(f"Rak: {self.rak}")
        print(f"Tanggal Terbit: {self.tanggal_terbit}")
        print()
        
class Perpustakaan:
    def __init__(self, nama, alamat):
        self.nama = nama
        self.alamat = alamat
        self.daftar_buku = LinkedListBuku()

    def tambah_buku(self, buku):
        self.daftar_buku.tambah_buku(buku)
        print(f"Buku dengan judul '{buku.nama}' berhasil ditambahkan.")

    def hapus_buku(self, judul):
        self.daftar_buku.hapus_buku(judul)

    def tampilkan_daftar_buku(self):
        print("Daftar Buku:")
        self.daftar_buku.tampilkan_daftar_buku()

    def pinjam_buku(self, judul):
        current_node = self.daftar_buku.head
        while current_node:
            if current_node.buku.nama == judul:
                if current_node.buku.stok > 0:
                    current_node.buku.stok -= 1
                    print(f"Anda berhasil meminjam buku '{judul}'.")
                    return
                else:
                    print("Maaf, stok buku habis.")
                    return
            current_node = current_node.next
        print("Buku tidak tersedia untuk dipinjam.")



perpustakaan1 = Perpustakaan("Perpustakaan Kota", "Jl. Kusuma bangsa")

perpustakaan1.tambah_buku(Buku("Ordeal", "Webtoon", 5, "Rak 1", "13/08/2021"))
perpustakaan1.tambah_buku(Buku("The Extincts", "Bhuana Sastra", 3, "Rak 2", "05/03/2013"))
perpustakaan1.tambah_buku(Buku("Laut Bercerita", "Kepustakaan Populer Gramedia", 7, "Rak 3", "10/07/2017"))

while True:
    print("Menu:")
    print("1. Tambah Buku")
    print("2. Hapus Buku")
    print("3. Tampilkan Daftar Buku")
    print("4. Pinjam Buku")
    print("5. Keluar")
    pilihan = input("Pilih menu (1/2/3/4/5): ")

    if pilihan == "1":
        nama_buku = input("Masukkan nama buku yang ingin ditambahkan: ")
        penerbit = input("Masukkan penerbit buku: ")
        stok = int(input("Masukkan jumlah stok buku: "))
        rak = input("Masukkan lokasi rak buku: ")
        tanggal_terbit = input("Masukkan tanggal terbit buku (dd/mm/yyyy): ")
        perpustakaan1.tambah_buku(Buku(nama_buku, penerbit, stok, rak, tanggal_terbit))
    elif pilihan == "2":
        judul_buku = input("Masukkan nama buku yang ingin dihapus: ")
        perpustakaan1.hapus_buku(judul_buku)
    elif pilihan == "3":
        print("1. ascending judul")
        print("2. descending judul")
        print("3. ascending stock")
        print("4. descending stock")
        milih =  input("Pilih Menu : ")
        if  milih == '1':
            perpustakaan1.daftar_buku.sort_ascening()
            perpustakaan1.tampilkan_daftar_buku()
        elif milih == "2":
            perpustakaan1.daftar_buku.sort_descending()
            perpustakaan1.tampilkan_daftar_buku()
        elif milih == "3":
            perpustakaan1.daftar_buku.sort_stok_ascening()
            perpustakaan1.tampilkan_daftar_buku()
        elif milih == "4":
            perpustakaan1.daftar_buku.sort_stok_descending()
            perpustakaan1.tampilkan_daftar_buku()
        else:
            print("tidak ada")
    elif pilihan == "4":
        judul_buku = input("Masukkan nama buku yang ingin dipinjam: ")
        perpustakaan1.pinjam_buku(judul_buku)
    elif pilihan == "5":
        print("Terima kasih telah menggunakan layanan perpustakaan.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang sesuai.")