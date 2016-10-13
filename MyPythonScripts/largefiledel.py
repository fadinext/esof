import os,shutil

path = './files/'

for folderName, subfolders , filenames in os.walk(path):
    for file in filenames:
        if(os.path.getsize(folderName + "/" + file) >= 104857600):
            print( os.path.abspath(folderName + file) + '\n')

input("Arquivos grandes revelados! ENTER para sair.")
                            
            
