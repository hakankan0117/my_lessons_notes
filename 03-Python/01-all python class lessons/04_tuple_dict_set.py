#################### TUPLE ################################
# my_tuple = ("hakankan")
# my_tuple2 = "hakankan"
# my_tuple = tuple("hakankan")
# print(my_tuple, type(my_tuple))  # tuple kelimeyi harflerine ayırıyor
# print(my_tuple2, type(my_tuple2))

# my_tuple = ("wakabayashi")  # tek başına eleman yapmak için 
# my_tuple2 = "wakabayashi"
# my_tuple = tuple("wakabayashi")
# print(tuple(my_tuple2))
# print(my_tuple, type(my_tuple))
# print(my_tuple2)

# my_tuple = ("wakabayashi")
# my_tuple2 = "wakabayashi"
# my_tuple = tuple("wakabayashi")
# print(my_tuple, type(my_tuple), sep="\n")
# print(my_tuple2)

# my_tuple = (1, 2, 3, 4, 567, 7, 863)
# my_list = list(my_tuple)
# print(my_tuple, type(my_tuple), sep="\n")
# print(my_list, type(my_list), sep="\n")

# my_tuple = (1, 2, 3, 4, 567, 7, 863)
# print(my_tuple, type(my_tuple))


# my_tuple = (1, 2, 3, 4, 567, 7, 863)
# print(my_tuple[3])
# print(my_tuple[3:5])  # start stop var bu komutta da

# my_tuple = (1, 2, 3, 4, 567, 7, 863)
# my_tuple[3] = 5  # tuple'a ekleme yapamıyoruz, fakat liste olsaydı yapabilirdik.
# print(my_tuple)  # 

# my_tuple = (1, 2, 3, 4, 567, 7, 863)
# my_list = list(my_tuple)
# my_list[5] = 17  # liste hali ile olabiliyor. (listenin 5. dizinin yerine yeni sayıyı ekliyor)
# print(my_list)

# sehirler = ["Istanbul", "Izmir", "Ankara", "Van", "Erzurum", "Sivas", "Gonya", "Ssinop", "Muğla", "Gaziantep"]
# print(sehirler)
# sehirler_tuple = tuple(sehirler)
# sehirler[9] = "çanakkale"  # [10] yazılırsa, "list assignment index out of range" hatası alırız
# print(sehirler)
# sehirler[10] = "Muş"  # 'tuple' object does not support item assignment" hatası verir

############################   DICT >> {} #################################  
# {key1 : value1, key2 : value2}
# {}
# dict()  

# first_dict1 = {"cola" : 25, "ekmek" : 5, "makarna" : 5}
# first_dict2 = dict(kola = 5, ekmek =4, makarna = "AKP")
# print(first_dict1)
# print(first_dict2)
# print(list(first_dict1))
# print(tuple(first_dict1))
# print(set(first_dict1))

# state_capitals = { "Ankara" : "Little Rock", 
#                     "Colorado" : "Denver",
#                     "California" : "Sacramento",
#                     "Geogia" : "Atlanta"
# }

# #state_capitals = ["Virgina" : "Richmond"]  # yanlış
# print(state_capitals["Atlanta"])  # atlanta değerini döndürüyor
# print(state_capitals["Atlanta"])

# state_capitals = { "Ankara" : "Little Rock", 
#                     "Colorado" : "Denver",
#                     "California" : "Sacramento",
#                     "Geogia" : "Atlanta"
# }

# state_capitals["Virgina"] = "Richmond"
# print(state_capitals)

# mix_values = {"animal": ("dog", "cat"), #tuple
#               "planet": ["Neptun", "Pluton", "Jupyter"], #liste
#               "number": 40, #integer
#               "pi": 3.14, #float
#               "is_good": False} #boolean

# mix_keys = {22 : "number",
#             3.14 :"float",
#             True: "boolean",
#             "key": "string"}

# my_dictionary = dict(animal= ("dog", "cat"), planet = ["Neptun", "Pluton", "Saturn"], number = 65)
# print(my_dictionary)

###### Main Operations With Dicts #################################
# items, keys, values 
# mix_values = {"animal": ("dog", "cat"), #tuple
#               "planet": ["Neptun", "Pluton", "Jupyter"], #liste
#               "number": 40, #integer
#               "pi": 3.14, #float
#               "is_good": False} #boolean

# mix_keys = {22 : "number",
#             3.14 :"float",
#             True: "boolean",
#             "key": "string"}
# print(mix_values.items(), "\n")  # hepsini gösteriyor
# print(mix_values.keys(), "\n")  # "\n" silinebiliriz de yukarıdaki için de gerçerli
# print(mix_values.values())

# mix_values = {"animal": ("dog", "cat"), #tuple
#               "planet": ["Neptun", "Pluton", "Jupyter"], #liste
#               "number": 40, #integer
#               "pi": 3.14, #float
#               "is_good": False} #boolean

# mix_keys = {22 : "number",
#             3.14 :"float",
#             True: "boolean",
#             "key": "string"}
# print(mix_values.items(), "\n")  # hepsini gösteriyor
# print(mix_values.keys(), "\n")  # "\n" silinebiliriz de yukarıdaki için de gerçerli
# print(mix_values.values(), "\n")
# mix_values.update({"is_bad" : True})  # value ekleme
# print(mix_values)
# del mix_values["is_good"]  # silme işlemi
# print(mix_values)

############## Nested Dictionaries #######################################

# ayrımlar ve dict üzerinden yapılıyor

# school_records={
# 	'personal_info':
# 		{'kid':{'tom':{'class':'intermediate', 'age':10},
# 			'sue':{'class':'elemantary', 'age':8}
# 			},
# 		'teen':{'joseph':{'class':'college', 'age':19},
# 			'marry':{'class':'high school', 'age':16}
# 			},
# 		},
#     'grades_info':
# 		{'kid':{'tom':{'math':88, 'speech':69},
# 			'sue':{'math':90, 'speech':81}

# 			},
# 		'teen':{'joseph':{'coding':80, 'math':89},
# 			'marry':{'coding':70, 'math':96}
# 			},
# 		}
# }
# print(school_records["grades_info"]["kid"]["sue"]["speech"])

# family = {
#     "erkek" : {
#         "baba" : {"yas" : 40, "meslek" : "eyt emeklisi" },
#         "kardes" : {"yas" : 22, "meslek" : "ogrenci"}
#     },
#     "kadin" : {
#         "anne" : {"yas" : 40, "meslek" : "emekli albay"},
#         "abla" : {"yas" : 27, "meslek" : "influencer"}
#     }
# }

# print(family["kadin"]["anne"]["meslek"])

############# set ##############################

# setler unordered, dict order

set_1 = {'red', 'blue', 'pink', 'red'}
colors = 'red', 'blue', 'pink', 'red'
renkler = tuple(colors[0])
print(renkler)
renkler1 = set(colors[0])
print(renkler1)
set_2 = set(colors)
print(type(set_1))  # her defasında farklı değerleri verir
print(type(colors))
print(set_2)

# flower_list = ["rose", "orchid", "cactus", "ginger", "rose", "tulip"]
# flower_set = set(flower_list)
# print(flower_list)
# print(flower_set)  # tekrarlı elemanı bir kere yazıyor

# a = set("aaAngara")
# b = set("Istanbul")
# c = set("Izmir")
# d = set("afyonkarahisar")
# #rint(a, b, sep = "\n")  # print(a), print(b)

# print(a.difference(b))  # == print(a - b)  farkı
# print(b.difference(a, c, d))  # == print(b - a, c, d)

# print(a.union(b))  # == print(a I b)   birleşim
# print(b.union(a))  # == print(b I a)

# print(a.intersection(b))  # == print(a & b)  kesişimi
























