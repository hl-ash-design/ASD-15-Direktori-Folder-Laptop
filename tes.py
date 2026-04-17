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

    def tambah(self, nama, tipe):
        if tipe not in ["Folder","File"]:
            print("Tipe harus 'folder' atau 'file'")
            return
        
        for child in self.current.children:
            if child.name == nama:
                print("Nama sudah digunakan!")
                return
            
        node = Node(nama, tipe)
        node.parent = self.current
        self.current.children.append(node)
        print(f"{tipe} berhasil dibuat.")

    def tampilan(self):
        if not self.current.children:
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
        print("1. Tambah Folder/file")
        print("2. Lihat isi folder")
        print("3. Masuk folder")
        print("4. Ganti nama")
        print("5. Hapus")
        print("6. Cari")
        print("7. Kambali")
        print("8. Keluar")

        pilihan = input("Pilih: ")

        if pilihan == "1":
            nama = input("Nama: ")
            tipe = input("Tipe (Folder/File): ")
            tree.tambah(nama, tipe)

        elif pilihan == "2":
            tree.tampilan()

        elif pilihan == "3":
            nama = input("Masuk: ")
            tree.masuk(nama)

        elif pilihan == "4":
            lama = input("Nama lama: ")
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