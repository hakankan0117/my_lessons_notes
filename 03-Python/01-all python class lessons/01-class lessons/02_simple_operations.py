# ARITHMETİC OPERATIPNS

# print(11 - 4)
# print(4 + 11.0)
# print("11 - 7")
# print("4" + 4)  # str ve int toplanamaz
# print("4" + str(4))  # int str yapılarak toplanabilir ancak

# print((4 * 5) / 2)
# print(type((4 * 5) / 2))  # tek bölme float verir.
# print(type((4 * 5) // 2))  # çift bölme int verir.

# sayı = 5
# sayı = sayı + 2
# sayı += 2  # sayı+2 yerine bu kısa komut da yazılabilir
# print(sayı)

# sayı = 5
# sayı = sayı - 2  # komutun önüne " # " işareti konularak sayı değerleri ayrı ayı denenebilir
# sayı -= 2
# print(sayı)

# sayı = sayı * 2
# sayı *= 2
# print(sayı)

# # sayı = sayı / 2
# sayı /= 2
# print(sayı)

# # sayı = sayı // 2
# sayı //= 2
# print(sayı)

# a = (1+ 3 ) ** (2 ** (1 * 2 / 2) / 2)
# print(a)

# ESCAPE SEQUENCES
# \n = Nemline (yeni satıra geçiyor)
# # \t = tab  (tab kadar boşluk bırakıyor)
# \b = backspace (bir satır geri siliyor)

# print( "we are", "boosting", "our", "brotherhood")
# print( "we are", "\boosting", "our", "\brotherhood")  # aradaki boşluğu kapatıyor
# print('it\'s essential to learn Python\'s libraries in IT world')  # \ virgülden önce bi etki etmiyor.

# print('C:\north pole\nnoise_penguins.text')  # "\n" yeni satıra atıyor
# print('C:\north pole\\nnoise_penguins.text')  # "\\n" yeni satıra atmıyor, fazladan "\", "\n" değerini etkisiz kılıyor.
# print('C:\\north pole\nnoise_penguins.text')

# print('first', 'second', 'third', sep="\n")  # her elemanı alt satıra atıyor.
# print('first', 'second', 'third', sep="\b")  # kendinden önceki harfi silip yerini alıp birleştiriyor.
# print('first', 'second', 'third', sep="\t")  # TAB kadar boşluk bırakıyor.
# print( "Mehmet", "Ahmet", "Ali", "Deniz", sep="\ ")

# Boolean Logic Expressions
# and   = tüm değerler True ise son True değerini döndürür, aksi halde ilk değer false ise ilk False döndürü.
# or    = 
# not

# True and True..      son True
# True and False..      ilk False
# False and False...   İlk False
# False and True...     İlk False

# print(True and True)  # True
# print(True and False)  # False
# print(False and True)  # False
# print(False and False)  # False
# print(True and  not True)  # False
# print(True and not False)  # True

# "Or" True duyarlidr, onu arar ilk buldugunu döndürür.

# False or False...   False döndürür
# True or True...       İlk True döndürür
# False or True...      İlk True döndürür
# True or False...     İlk True döndürür

# print(True and False or not False or False)  # "not False" = "True" olur
# print(True and False or True or False)  # "True and False" = "False" olur
# print(False or True or False)  # "false or True" = "True" olur
# print(True or False)  # "True or False" = "True" olur

#  TRUTH VALUES OF LOGIC STATEMENTS

# None
# Zero : 0, 0.0, 0j
# Empty Seq. and collections: ' ', [], {}
# Any remaining value: True   (Diğer kalan her şey "True")

# AŞAĞIDAKİ DEĞERLERİN DIŞINDA KALAN HER ŞEY "True" dur.

# print(0 and 'True')  # boşluk değerini döndürür.
# print(0.0 and 'True')
# print(0j and 'True')
# print('' and 'True')
# print("" and 'True')
# print([] and 'True') 
# print({} and 'True')
# print(() and 'True')
# print("True" and () and "True")

# print(2 and "hello world")  # and komutu son true değerini döndürür.
# print(2 and "False")
# print(" " and "hello world")
# print("" and "hello world")

# print([] and "be happy")
# print(() and None)
# print(1 and 2 and False and 4)  # son "false"u döndürür
# print(1 or 2 or False or 4)  # ilk "true" olanı bulur döndürür.
# print(False or 2 or False or 4)  # ilk "true" olanı bulur döndürür.
# print(False or [] or {} or None or " ")  # hepsi "false" ise son "false"u döndürür.

# # "or" her zaman ilk "True" değerini döndürür, (fakat son "False" değerini döndürür.)

# print(2 or "hello world")
# print([] or "be happy!")
# print(None or ())
# print({} or 0)
# print({0} or False)
# print({} or False)
# print(False or 2 or False or 4)

# INDEXING & SLICING STRINGS

# best = "Clarusway"
# print("Clarusway"[4])
# print(best[4])  # tek rakamla alınca indeksleme,
# print(best[0:4])  # belli bir aralığı alınca slice'lamadır.
# print(best[-1])  # son harfi alır
# print(best[0:-1])  # ilk harften sondan bir öncekine kadar
# print(best[::2])  # bir harf atlayarak alır
# print(best[0:2:4])
# print("123456789"[0:9:1])  # start:stop:step
# print("1234567899"[0:10:3])  # 3 atlayarak alır

# fruit = 'Orange'
# print('Word : ', fruit)
# print('First letter : ', fruit[0])
# print('Second letter : ', fruit[1])
# print('3rd to 5th letters : ', fruit[2:5])  # kelime harf sıralaması 0'dan başlar
# print('Letters all after 3rd : ', fruit[2:])
# print('First letter : ', fruit[0:len(fruit)])
# print(len(fruit))

# best = "clarusway"
# print(len(best))

# print("clarus" + "way")  # combine ediyor
# print("clarusway" * 3)  # 3 defa yan yana yazıyor
# print(3 * "clarusway")  # 3 defa yan yana yazıyor
# print(* "clarusway")  # tek tek elemanlarına ayırıyor


# a = "upper"
# b = "case"
# a += b  # (a = a + b)
# print(a) 

# c = "letter"
# a = "first "
# a += c  # (a = a + c)
# print(a)

# STRING FORMATTING   (f"string{})
# Ex: print("string{} string{} string{}".format(data1, data2, data3))
# Ex: print(f"string {} string{} string{} string{}")
# fruit = "apple"
# vegetable = "spinach"
# amount = 5
# output = f"I bought {fruit} and {vegetable}. They are {amount} kgs."
# print("I bought apple and spinach. They are 5 kg.")
# print(output)
# print(f"I bought {fruit} and {vegetable}. They are {amount} kgs.")
# print("I bought {} and {}. They are {} kg.".format(fruit, vegetable, amount))

# Ex: print(f"string{variable1} string{variable2} string{variable3} string
# print(f"I bought {fruit} and {vegetable}. They are {amount} kgs.")
# print(f"I bought {fruit} and {vegetable}. They are {2 + 3} kgs.")
# print(f"I bought {fruit.upper()} and {vegetable.lower()}. They are {amount} kgs.")  # "upper" heğsini büyük harf yapar
# print(f"I bought {fruit.lower()} and {vegetable.upper()}. They are {amount} kgs.")  # "lower" hepsini küçük harf yapar
# print(output)

# simple = f"{2 ** 3}"
# print(simple)

# my_name = "hakan"
# output = f"My name is {my_name.capitalize()}"
# print(output)

# name = "marIAM"
# output = f"My name is {name.capitalize()}"  # kelimenin baş harfini büyük yapar
# print(output)

# Python code to get the output of “Susan is a young lady and she is a student
# at the CLRWY IT university.”, using f-string in multiline with the variables below.

# name = "Susan"
# age = "young"
# gender = "lady"
# school = "CLRWY IT university"
# output = f"{name} is a {age} {gender} and she is a student at the {school}"
# print(output)


