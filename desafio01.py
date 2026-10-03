#resolucao desafio1 nota = []
nota1 = int(input (" digite  a nota 1: "))
nota2 = int(input (" digite  a nota 2: "))
nota3 = int(input (" digite  a nota 3: "))
nota4 = int(input (" digite  a nota 4: "))

lista_de_notas = [nota1,nota2,nota3,nota4]

print(f"a maior nota foi {max(lista_de_notas)}")
print(f"a menor nota foi {min(lista_de_notas)}")
print(f"a soma de todas as nota foi {sum(lista_de_notas)}")

media = sum(lista_de_notas)/len(lista_de_notas)
print (media)

lista_de_notas = 5
if lista_de_notas >=5:
 print(" aprovado!")

else:
 print("reprovado! )")

 #if sum(notas/len(notaas) >= 6:)
  #print("aprovado")
  #else:
  #print("reprvado")


