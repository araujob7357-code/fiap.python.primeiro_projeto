#--------------------------------------estrutura condicional simples
# nota = 5.0
#
# if nota < 6:
#     print(f'sua nota é: {nota}')
#
# print("FIM")

#---------------------------------------Estrtura condicional composta
# nota_final = 5.0
#
# if nota_final < 6:
#     print("Reprovado")
# else:
#     print('Aprovado')
#

#--------------------------------------estrutura codicional encadeada
nota_final = 5.0

if nota_final < 6:
    print("Reprovado")
else:
    if nota_final < 6:
        print("Recuperação")
    else:
        print("Aprovado")

# --------------------------------------estrutura codicional encadeada - elif
nota_final = 5.0

if nota_final < 6:
    print("Reprovado")
elif nota_final < 6:
        print("Recuperação")
else:
        print("Aprovado")

print("FIM")