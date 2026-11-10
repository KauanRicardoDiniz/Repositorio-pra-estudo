nomec = str(input("Digite seu nome completo: ")).strip()
nomec = nomec.split()
print("Primeiro nome: {}\nÚltimo nome: {}".format(nomec[0], nomec[len(nomec)-1]))