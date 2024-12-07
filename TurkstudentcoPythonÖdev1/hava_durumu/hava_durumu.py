class Sehir:
    def __init__(self, ad, sicaklik):
        self.ad = ad
        self.sicaklik = sicaklik

    def __str__(self):
        return f"{self.ad} - {self.sicaklik}°C"


class HavaDurumu:
    def __init__(self):
        self.sehirler = []

    def sehir_ekle(self, ad, sicaklik):
        self.sehirler.append(Sehir(ad, sicaklik))

    def sicaklik_sorgula(self, ad):
        for sehir in self.sehirler:
            if sehir.ad.lower() == ad.lower():
                return sehir.sicaklik
        return None

    def tavsiye_ver(self, sicaklik):
        if sicaklik < 0:
            return "Soğuk, sıkı giyinin."
        elif 0 <= sicaklik < 15:
            return "Serin, mont almayı unutmayın."
        else:
            return "Hava güzel, rahat giyin."

    def listele(self):
        print("\nKayıtlı Şehirler ve Sıcaklıklar:")
        for sehir in self.sehirler:
            print(sehir)


def main():
    hava = HavaDurumu()
    while True:
        print("\n1. Şehir Ekle\n2. Hava Durumu Sorgula\n3. Şehirleri Listele\n4. Çıkış")
        choice = input("Seçiminiz: ")
        if choice == "1":
            ad = input("Şehir adı: ")
            sicaklik = float(input("Sıcaklık (°C): "))
            hava.sehir_ekle(ad, sicaklik)
        elif choice == "2":
            ad = input("Sorgulamak istediğiniz şehir: ")
            sicaklik = hava.sicaklik_sorgula(ad)
            if sicaklik is not None:
                print(f"{ad} için sıcaklık: {sicaklik}°C")
                print(hava.tavsiye_ver(sicaklik))
            else:
                print("Şehir bulunamadı!")
        elif choice == "3":
            hava.listele()
        elif choice == "4":
            print("Çıkış yapılıyor.")
            break
        else:
            print("Geçersiz seçim!")


if __name__ == "__main__":
    main()
