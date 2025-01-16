from market import Market

def menu():
    market = Market()
    while True:
        print("\n*** MENÜ ***")
        print("1) Ürünleri Listele")
        print("2) Ürün Ekle")
        print("3) Ürün Sil")
        print("4) Çıkış")
        choice = input("Seçiminizi yapın: ")
        
        if choice == '1':
            market.list_product()
        elif choice == '2':
            market.add_product()
        elif choice == '3':
            market.delete_product()
        elif choice == '4':
            print("Programdan çıkılıyor.")
            del market
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    menu()
