# python list metodları uygulama örnekleri

names = ["Ali", "Yağmur", "Hakan", "Deniz"]
years = [1998, 2000, 1998, 1987]

# 1- "Cenk" ismini listenin sonuna ekleyiniz.
names.append("Cenk")
print(names)

# 2- "Sena" değerini listenin başına ekleyiniz.
names.insert(0, "Sena")
print(names)

# 3- "Deniz" ismini listeden siliniz.
names.remove("Deniz")
print(names)
#names.pop() yaparsak listenin en son elemanını siler.

# 4- "Yağmur" isminin indexi nedir?
index = names.index("Yağmur")
print(index)

# 5- "Ali" listenin bir elemanı mıdır?
names2 = "Ali" in names
print(names2) # cevap:True

# 6- Liste elemanlarını ters çevirin.
names.reverse()
print(names)

# 7- Liste elemanlarını alfabetik olarak sıralayınız.
names.sort()
print(names)

# 8- years listesini rakamsal büyüklüğe göre sıralayınız.
years.sort()
print(years)

# 9- str = "Chevrolet, Dacia" karaktere dizisini liste çeviriniz.
str = "Chevrolet, Dacia"
list1 = str.split(",")
print(list1)

# 10- years dizisinin en büyük ve en küçük elemanı nedir?
min = min(years)
max = max(years)
print(min, max)

# 11- years dizisnde kaç tane 1998 değeri vardır?
result = years.count(1998)
print(result)

# 12- years dizisinin tüm elemanlarını siliniz.
years.clear()
print(years)

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
markalar = []
marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

print(markalar)