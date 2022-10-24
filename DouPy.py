import shutil

from imagededup.methods import PHash
import os
import json
fileName = r"Doublon"
if (os.path.exists(fileName)):
    print("le fichier doublon est bien là")
else:
    os.mkdir("Doublon")

try:

    phasher = PHash()
    duplicates = phasher.find_duplicates_to_remove(image_dir='C:/Users/Phili/Desktop/Test',
                                                   max_distance_threshold=12,
                                                   outfile='my_duplicates.json')
    with open('my_duplicates.json') as mon_fichier:
        data = json.load(mon_fichier)
    for loop in range(len(data)):
        shutil.move(data[loop], "Doublon")



except (RuntimeError):
    print(RuntimeError)