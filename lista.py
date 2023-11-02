quant = int(input("Informe a idade de pessoas para o experimento "))
X, Y, Z, M, F, P, NP, XS, YS, ZS, MS, FS, PS, NPS, i = (
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
)


def calculo(x, y):
    if x > 0:
        x = (y / x) * 100
        print(f"{x:.2f}% Ganhar {100 - x:.2f}% Perder ")
    else:
        print("Não teve ")
        # b


def calcular(input, x, quant):
    if input == x:
        return quant + 1
    return quant


def calc_ganhar(input, x, ganha, quantS):
    if input == x and ganha == "S":
        return quantS + 1
    return quantS


while i < quant:
    geracao = str(input("Informe sua geracao. (X, Y, Z) ")).upper()
    sexo = str(input("Informe seu sexo. (M, F) ")).upper()
    pratica = str(input("Pratica ou Praticou futebol? (S, N) ")).upper()
    ganhar = str(input("O Brasil vai ganhar em 2026? (S, N) ")).upper()
    X = calcular(geracao, "X", X)
    Y = calcular(geracao, "Y", Y)
    Z = calcular(geracao, "Z", Z)
    M = calcular(sexo, "M", M)
    F = calcular(sexo, "F", F)
    P = calcular(pratica, "S", P)
    NP = calcular(pratica, "N", NP)
    XS = calc_ganhar(geracao, "X", ganhar, XS)
    YS = calc_ganhar(geracao, "Y", ganhar, YS)
    ZS = calc_ganhar(geracao, "Z", ganhar, ZS)
    MS = calc_ganhar(sexo, "M", ganhar, MS)
    FS = calc_ganhar(sexo, "F", ganhar, FS)
    PS = calc_ganhar(pratica, "S", ganhar, PS)
    NPS = calc_ganhar(pratica, "N", ganhar, NPS)
    i += 1
print("Geração X :")
calculo(X, XS)
print("Geração Y :")
calculo(Y, YS)
print("Geração Z :")
calculo(Z, ZS)
print("Sexo masculino :")
calculo(M, MS)
print("Sexo feminino :")
calculo(F, FS)
print("Pratica futebol :")
calculo(P, PS)
print("Não Pratica futebol :")
calculo(NP, NPS)

"""print("Pesquisa sobre o elevador.")
print("Digite o elevador que você mais utilizado:")
print("Qual périodo você utiliza o elevador com mais frequência:")
elevadorA = 0
elevadorB = 0
elevadorC = 0
perAm= 0
perAv = 0
perAn = 0
perBm = 0
perBv = 0
perBn = 0
perCm = 0
perCv = 0
perCn = 0

for i in range(20):
  elevador =  int(input("1- Elevador A, 2- Elevador B, 3- Elevador C. "))

  if elevador == 1:
    elevadorA += 1
    periodoA = (input("m- matutino, v- vespertino, n- noturno."))
    if periodoA == "m":
      perAm += 1
    if periodoA == "v":
      perAv += 1
    if periodoA == "n":
      perAn += 1

  if elevador == 2:
    elevadorB += 1
    periodoB = (input("m- matutino, v- vespertino, n- noturno."))
    if periodoB == "m":
      perBm += 1
    if periodoB == "v":
      perBv += 1
    if periodoB == "n":
      perBn += 1

  if elevador == 3:
    elevadorC += 1
    periodoC = (input("m- matutino, v- vespertino, n- noturno."))
    if periodoC == "m":
      perCm += 1
    if periodoC == "v":
      perCv += 1
    if periodoC == "n":
      perCn += 1
    
    periodoMaisA = max(perAm, perAv, perAn)
    elevadorUtilizado = max(elevadorA, elevadorB, elevadorC)

    if elevadorUtilizado == elevadorA:
        if  periodoMaisA == perAm:
          print("elevador A é o mais utilizado o periodo mais utilizado e matutino")
        if  periodoMaisA == perAv:
          print("elevador A é o mais utilizado o periodo mais utilizado e vespertino")
        if  periodoMaisA == perAn:
          print("elevador A é o mais utilizado o periodo mais utilizado e noturno")

    if elevadorUtilizado == elevadorB:
        if  periodoMaisA == perBm:
         print("elevador B é o mais utilizado o periodo mais utilizado e matutino")
        if  periodoMaisA == perBv:
         print("elevador B é o mais utilizado o periodo mais utilizado e vespertino")
        if  periodoMaisA == perBn:
         print("elevador B é o mais utilizado o periodo mais utilizado e noturmo")

    if elevadorUtilizado == elevadorC:
        if  periodoMaisA == perCm:
          print("elevador C é o mais utilizado o periodo mais utilizado e matutino")
        if  periodoMaisA == perCv:
          print("elevador C é o mais utilizado o periodo mais utilizado e vespertino")
        if  periodoMaisA == perCn:
          print("elevador C é o mais utilizado o periodo mais utilizado e noturno")""""





print("Pesquisa sobre o elevador.")
print("Digite o elevador que você mais utilizado:")
print("Qual período você utiliza o elevador com mais frequência:")
elevadorA = 0
elevadorB = 0
elevadorC = 0
perAm = 0
perAv = 0
perAn = 0
perBm = 0
perBv = 0
perBn = 0
perCm = 0
perCv = 0
perCn = 0

for i in range(5):
    elevador = int(input("1- Elevador A, 2- Elevador B, 3- Elevador C: "))

    if elevador == 1:
        elevadorA += 1
        periodoA = input("m- matutino, v- vespertino, n- noturno: ")
        if periodoA == "m":
            perAm += 1
        if periodoA == "v":
            perAv += 1
        if periodoA == "n":
            perAn += 1

    if elevador == 2:
        elevadorB += 1
        periodoB = input("m- matutino, v- vespertino, n- noturno: ")
        if periodoB == "m":
            perBm += 1
        if periodoB == "v":
            perBv += 1
        if periodoB == "n":
            perBn += 1

    if elevador == 3:
        elevadorC += 1
        periodoC = input("m- matutino, v- vespertino, n- noturno: ")
        if periodoC == "m":
            perCm += 1
        if periodoC == "v":
            perCv += 1
        if periodoC == "n":
            perCn += 1

# Agora, fora do loop, calcule os resultados finais
periodoMaisA = max(perAm, perAv, perAn)
elevadorUtilizado = max(elevadorA, elevadorB, elevadorC)

if elevadorUtilizado == elevadorA:
    
    if periodoMaisA == perAv:
        
    if periodoMaisA == perAn:
        print("Elevador A é o mais utilizado e o período mais é noturno.")

# Repita o mesmo padrão para os outros elevadores (B e C)
