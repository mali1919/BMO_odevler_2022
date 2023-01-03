# sinav_sonuc isimli sözlük oluşturuluyor
sinav_sonuc = {
    "İsim": ["Ayşe K.", "Ahmet M.", "Nuri C.", "Nawar T.", "Suzan T.", "Ala B."],
    "Cinsiyet": ["K", "E", "E", "E", "K", "K"],
    "Vize": [80, 60, 77, 25, 36, 75],
    "Final": [90, 50, 53, 100, 98, 66],
    "Gecme_Notu":[]
}
# Fonksiyon tanımlanıyor
def yeni_kayit(isim, cinsiyet, vize, final):
  # Sözlüğe yeni kayıt ekleniyor
  sinav_sonuc["İsim"].append(isim)
  sinav_sonuc["Cinsiyet"].append(cinsiyet)
  sinav_sonuc["Vize"].append(vize)
  sinav_sonuc["Final"].append(final)
  # Geçme notu hesaplanıyor ve sözlüğe ekleniyor
  gecme_notu = (vize * 0.3) + (final * 0.7)
  sinav_sonuc["Gecme_Notu"].append(gecme_notu)
# Kullanıcıdan 2 yeni kayıt girişi isteniyor
for i in range(2):
  isim = input("Öğrencinin ismi: ")
  cinsiyet = input("Öğrencinin cinsiyeti (K/E): ")
  vize = int(input("Öğrencinin vize notu: "))
  final = int(input("Öğrencinin final notu: "))
  
  # Girdiği bilgilerle yeni kayıt ekleniyor
  yeni_kayit(isim, cinsiyet, vize, final)
  
  # Güncellenmiş sözlük ekrana yazdırılıyor

print(sinav_sonuc)