import os,shutil
folder = "./gaps/"
prefix = input("Digite o prefixo :")
suffix = input("Digite a extensão do arquivo(ex: .txt ) :")

for i,file in enumerate(os.listdir(folder)):
    if file.startswith(prefix):
        num = int(file[len(prefix):len(file)-len(prefix):])
        if(num!=i+1):
            shutil.move( folder + file,
                         folder + prefix + str(i+1).zfill(3)+ suffix )

input("Arquivos renomeados com sucesso!")

        
