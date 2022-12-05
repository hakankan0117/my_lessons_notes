# 1- "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
list1 = ["Bmw", "Mercedes", "Opel", "Mazda"]

# 2- Liste kaç elemanlıdır?
print(len(list1))

# 3- Listenin ilk ve son elemanı nedir?
print(list1[0]) # ilk eleman
print(list1[3]) # son eleman

# 4- Mazda değerini Toyota ile değiştirin.
list1[3] = "Toyota"
print(list1)

# 5- Mercedes listenin bir elemanı mıdır?
print("Mercedes" in list1) # true ya da false değeri verir.
# ya da böyle yaparız.
# list1= "Mercedes" in list1
# print(list1)

# 6- Listenin 2 indexindeki değer nedir?
print(list1[2])
# 7- Listenin ilk 3 elemanını alın.
print(list1[:3])
# ya da
print(list1[0:3])

# 8- Listenin son iki elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin.
list1[2:4] = ["Toyota", "Renault"]
print(list1)

# 9- Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
print(list1 + ["Audi", "Nissan"])
#ya da
list1 = list1 + ["Audi", "Nissan"]
print(list1)

# 10- Listenin son elemanını silin.
del list1[5]
print(list1)

# 11- Liste elemanlarını tersten yazdırınız.
list1 = list1[::-1]
print(list1)

# 12- Aşağıdaki verileri bir liste içinde saklayınız.
        # studentA: Yiğit Bilgi 2010, (70,60,70)
        #studentB: Sena Turan 1999, (80,80,70)
        #studentC: Ahmet Turan 1988, (80,70,90)

studentA = ["Yiğit", "Bilgi", 2010, [70,60,90]]
studentB = ["Sena", "Turan", 1999, [80,80,70]]
studentC = ["Ahmet", "Turan", 1988, [80,70,90]]

# 13- Liste elemanlarını ekrana yazdırınız.

print(studentA)
print(studentB)
print(studentC)
print(studentA[2]) # v.b

#BAŞKA BİR ÖRNEK
list2 = f"{studentA[0]} {studentA[1]} {2019-studentA[2]} yaşında ve not ortalaması {(studentA[3][0] +  studentA[3][1] + studentA[3][2])/3}"
print(list2)