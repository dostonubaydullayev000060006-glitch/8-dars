import os
os.system("cls")

# 1.m
# import datetime
# text = datetime.datetime.now()
# print(text)


# 2.m
# import datetime
# a = int(input("Yil: "))
# s = int(input("Oy: "))
# d = int(input("Sana: "))

# kiritilgan_yil = datetime.datetime(a,s,d)

# tugilgan = datetime.datetime.now()

# natija = tugilgan - kiritilgan_yil

# print(f"{natija.days} kun o'tdi")


# 3.m
# import datetime

# a = int(input("Yil: "))
# s = int(input("Oy: "))
# d = int(input("Sana: "))

# kelgusi = datetime.datetime(a,s,d)

# berilgan = datetime.datetime(a,9,30)

# natija = berilgan - kelgusi
# print(f"{natija.days} kun qoldi")


# 4.m
# A = [[1,2],[3,4]]
# B = [[5,6],[7,8]]

# C= []
# for i in range(len(A)):
#     new = []
#     for j in range(len(A[0])):
#         new.append(A[i][j] + B[i][j])
#     C.append(new)
# print(C)


# 5.m
# from translate import Translator
# tarjimon = Translator(to_lang="en", from_lang='uz')
# sozlar = ['salom','dastur',2.5,'yordam',34,'kitob']
# natija = {}

# for i in sozlar:
#     if type(i)==str:
#         natija[i]=tarjimon.translate(i)
  
# print(natija)



# 6.m
# filmlar = {
#     "Titanic": "Jack Dawson",
#     "Harry Potter": "Harry Potter",
#     "The Dark Knight": "Bruce Wayne (Batman)",
#     "The Matrix": "Neo (Thomas Anderson)",
#     "Forrest Gump": "Forrest Gump",
#     "Gladiator": "Maximus Decimus Meridius",
#     "Inception": "Dom Cobb",
#     "Spider-Man": "Peter Parker",
#     "Iron Man": "Tony Stark",
#     "The Lord of the Rings": "Frodo Baggins"
# }

# try:
#     soz = input("FIlm nomi : ")
#     print(filmlar[soz])
# except KeyError:
#     print("Bunday film yo'q!")
# finally:
#     print("Try except tugadi!")
   


