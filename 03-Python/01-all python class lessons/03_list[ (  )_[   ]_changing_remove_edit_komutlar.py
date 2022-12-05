
# text = "www.clarusway.com"
# print(text.startswith("www"))
# print(text.endswith(".om"))  # sonucu true veya false olarak döndürür
# print(len(text))
# print(text.upper())
# print(text.lower())
# print(text.capitalize())

# game = "witcher 3"
# print(game.endswith("4"))

# sentence = "i live and work in Turkey"
# sentence = sentence.capitalize()
# print(sentence)
# print("i live and work in Turkey".capitalize())
# print(sentence.capitalize())  # cümlenin ilk kelimesinin baş harfini büyük yapar
# print(sentence.upper())  # bütün kelimelerin baş harfini büyük yapar
# print(sentence.lower())  # bütün kelimelerin baş harifini küçük yapar
# print(sentence.title())  # her kelimenin baş harfini büyütür.
# print(sentence.replace("Turkey", "Cyprus"))  # belirtilen kelimelerin yerini değiştirir

# text_2 = "mERHABA DÜNYALI BEN DOSTUM"
# print(text_2.capitalize())
# print(text_2.lower())
# print(text_2.title())

# print(sentence)
# print(text)
# print(text_2)

# text_2 = "mERHABA DÜNYALI BEN DOSTUM"
# print(text_2.upper().lower().capitalize().lower().upper())  # en son fonksiyonu döndürür yani upper()

# sentence_2 = "Pc her zaman console oyunlarini dover"
# print(sentence_2.replace("i", "+"))

# text = "the better the familt, the better the society"
# print(text.title())

# text = "S0d0me and G0m0re)"
# print(text.replace("0","o"))

# text_3 = "      listen first        "
# print(text_3.strip())

# text = "tyou can learn almost everything in pre-classz"
# print(text.upper().lstrip("T").rstrip("Z"))  # önce kelimelerin hepsini büyük harf sonra diğerlerini döndürür
# print(text.lstrip("t").rstrip("z").upper())
# print(text.lstrip("t").upper().rstrip("z"))  # sırasıyla yaptığı için küçük "z" kaldırılmadı, çünkü "Z" old. için
# print(text.upper().strip("TZ"))  # en solda ve en sağdaki harfleri kaldırır.

#   list []
#   tuple ()
#   dict {}
#   set {}

# text1 = ["kuroko no basket", 36, ["Slam Dunk"]]
# print((text1))

# liste1 = ["happy", 336, 3.14]
# liste2 = ("happy") 
# liste3 = "happy"
# print(liste3)
# print(list(liste1))
# print(list(liste2))  # output liste [] içinde veriliyor

list_1 = ['h', 'a', 'p', 'p', 'y']
my_tuple = tuple(list_1)
my_set = set(list_1)
my_dict = dict(list_1)
print(my_tuple)
print(my_set)
print(my_dict)  # dönüşemez, dict'te mutlaka key:value olacak.

# word = 'happy'
# list_2 = list(word)
# print(list(word))
# print(list_2)

# country = ["USA", "New Zealand", "Finland", "Sweden", "Syria", "Turkey"]
# a = "Sweden"
# b = tuple(a[:])
# print(country)
# print(list(country[3]))
# print(list(a))
# print(b)

# mixed_list = [11, 'Joseph', False, 3.14, None, {1: "bir"}]  
# output = list(mixed_list)
# print(output)

# mixed_list = [11, 'Joseph', False, 3.14, None, [1, "bir"]] # listenin içinde liste olabiliyor
# output = list(mixed_list)
# print(output)

# mixed_list = [11, list('Joseph'), False, 3.14, None,(1, "bir")]  # listenin içinde liste olabiliyor
# output = list(mixed_list)
# print(output)

# my_list = ["Aslan", "Clarusway", 2022]
# new_list1 = list(my_list)
# new_list2 = [my_list]
# print(list(my_list))
# print(new_list1)
# print(new_list2)
# print(len(new_list1))
# print(len(new_list2))

# my_list = ["em", "key", 4130]
# new_list = list(my_list)
# print(new_list)
# print(len(list(my_list)))

# my_list = ("em", "key", 4130)
# new_list1 = list(my_list)
# new_list2 = [my_list]
# print(new_list1)
# print(len(new_list2))

# empty_list = [1]
# empty_list.append(2)  # Append object to the end of the list.
# empty_list.append("Multiverse")
# empty_list.append("multiVeRses".casefol())
# empty_list.append("Multiuniverse")
# empty_list.append(3.14)
# empty_list.append("")
# print(empty_list)

# a = "deneme".casefold()
# b = "DenemE".casefold()
# print(a)
# print(b)
# if a == b:
#     print(True)
# else:
#     print(False)

# empty_list = []
# empty_list.append(1)
# empty_list.append(10)
# print(empty_list)
# empty_list.append(2)
# empty_list.append(3)
# empty_list.append(4)
# print(empty_list)


# my_list = [1, 2, 3]
# my_list.append(4)  # my_list.append(4, 5, 6) list.append() takes exactly one argument ( not 2 or more)
# my_list.append("hakan")
# my_list.append(None)
# print(my_list)

# liste_4 = [1,4,7]
# liste_4.insert(3, 5)  # 3. indeksten sonra 5 ekliyor
# print(liste_4)

# liste4 = ["1", 4, 5, "Ankara", 7]
# liste4.insert(0, 5)  # 0. indekse 5 ekliyor. kaçıncı indeks olduğu belirtilmeli mutlaka (0. indeks)
# liste4.insert(2, 5)  # 2. dizine 5 ekliyor.
# print(liste4)

# liste4 = [1,4,5,7]
# liste4.pop()  # pop son indeksi atıyor (siliyor) >> 7 attı
# liste4.remove(5)  # listedeki belirtilen indeksi kaldırıyor >> 5 kaldırıldı
# del liste4[0]  # listedeki 0. dizindeki elemanı siliyor >> 1 silindi
# print(liste4)  # geriye [4] kalır

# a = ["deneme", 1, 2, "emkey", 4, "hakan"]
# del a[3]  # del sadece listeden eleman siliyor.
# print(a)

# liste5 = [4, 1, 5, 7]
# liste5.sort()  # "sort" büyükten küçüğe ve alfabetik sıraya göre sıralıyor, karışık elemanları görmüyor.
# print(liste5)

# liste5 = ["a", "i", "c", "h"]
# liste5.sort()  # "sort" büyükten küçüğe veya alfabetik sıraya göre sıralıyor, karışık elemanları görmüyor.
# print(liste5)  # ya int ya da str olacak. karışık karekterleri sıralamaz

# new_list = ["Benim adım", ".", "Okul numaram", ".", 2003, "yılında mezun", ".", "atılacak"]
# new_list.insert(1, "Hakan")
# new_list.insert(4, 4217)
# new_list.insert(8, "oldum")
# new_list.pop()
# print(new_list)

# city = ['New York', 'Stockholm', 'Istanbul', 'Seoul', 'Sydney', 'Addis Ababa']
# city[1] = 'Melbourne'  # we assign 'Melbourne' to index 1
# print(city) 

# animals = ['elephant', 'bear', 'fox', 'wolf', 'rabbit', 'deer', 'giraffe']
# print(animals[1:5])  # 1. indeks dahil 5. indekse kadar alıyor, 5. indeks hariç

# animals = ['elephant', 'bear', 'fox', 'wolf', 'rabbit', 'deer', 'giraffe']
# print(animals[3:])  # 3. indeksten sonra sonuna kadar hepsini alıyor

# animals = ['elephant', 'bear', 'fox', 'wolf', 'rabbit', 'deer', 'giraffe']
# print(animals[:5])  # en baştan 5. indekse kadar (5. indeks hariç)

# animals = ['elephant', 'bear', 'fox', 'wolf', 'rabbit', 'deer', 'giraffe']
# print(animals[0:])  # o. indeksten sonuna kadar hepsini alıyor

# animals = ['elephant', 'bear', 'fox', 'wolf', 'rabbit', 'deer', 'giraffe']
# print(animals[::2])  # baştan sona 1 indeks atlayıp 2. indeksi alarak devam ediyor. (0,2,4,6.. şeklinde alıyor)

# liste5 = [[1, 3], [44, -44], [-12, 1]]  # liste içinde listeden indeks alma
# print(liste5[1])  # listedeki 1. indeksi alıyor 
# print(liste5[1][0])  # listenin 1. indeksinin 0. indeksini alıyor

# liste5 = [[1, 3], [44, -44], [-12, 1]]  # liste içinde listeden indeks alma
# print(liste5[1])  # listedeki 1. indeksi alıyor 
# print(liste5[1][0])  # listenin 1. indeksinin 0. indeksini alıyor
# print(liste5[1].append(5))

# x = list(range(1, 11))  # range komutu girilen sayılar arası aralığını veriyor (range(1, 6) = 1 ve 5 arası sayıları verir
# x.sort(reverse=True)
# x.reverse
# print(x)
