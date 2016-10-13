import os,shutil

path = './files/'
ext = input('Digite a extensão dos arquivos que deseja copiar (ex: .txt) :')
new_path = './copias/'

for folderName, subfolders , filenames in os.walk(path):
    for file in filenames:
        if (file.endswith(ext)):
            shutil.copy(folderName+'/' + file,
                        new_path + file)

input("Arquivos " + ext +" copiados! ENTER para sair.")
                            
            
