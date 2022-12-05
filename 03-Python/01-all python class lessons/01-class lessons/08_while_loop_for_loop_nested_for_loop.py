##########  while Loop  ########
# while condition: condition true old. sürece sürekli çalışacak.
    # body

# number = 0
# while number < 6:
#     print(number)
#     number += 1
# print("now, number is bigger than or equel to 6")

# number = 0
# while number < 20:
#     print(number)
#     number += 2
# print("now, number is bigger than or equel to 20")

# my_list = ["a", "b", "c", "d", "e","f"]
# a = 0
# while a < len(my_list):
#     print(f"square of {a} is : {a ** 2}")
#     a += 1

# age = input("Please enter your age please : ")
# while age.isdigit():
#     print(f"Great you entered valid input : {age}")
#     age = input("Please enter your age : ")
# print("You entered invalid input")

# cevap = 17
# soru = "What number am i think number of? "
# print("Let's play the guessing game")
# while True:
#     tahmin = int(input(soru))
#     if tahmin < cevap:
#         print("little higher...")
#     elif tahmin > cevap:
#         print("little lower...")
#     else:
#         print("are you MINDREADER!!!")
#         break

# cevap = 17
# soru = "What number am i think number of? "
# print("Let's play the guessing game")
# while True:
#     tahmin = int(input(soru))
#     if tahmin < cevap:
#         print("little higher...")
#     elif tahmin > cevap:
#         print("little lower...")
#     elif tahmin == cevap:
#         print("are you MINDREADER!!!")
#         cevap += 25
#         break

# import random
# coin = ("yazi", "tura")
# yazi, tura = 0, 0
# games = 0

# print("Cikmak icin x e basiniz.")

# while True:
#     flip = random.choice(coin)
#     your_choice = input("Yazi mi Tura mi? ").lower()
#     if your_choice == "x":
#         print("GAME OVER")
#         print("Oyun istatistikleri: ")
#         print(f"Kac kere oynadiniz: {games}")
#         print(f"Kac kere yazi geldi: {yazi}")
#         print(f"Kac kere tura geldi: {tura}")
#         break
#     if your_choice == flip:  # "elif" de yazılırsa değişen bişi olmuyor komutta
#         print(f"Para {flip} geldi. Bravo!")
#         games += 1
#     else:
#         print(f"Para {flip} geldi. Tekrar deneyiniz.")
#         games += 1
#     if flip == "yazi":
#         yazi += 1
#     elif flip == "tura":
#         tura += 1

# sentence = input("Give me a sentence : ")
# words = sentence.split()  # cümledeki boşlukları alarak verdi
# counter = 0
# longest = 0
# # print(words) # deneme amaçlı girildi
# while counter < len(words):
#     if len(words[counter]) > longest:
#         longest = len(words[counter])
#     counter += 1
#     print(f"the length of the word: {longest}")

######### for variable in iterable: #############

# for i in [1, 2, 3, 4, 5]
#     print(i)

# liste = [1, 2, 3, 4, 5]
# for i in liste:
#     print(i)

# liste = [1, 2, 3, 4, 5]
# for number in liste:
#     print(number)

# seasons = ['spring', 'summer', 'autumn', 'winter']
# for i in seasons :
#     print(i)

 
# seasons = "erokmbwlkvkwpegmwegowmekglweogkwpeowpeokw"
# for i in seasons :
#     print(i)   

# seasons = "erokmbwlkvkwpegmwegowmekglweogkwpeowpeokw",  # tuple old. için yanyanya yazıyor
# for i in seasons :
#     print(i)   

# seasons = "erokmbwlkvkwpegmwegowmekglweogkwpeowpeokw"
# for i in seasons :
#     print(len(i))   

# seasons = ['spring', 'summer', 'autumn', 'winter']
# for i in seasons:
#     print(len(i)) 

# isim = ["Ahmet", "Ayşe", "Adem", "Yusuf", "Galip"]
# for i in isim:
#     print(f"Hello, {i}!")

# liste = []
# for i in range(1, 6):
#     liste.append(i)
#     print(liste)

# liste = []
# for i in range(1, 6):
#     liste.append(i)
# print(liste)  # tab geri olursa output farklı olur

# liste = []
# for i in range(1, 6):
#     liste.append(i)
#     print(i)

# word = input("Clarusway")  # isteğe bağlı
# word = "Clarusway"
# for i in word:
#     print(i, end="-")
   
# word = "Clarusway"
# count = 0
# for i in word:
#     count += 1
#     if count < len(word):
#         i = i + "-"
#     print(i, end="")

############ EDVIN İNSTRUCTER #########################
# answer = 26

# while True :
#     guess = int(input("what a two number i am thinking? "))
#     if guess < answer :
#         print("little higher")
#     elif guess > answer :
#         print("lither lower")
#     else :
#         print("Are you a MINDREADER!")
# #         break

# sentence = input("The best school is Clarusway : ")
# world_list = sentence.split()
# longest = 0


# city[1] = 'Melbourne'  # we assign 'Melbourne' to index 1
city = ['New York', 'Stockholm', 'Istanbul', 'Seoul', 'Sydney', 'Addis Ababa']
print(city[0]) 

# sentence = input("Give me a sentence : ")
# words = sentence.split()  # cümledeki boşlukları alarak verdi
# counter = 0
# longest = 0
# # print(words) # deneme amaçlı girildi
# while counter < len(words):
#     if len(words[counter]) > longest:
#         longest = len(words[counter])
#     counter += 1
#     print(f"the length of the word: {longest}")








