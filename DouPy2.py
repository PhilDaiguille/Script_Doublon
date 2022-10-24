import os
import shutil
fileName = r"Doublon"
from PIL import Image, ImageStat
image_folder = os.getcwd()
Fichier_image = os.listdir(image_folder)
if (os.path.exists(fileName)):
    print("le fichier doublon est bien là")
else:
    os.mkdir("Doublon")

print(Fichier_image)

for loop in range (len(Fichier_image)):
    #print(Fichier_image[loop])

    if Fichier_image[loop].__contains__("(1)"):
        print(Fichier_image[loop])
        shutil.move(Fichier_image[loop], "Doublon")
    elif Fichier_image[loop].__contains__("(2)"):
        print(Fichier_image[loop])
        shutil.move(Fichier_image[loop], "Doublon")
    elif Fichier_image[loop].__contains__("Copie"):
        print(Fichier_image[loop])
        shutil.move(Fichier_image[loop], "Doublon")
    elif Fichier_image[loop].__contains__("(3)"):
        print(Fichier_image[loop])
        shutil.move(Fichier_image[loop], "Doublon")
    elif Fichier_image[loop].__contains__("(4)"):
        print(Fichier_image[loop])
        shutil.move(Fichier_image[loop], "Doublon")


