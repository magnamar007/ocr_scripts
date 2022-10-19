from email.mime import image
import re
from tkinter.messagebox import NO
import cv2
import easyocr
from timeit import default_timer
#---------
import os
import sys
from string import Template
#---------
#---------
filein=open("Template/Plantilla.html")
src=Template(filein.read())
#---------
inicio = default_timer()

reader = easyocr.Reader(["es"], gpu=False)

image = cv2.imread("carnet.jpg")
result = reader.readtext(image)

cont = 0
pos = 0
dato = "nada"
encontrado = False

for res in result:
    
    
    
    cont += 1
    if encontrado == True:
        dato = res [1]
        encontrado = False
        
        
        
        
    if res [1] == "No" or res[1] == "No.":
        encontrado = True
        print("encontre el numero")
        
#--------------------------------------------        
D={ 'dato':dato,}

result=src.substitute(D)
try:
    os.mkdir("perfil")
    filein2 = open('perfil/'+'20175532'+'.html','a')
    filein2.writelines(result)
    print("Creando carpeta...")
    print("Guardando...")

except OSError:
    if os.path.exists('perfil'):    
        filein2 = open('perfil/'+'20175532'+'.html','a')
        filein2.writelines(result)
        print("Guardando...")

#--------------------------------------------  
archi1=open("dato2.txt","w") 
archi1.write(dato)   
archi1.close() 
print("en dato es: ", dato) 
    
fin = default_timer()
print(fin - inicio)