

# #SORU 1:

# #Kullanıcıdan değer aldık.
# sayi1 = int(input("Birinci sayiyi giriniz: "))
# sayi2 = int(input("İkinci sayiyi giriniz: "))

# #Sırasıyla toplama, çıkarma, çarpma, bölme, mod alma ve üssü işlemleri yaptık.
# toplama = sayi1 + sayi2
# cikarma = abs(sayi1 - sayi2)
# carpma = sayi1 * sayi2
# bolme = sayi1 / sayi2
# mod = sayi1 % sayi2
# us_alma = sayi1 ** sayi2

# #Yazdırma işlemi yaptık.
# print(f" Saylarınızın toplamı: {toplama} \n Sayıların farkı: {cikarma} \n Sayıların çarpımı: {carpma} \n Sayıların bölümü: {bolme} \n Sayıların modu: {mod} \n {sayi1} üssü {sayi2} :{us_alma}")




# #SORU 2:

# #Kullanıcıdan değer aldık.
# sayi = int(input("Bir sayi giriniz:"))

# #Birbiri ardınca sayıları toplayacağımız için toplam sıfır değeri atadık.
# toplam = 0

# #Döngü sayesinde 1 den bize verilen sayıya kadar sayıların toplanmasını sağladık.
# for i in range(1,sayi+1):      ##Burda döngümüzün nerden başlayıp nereye kadar olacağını belirttik.
#     toplam += i                ##Burda elde ettiğimiz her sayıyı toplayarak toplama atadık.

# #Yazdırma işlemi yaptık.
# print(f"Bir'den {sayi} kadar olan sayıların toplamı : {toplam}")




# #SORU 3:

# for i in range(2,101,2):      ##Burda döngümüzün 2 den başalayıp 100'e kadar , 2'şer bir şekilde artmasını söyledik.
#     print(i)                  ##Yazdırma işlemi yaptık.
    



# #SORU 4:

# # Kullanıcıdan metin aldık.
# metin = input("Bir metin girin: ")

# # Ters metni oluşturmak için boş bir değişken tanımladık.
# ters_metin = ""

# # Metni sondan başa döngü ile gezdik.
# for i in range(len(metin) - 1, -1, -1):
#     ters_metin += metin[i]                 #Burda her elde etiğimiz harfi ters metne eklemeyi yaptık.

# # Sonucu yazdırdık.
# print("Ters çevrilmiş metin:", ters_metin)






