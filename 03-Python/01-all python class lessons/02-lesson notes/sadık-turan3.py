website = "http://www.sadikturan.com"
course = "Python Kursu: Bastan Sona Python Programlama Rehberiniz (40 saat)"

# 1-"Hello World" karakter dizisinin baş ve sondaki boşluk karakterleri silin.
a = "Hello World"
print(a.strip("Hd"))
#ya da
print(a.lstrip("H").rstrip("d")) # bu şekilde string metodlarını ard arda kullanabiliriz.

print(a.lstrip("H")) # soldaki karakterleri siler
print(a.rstrip("d")) # sağdaki karakterleri siler

# 2- "www.sadikturan.com" içindeki sadikturan bilgisi haricindeki her karakteri silin.
print(website.lstrip("http://www.").rstrip(".com"))
# ya da
b = "www.sadikturan.com"
print(b.strip("w.moc"))

# 3- "course" karakter dizisinin karakterlerini küçük harf yapın.
print(course.lower())

# 4- "website" içinde kaç tane a karakteri vardır? 
print(website.count("a"))

# 5- "website", "www" ile başlayıp "com" ile bitiyor mu?
print(website.startswith("www")) # False
print(website.endswith("com")) # True

# 6- "website" içinde "com" ifadesi var mı?
print(website.count("com"))
# ya da
print(website.find("com"))

# 7- "course" içindeki karakterlerin hepsi alfabetik mi?
print(course.isalpha()) # False
print(course.isdigit()) # False

# 8- "Contents" ifadesini satırda 50 karakter içine yerleştirip  sağ ve soluna * ekleyiniz.
text = "Contents"
print(text.center(50, "*"))
print(text.ljust(50, "*")) # contents ifadesini sola yaslar
print(text.rjust(50, "*")) # contents ifadesini sağa yaslar

# 9- "course" karakter dizisindeki tüm boşluk karakterlerini "-" ile değiştirin.
print(course.replace("", "-"))

# 10- "Hello World" karakter dizisinin "World" ifadesini "There" olarak değiştirin.
a = "Hello World"
print(a.replace("World", "There"))

# 11- "course" karakter dizisini boşluk karakterlerinden ayırın.
print(course.split(" "))