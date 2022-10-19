from email.mime import image
import re
from tkinter.messagebox import NO
import cv2
import easyocr
from timeit import default_timer

inicio = default_timer()


reader = easyocr.Reader(["es"], gpu=False)
image = cv2.imread("1.jpg")
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

archi1=open("dato2.txt","w") 
archi1.write(dato)   
archi1.close() 
print("en dato es: ", dato) 
    
fin = default_timer()
print(fin - inicio)

