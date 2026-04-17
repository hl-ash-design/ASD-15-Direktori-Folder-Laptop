class Node:
    def __init__(self, name, tipe):
        self.name = name
        self.tipe = tipe
        self.children = []
        self.parent = None

class stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if self.data:
            return self.data.pop()
        return None
    
    def is_empty(self):
        return len(self.data) == 0


class DirectoryTree:
    def __init__(self):
        self.root = Node("Home","Folder")
        self.current = self.root
        self.history = stack()

    def cek_current(self):
        return self.current.name
    # Fungsi Untuk menambah folder
    def tambah(self):
        print("\n===Pilih tipe===")
        print("[FOLDER]")
        print("[FILE]")
        def inputTipe():
            while True:
                pilihan = input("Pilih tipe (1/2): ")
                if pilihan == "1":
                    return "Folder"
                elif pilihan == "2":
                    return "File"
                else:
                    print("Tipe salah. Silahkan input ulang") 
        tipe = inputTipe()
        # Cek input tipe, apakah Folder atau bukan
        if tipe not in ["Folder","File"]:
            print("Tipe harus 'folder' atau 'file'")
            return
        nama = input(f"Masukan nama {tipe}: ")
        # Cek apakah nama file/folder sudah digunakan
        for child in self.current.children:
            if child.name == nama:
                print("Nama sudah digunakan!")
                return
        
        # simpan dengan nama,tipe Folder/File
        node = Node(nama, tipe)
        node.parent = self.current
        self.current.children.append(node)
        print(f"{tipe} berhasil dibuat.")

    # Fitur menampilkan child(jika current bertipe folder)
    def tampilan(self):
        if not self.current.children:
            print("Folder kosong")
            return
        
        sorted_children = sorted(self.current.children, key=lambda x: x.name.lower())

        for child in sorted_children:
            print(f"[{child.tipe.upper()}] {child.name}")

    def ubah_nama(self, nama_lama, nama_baru):
        for child in self.current.children:
            if child.name == nama_lama:
                child.name = nama_baru
                print("Berhasil mengganti nama.")
        print("Folder/file tidak ditemukan")
        
    def hapus(self, nama):
        for child in self.current.children:
            if child.name == nama:
                self.current.children.remove(child)
                print("Berhasil dihapus")
                return
        print("Folder/File tidak ditemukan.")

    def cari(self, node, keyword):
        if keyword.lower() in node.name.lower():
            print("Ditemukan:", node.name)
            
        for child in node.children:
            self.cari(child, keyword)

    def masuk(self, nama):
        for child in self.current.children:
            if child.name == nama and child.tipe =="Folder":
                self.history.push(self.current)
                self.current = child
                return 
        print("Folder tidak ditemukan.")
        
    def cek_child(self):
        print('\n', 'Path: ',self.path())
        print("\n====Daftar Folder====")
        for child in self.current.children:
            if child.tipe == 'Folder':
                print(f'[{child.tipe}] {child.name}')
    
    def kembali(self):
        prev = self.history.pop()
        if prev:
            self.current = prev
        else:
            print("Sudah di root")

    def path(self):
        node = self.current
        path_list = []
        while node:
            path_list.append(node.name)
            node = node.parent
        return "/".join(reversed(path_list))
    
def main():
    tree = DirectoryTree()

    while True:
        print("\nPath:", tree.path())
        print("\nMenu:")
        print("1. Buat Folder/file")
        print("2. Lihat Isi Folder", tree.cek_current())
        print("3. Masuk ke Folder")
        print("4. Ganti Nama ")
        print("5. Hapus File/Folder")
        print("6. Cari File/Folder")
        print("7. Kambali")
        print("8. Keluar")

        pilihan = input("Pilih: ")

        if pilihan == "1":
            tree.tambah()

        elif pilihan == "2":
            tree.tampilan()

        elif pilihan == "3":
            tree.cek_child()
            nama = input("Masuk: ")
            tree.masuk(nama)

        elif pilihan == "4":
            tree.cek_child()
            lama = input("Nama yang ingin diubah: ")
            baru = input("Nama baru: ")
            tree.ubah_nama(lama, baru)

        elif pilihan == "5":
            nama = input("Masukan nama yang ingin dihapus: ")
            tree.hapus(nama)

        elif pilihan == "6":
            keyword = input("Masukkan kata kunci: ")
            tree.cari(tree.root, keyword)

        elif pilihan == "7":
            tree.kembali()

        elif pilihan == "8":
            print("Keluar dari program.")
            break

        else:
            print("Input tidak valid!")

if __name__ == "__main__":
    main()