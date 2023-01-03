#kisiler isimli bos bir liste olusturdum.
kisiler = []
#kullanicidan bir isim girilmesi istenir.
x = input("isim giriniz:")
#kullanicidan alinan bir isim eklenir.
kisiler.append(x)
#kullaniciden alinan isim listeye eklenip yazilir.
print(kisiler)
#kullanicidan bir isim girilmesi istenir.
y = input("isim giriniz:")
#kullanicidan alinan bir isim eklenir.
kisiler.append(y)
#kullaniciden alinan isim listeye eklenip yazilir.
print(kisiler)
#kullanicidan bir isim girilmesi istenir.
z = input("isim giriniz:")
#kullanicidan alinan bir isim eklenir.
kisiler.append(z)
#kullaniciden alinan isim listeye eklenip yazilir.
print(kisiler)
#kullanicidan bir isim girilmesi istenir.
p = input("isim giriniz:")
#kullanicidan alinan bir isim eklenir.
kisiler.append(p)
#kullaniciden alinan isim listeye eklenip yazilir.
print(kisiler)
#kisiler adli listenin kac elemanli oldugu belirlemeye yarar.
uzunluk = len(kisiler)
#kisiler adli listenin kac elemanli oldugu ekrana yazilir.
print("listenin uzunlugu=",uzunluk)
#listenin ikinci elemani nedir belirleyip ekrana yazdirir.
print("istenilen kisi:",kisiler[1])
#kisiler listesinin son elemanini silmeye yarar.
kisiler.pop(-1)
#kisiler listesinin son elemanini silip ekrana yazdirir.
print("silindikten sonra:",kisiler)
#kisiler listesinin ekrana yazdirilmasini saglanir.
print("yenilenmis son hal kisilerin siralamis hali:",kisiler)