#sinav_sonuc isimli bir sozluk acilarak isim ,cinsiyet, matematik notu,turkce notu listeleri olusturulur.
sinav_sonuc = {'isimler':['Ayse K.' ,'Ahmet M.','Nuri C.','Nawar T. ','Suzan T. ','Ala B.'],
'cinsiyet' : ['K', 'E', 'E', 'E', 'K', 'K'], 
'Matematik' : [80,60,77,25,36,75],
'Turkce' : [90,50,53,100,98,66]}
#kadinlarin ve erkeklerin Turkce notunu girecek bos listeler olusturulur.
kadinlar_Turkce = []
erkekler_Turkce = []
#kadin ve erkeklerin kac kisi oldugunu sayamak icin sifirdan baslanir.
count_e = 0
count_k = 0
#kadinlarin ve erkeklerin ;Turkce ve Matematik notlarini girmesi icin sifirdan baslanir.
e_mat = 0
k_mat = 0
k_tur = 0
e_tur = 0
#for , if , elif donguleri icinde kadin matematik ve turkce,erkek matematik ve Turkce notlarini arttirarak yazar.
for i in range(len(sinav_sonuc['cinsiyet'])):
    if  sinav_sonuc['cinsiyet'][i] == 'K': 
        count_k +=1 
        k_mat =k_mat + sinav_sonuc['Matematik'][i]
        k_tur =k_tur + sinav_sonuc['Turkce'][i]
        kadinlar_Turkce.append(sinav_sonuc['Turkce'][i])
    elif sinav_sonuc['cinsiyet'][i] == 'E':
        count_e +=1 
        e_mat =e_mat + sinav_sonuc['Matematik'][i]
        e_tur =e_tur + sinav_sonuc['Turkce'][i]
        erkekler_Turkce.append(sinav_sonuc['Turkce'][i])
x = ((k_tur + e_tur)/(count_e + count_k))
#kadin erkek mat notlarinin ortalamasini alir.ve sinifin Turkce ortalamasini alip ekrana yazar.
print(f"Kadinlarin matematik ortalamasi: {k_mat/count_k}\n\
    Erkeklerin matematik ortalamasi: {e_mat/count_e}\n\
    Kursun toplam Turkce ortalamasi: {x}\n")
#kadin ve erkelerin Turkce notu icerisinde en yuksek olani yazar.
print("Turkce icin kadin en yuksek Elemani: ",max(kadinlar_Turkce))
print("Turkce icin erkek en yuksek Elemani: ",max(erkekler_Turkce))