message = "     Hello There. My name is Sadık Turan     "
print(message.upper()) # bütün karakterleri büyük karaktere çevirir.
print(message.lower()) # bütün karakterleri küçük karaktere çevirir.
print(message.title()) # her kelimenin baş harfi büyük harfe çevrilir.
print(message.capitalize()) # verilen string ifadenin sadece ilk harfini büyük harfe çevirir.
print(message.strip()) # sağ ve soldaki boşlukları siler.
print(message.split()) # her bir kelime boşluk karakterlerinden ayrılır ve ayrı stringler halinde karşımıza çıkar.
print(message.split(".")) # her bir noktadan itibaren ayırır.
print(message.join("123")) # join içine yazdığımız karakterleri ayırarak her birinin arasına message'a atadığımız değeri yazdırır.
print(message.find("Sadık")) # sadık'ın hangi index değerine sahip olduğunu gösterir.
print(message.startswith("h")) # h ile mi başladığını sorarız. cevap boolean değere sahiptir: False
print(message.endswith("")) # boşluk ile mi bitiyor? : True
print(message.replace("Sadık", "Çınar")) # sadık yerine çınar yazdırdık.
print(message.center(50)) # bizim değerimizi 50 karakterlik alanına sığdırır. Daha çok web uygulamasında açıklama yapmak istediğimiz durumlarda ortalamak için kullanırız.