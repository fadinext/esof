import os,shutil
folder = "./gaps/"
prefix = input("Digite o prefixo :")
suffix = input("Digite a extensão do arquivo(ex: .txt ) :")
gap = int(input("Digite o num do arquivo do gap :"))

for file in os.listdir(folder)[::-1]:
    if file.startswith(prefix):
        num = int(file[len(prefix):len(file)-len(prefix):])
        if(num>=gap):
            shutil.move( folder + file,
                         folder + prefix + str(num+1).zfill(3)+ suffix )
            
input("Gap criado com sucesso! ENTER para sair.")

        
