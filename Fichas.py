import string
import random
import os


number_ticke = input("Introduce la cantidad de Ticke que desee 1Hoja = (21) : ")
length_ticke = input("Intruduce el tamaño de caracteres: ")
profile_ticke = input("Introduce profile del ticke :")
coment_ticke = input("Introduce comentario del ticke :")
time_ticke = input("Introduce el tiempo ejemplo hrs:min:seg : ")
price_ticke = input("Introduce el precio de la Ficha : ")


number_ticke = int(number_ticke)
length_ticke = int(length_ticke)
time_ticke = time_ticke
number_of_strings = number_ticke
length_of_string = length_ticke
coment_ticke = coment_ticke
profile_ticke = profile_ticke



f = open(f"{coment_ticke}.pdf","w")
print("----------------Pegar Terminal--------------------------")
print("/ip hotspot user")
for x in range(number_of_strings):
    code = (''.join(random.SystemRandom().choice(string.ascii_letters + string.digits)for _ in range(length_of_string)))
    doc = ("add server=hotspot1 name="+code+" limit-uptime="+time_ticke+" profile="+profile_ticke+" comment="+coment_ticke)
    a = ("---------------------------------FdezNet-Fichas---------------------------------""\n")
    ficha = ("PIN: " +code+" | Tiempo: "+coment_ticke+" | Precio: $"+price_ticke+ " | FdezNet Residencial: XXXXXXXXXXX"+"\n")
    b = ("--------------------------------Internet-ilimitado------------------------------""\n")
    f.write(a)
    f.write(ficha)
    f.write(b)
    print(doc)
    
f.close()  # Este comando cierra el archivo después de escribir todos los usuarios
