# count = 0
# while count < 5:
#     print("Halil Pazarlama")
#     count += 1
# print("Osman Pazarlama")

# isim = "M.Osman"
# for i in isim:
#     print(i)  #  stringi harf harf alt alta sıralıyor

# isim = "M.Osman"
# for i in isim:
#     print(i, end="")  # "" arada boşluk olmadan yazdırıyor

# isim = "M.Osman"
# for i in isim:
#     print(i, end=" ")  # " " araya boşlık koyarak yazdırıyor

# times = int(input("How many times should I say 'I love you'"))
# for i in range(times) :
#     print('I love you')

# times = int(input("Kaç defa 'seni seviyorum' yazdırmalıyım"))
# for i in range(times) :
#     print("Seni seviyorum")

# times = int(input("Kaç defa 'seni seviyorum' yazdırmalıyım"))
# count = 1
# while count <= times:
#     count += 1
#     print("Seni seviyorum")

######### ÇARPIM TABLOSU #######################

# number = int(input("enter a number between 1-10: "))
# for i in range(11) :
#     print("{}X{}= ".format(number, i), number * i)
#     print(f"{number}X{i}=  {number * i}")

# for i in range(1,10):
#     for k in range(1,10):
#         print(f"{i} * {k}", "=", i *k)  # bu da olur
#         print(f"{i} * {k} = {i * k}")  # bu da olur

########### ARROW kullanıcısının yaptığı #########

# i=1
# sayi=int(input("Bir ile on arasında bir sayı giriniz: "))
# while i<=10:
#     if 1<=sayi<=10:
#         print(f"{sayi} * {i}= {sayi * i}")
#         i=i+1
#     if sayi >10:
#         print("Yazdığınız sayıyı kontrol ediniz")
#         break
######################################################

# b = list(range(11))
# print(b)

# b = list(range(11, 5, -1))
# print(b)


# b = list(range(11, 5, -2))
# print(b)

# a = list(range(10))
# print(a)

# b = set(range(10))
# print(b)

# c = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# c = set(c)
# print(c)

# d = "Havva Nur"
# d = set(d)
# print(d)

# print(range(5))
# print(*range(5))  # seperate it 
# print(*range(5,22,2))

# print(*("seperate"))

# print(("seperate"), end=" ")

# numbers = [0, 1, 2, 3, 4, 5]
# text = ["zero", "one", "two", "thre", "four", "five"]
# for x, y in zip(numbers, text):  # tablo mantığı ile eşleştiriyor
#     print(x, ":", y)

### Tekler ve Çiftler

# b = int(input("bir rakam giriniz : "))
# print(list(range(b[:2:])))

# numbers = int(input("Bir rakam giriniz : "))
# numbers = range(numbers)
# for i in range(numbers):
#     print(i)


# evens = []
# odds =[]
# for i in range (11):
#     if i % 2 == 0:
#         evens.append(i)
#     else:
#         odds.append(i)
# print(evens)
# print(odds)

######### TASK ####################################
# numbers = (11, 36, 33, 66, 89, 21, 32, 16, 10)
# or
# numbers = [11, 36, 33, 66, 89, 21, 32, 16, 10]

# numbers = (11, 36, 33, 66, 89, 21, 16, 10)
# evens = []
# odds = []
# for i in numbers : 
#     if i %2 == 0 :
#         evens.append(1)
#     else:
#         odds.append(i)
# print(f"The number of odds numbers: {len(evens)}")
# print(f"The number of odds numbers: {len(odds)}")

# numbers = (11, 36, 33, 66, 89, 21, 16, 10)
# evens = 0
# odds = 0
# for i in numbers : 
#     if i % 2 == 0 :
#         evens += 1
#     else:
#         odds += 1
# print(f"The number of odds numbers: {evens}")
# print(f"The number of odds numbers: {odds}")

##################################################

########### TASK ################################

# for i in range(10) :
#     print(f"{i}" * i)

# a = 1,2,3,4,5,6,7,8,9
# for i in a :
#     print(f"{i}" * i )

# for i in range(1, 10) :
#     print(str(i) * i)

############ TASK ##########################

# toplam = 0
# for i in range(1,75) :
#     toplam +=i
#     # print(toplam)
# print(toplam)

#############################################

# who = ["I am ", "Yor are "]
# mood = ["happy", "confident"]
# for i in who :
#     for k in mood :
#         print(i + k)


# who = ["I am ", "Yor are "]
# mood = ["happy", "confident"]
# for i, k in zip(who, mood):
#     print(i, k)

############# TASK ##########################

# names = ["susan", "tom", "edward"] 
# mood = ["happy", "sad"]
# for i in names:
#     for k in mood:
#         # print(f"{i} is {k}")
#         print(i.capitalize() + " is " + k)

################################################################
# for i in range(10):
#     print((9-i) * f" " + (2 * i -1) * f"{i}")  # piramit
#     print((9-i) * (" ") + (2 * i -1) * f"{i}")

# for i in range(9,0,-1):
#     print((9-i) * f" " + (2 * i -1) * f"{i}")  # ters piramit

######################################################################3
# for i in range(1, 7):
#     for k in range(i):
#         print("* ", end="")
#     print("")

# İKİSİNİ BİRLEŞTİREREK RUN DEDİĞİMİZDE OKLU PİRAMİT ÇIKIYOR

# for i in range(7, 0, -1):
#     for k in range(i):
#         print("* ", end="")
#     print("")

#######################################################################

# n = 5
# for i in range(n):
#     print(" " * (n - i - 1) + "* " * (i + 1))
# for k in range(n-1, 0, -1):
#     print(" " * (n - k) + "* " * k)

n = 5
for i in range(n):
    print(" " * (n - i - 1) + "* " * (i + 1))
for k in range(n-1, 0, -1):
    print(" " * (n - k) + "* " * k)