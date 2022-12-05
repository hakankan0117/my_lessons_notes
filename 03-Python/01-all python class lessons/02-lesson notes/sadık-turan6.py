ogrenciler = {
    "120": {
        "ad" : "Ali",
        "soyad" : "Yılmaz",
        "telefon" : "532 000 00 01"
    },
    "125" : {
        "ad" : "Can",
        "soyad" : "Korkmaz",
        "telefon" : "532 000 00 02"
    },
    "128" : {
        "ad" : "Volkan",
        "soyad" : "Yükselen",
        "telefon" : "532 000 00 03"
    },
}
    
    # 1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.
ogrenciler = {}

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyadı: ")
phone = input("öğrenci telefon: ")
# ogrenciler[number] = {
#     "ad" : name,
#     "soyad" : surname,
#     "telefon" : phone
# }
# print(ogrenciler)

# ya da şu şekilde yaparız.
ogrenciler.update({
    number: {
        "ad" : name,
        "soyad" : surname,
        "telefon" : phone
    }
})
print(ogrenciler)

    # 2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösteriniz.

ogrencino = input("öğrenci no: ")
ogrenci = ogrenciler[ogrencino]
print(ogrenci)