from datetime import datetime
import time
import json
import os

class Node:
    def __init__(self, name, tipe, mdtime=datetime.now().strftime("%d/%m/%Y %H:%M %p")):
        self.name = name
        self.tipe = tipe
        self.modtime = mdtime
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

# Mengubah metode akses json 
script_dir = os.path.dirname(os.path.abspath(__file__))
nama_file = os.path.join(script_dir, "dataMemori.json")

def json_to_node(data, parent=None):
        if data:
            node = Node(data['name'], data['tipe'], data['modtime'])
            node.parent = parent
            for child_data in data.get('children', []):
                node.children.append(json_to_node(child_data, node))
            return node


def bacaData(nama_file):
            with open(nama_file, "r", encoding="utf-8") as f:
                data_dict = json.load(f)
            return json_to_node(data_dict)

class DirectoryTree:
    def __init__(self):
        self.root = bacaData(nama_file)
        self.current = self.root
        self.history = stack()

    def cek_current(self):
        return self.current.name

    # Fungsi Untuk menambah folder
    def tambah(self):
        print("\n===Pilih tipe===")
        print("[1] FOLDER")
        print("[2] FILE")

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
        if tipe not in ["Folder", "File"]:
            print("Tipe harus 'folder' atau 'file'")
            return
        def inputnama():
            while True:
                nama = input(f"Masukan nama {tipe}: ")
                nama_terpakai = False
                
                for child in self.current.children:
                    if child.name == nama:
                        print("Nama sudah digunakan!, Silahkan masukan ulang")
                        nama_terpakai = True
                if not nama_terpakai:
                    return nama
        # Cek apakah nama file/folder sudah digunakan
        nama = inputnama()

        modtime = datetime.now().strftime("%d/%m/%Y %H:%M %p")

        # simpan dengan nama,tipe Folder/File
        node = Node(nama, tipe, modtime)
        node.children = []
        node.parent = self.current
        self.current.children.append(node)
        print(f"{tipe} berhasil dibuat.")

    # Fitur menampilkan child(jika current bertipe folder)
    def tampilan(self):
        if not self.current.children:
            print("Folder kosong")
            return
        # garis = "│   " * level + "├──"
        sorted_children = sorted(self.current.children, key=lambda x: x.name.lower())
        print(f"===Isi Folder {self.current.name}===")
        for child in sorted_children:
            print(f"[{"📄" if child.tipe.upper() == "FILE" else "📁"}] {child.name.ljust(25) if len(child.name) < 25 else child.name[:22] + '...'} {child.modtime}")

    def ubah_nama(self, nama_lama, nama_baru):
        
        cek = False
        for child in self.current.children:
            if child.name == nama_baru:
                print("Nama sudah digunakan!")
                return

        for child in self.current.children:
            if child.name == nama_lama:
                child.name = nama_baru
                print("Berhasil mengganti nama.")
                child.modtime = datetime.now().strftime("%d/%m/%Y %H:%M %p")
                cek = True
        if not cek:
            print("Folder/file tidak ditemukan")

    def hapus(self):
        if not self.current.children:
            print("Folder kosong")
            return
        sorted_children = sorted(self.current.children, key=lambda x: x.name.lower())
        print(f"===Isi Folder {self.current.name}===")
        for child in sorted_children:
            print(f"[{"📄" if child.tipe.upper() == "FILE" else "📁"}] {child.name.ljust(25) if len(child.name) < 25 else child.name[:22] + '...'} {child.modtime}")
        nama = input("Masukan Nama yang ingin dihapus: ")
        for child in self.current.children:
            if child.name == nama:
                self.current.children.remove(child)
                print("Berhasil dihapus")
                return
        print("Folder/File tidak ditemukan.")

    def cari(self, node, keyword):
        if not node:
            return

        # Validasi keyword agar case insensitive
        if keyword.lower() in node.name.lower():
            parent_path = []
            parent_node = node.parent
            while parent_node:
                parent_path.append(parent_node.name)
                parent_node = parent_node.parent
            print("Ditemukan:", f"{node.name} [Path: {('/'.join(reversed(parent_path)))}/{node.name}]")

        for child in node.children:
            self.cari(child, keyword)

    def masuk(self):
        if not self.current.children:
            print("Folder kosong")
            return
        sorted_children = sorted(self.current.children, key=lambda x: x.name.lower())
        print(f"===Isi Folder {self.current.name}===")
        for child in sorted_children:
            print(f"[{"📄" if child.tipe.upper() == "FILE" else "📁"}] {child.name.ljust(25) if len(child.name) < 25 else child.name[:22] + '...'} {child.modtime}")
        nama = input("Masuk: ")
        if self.current.children:
            for child in self.current.children:
                if child.name == nama and child.tipe == "Folder":
                    self.history.push(self.current)
                    self.current = child
                    return
                elif child.name == nama and child.tipe == "File":
                     print("Tidak bisa masuk ke file!")
                     return
        print("Folder tidak ditemukan.")

    def cek_child(self):
        print("\n", "Path: ", self.path())
        print("\n====Daftar Folder====")
        for child in self.current.children:
            if child.tipe == 'Folder':
                print(f'[📁] {child.name}')
    
    def cek_all_child(self):
        print("\n", "Path: ", self.path())
        print("\n====Daftar Folder====")

        for child in self.current.children:
            print(f'[{ "📄" if child.tipe.upper() == "FILE" else "📁" }] {child.name}')


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

    def node_ke_dict(self, node):
        data = {
            "name" : node.name,
            "tipe" : node.tipe,
            "modtime" : node.modtime,
            "children" : [self.node_ke_dict(child) for child in node.children]
        }
        if node.parent is not None:
            data["parent"] = node.parent.name

        return data

    def simpan_json(self, filename):
        data_dict = self.node_ke_dict(self.root)

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data_dict, f, indent=4)
        print("Berhasil simpan data")
    
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
        print("8. Simpan ke Json")
        print("9. Keluar")
        print("=====================================")
        pilihan = input("Pilih: ")

        if pilihan == "1":
            tree.tambah()

        elif pilihan == "2":
            tree.tampilan()

        elif pilihan == "3":
            tree.masuk()

        elif pilihan == "4":
            tree.cek_all_child()
            print()
            lama = input("Nama yang ingin diubah: ")
            baru = input("Nama baru: ")
            tree.ubah_nama(lama, baru)

        elif pilihan == "5":
            tree.hapus()

        elif pilihan == "6":
            keyword = input("Masukkan kata kunci: ")
            tree.cari(tree.root, keyword)

        elif pilihan == "7":
            tree.kembali()

        elif pilihan == "8":
            tree.simpan_json(nama_file)

        elif pilihan == "9":
            print("Keluar dari program.")
            break

        else:
            print("Input tidak valid!")
        
        time.sleep(2)

if __name__ == "__main__":
    main()