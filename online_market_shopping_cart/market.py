import os

class Market:
    def __init__(self):
        self.file_name = "product.txt"
        if not os.path.exists(self.file_name):
            open(self.file_name, 'w').close()

    def __del__(self):
        print("Market nesnesi sonlandırıldı ve dosya kapatıldı.")
    
    def list_product(self):
        with open(self.file_name, 'r') as file:
            lines = file.readlines()
            if not lines:
                print("Ürün listesi boş.")
                return
            print("Ürünler:")
            for line in lines:
                name, category, price, stock = line.strip().split(',')
                print(f"Ad: {name}, Kategori: {category}, Fiyat: {price}, Stok: {stock}")

    def add_product(self):
        name = input("Ürün adı: ")
        category = input("Kategori: ")
        price = input("Fiyat: ")
        stock = input("Stok miktarı: ")
        new_product = f"{name},{category},{price},{stock}\n"
        with open(self.file_name, 'a') as file:
            file.write(new_product)
        print("Ürün başarıyla eklendi.")

    def delete_product(self):
        product_name = input("Silinecek ürün adı: ")
        with open(self.file_name, 'r') as file:
            lines = file.readlines()
        updated_lines = [line for line in lines if not line.startswith(product_name)]
        if len(updated_lines) == len(lines):
            print("Ürün bulunamadı.")
        else:
            with open(self.file_name, 'w') as file:
                file.writelines(updated_lines)
            print("Ürün başarıyla silindi.")
