website = "http://www.sadıkturan.com"
course = "Python Kursu: Bastan Sona Python Programlama Rehberiniz (40 saat)"
# 1-"course" karakter dizisinde kaç karakter bulunmaktadır?
print(len(course))
# 2- "website" içinden www karakterlerini alın.
print(website[7:10])
# 3- "website" içinden com karakterlerini alın.
print(website[22:25])
# ya da 
length = len(website)
print(website[length-3:length])
# 4- "course" içinden ilk 15 ve son 15 karakteri alın.
print(course[:15]) 
#ya da 
print(course[0:15])
print(course[-15:])
# 5- "course" ifadesindeki karakterleri tersten yazdırın.
print(course[::-1])

name, surname, age, job = "Bora", "Yılmaz", 32, "mühendis"

# 6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#   "Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis."
# f.string metodu kullanarak
print(f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}.")
#ya da .format işlemi uygulayarak
print("Benim adım {} {}, Yaşım {} ve mesleğim {}".format(name, surname, age, job))
#ya da string birleştirme işlemi yaparsak:
print("Benim adım " + name + " " + surname + " Yaşım" + " " + str(age) + " ve mesleğim"+ " " + job)

# 7- "Hello World" ifadesindeki w harfini W harfi ile değiştirin.
s = "Hello World"
print(s[0:6] +  "W" + s[-4:])
# ya da .replace() metodu kullanırız.
print(s.replace("w", "W"))

# 8- "abc" ifadesini yan yana 3 defa yazdırın.
s = "abc"
print(3*s)