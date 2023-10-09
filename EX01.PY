import random

palavras = ["COMPUTADOR", "MOUSE", "UNITY", "PYTHON" ]
advinhos = ""

def escolher_palavra(palavras):
  numero = random.randrange( 0, len ( palavras ))
  palavra_escolhida = palavras[numero].upper()
  return palavra_escolhida

def letra():
  advinhar = input("Qual letra? ")
  advinhar = advinhar.strip()
  advinhar = advinhar.upper()
  return advinhar

def percorrer_palavra(advinhar, acertos, palavra_escolhida):
  indice = 0
  for i in palavra_escolhida:
      if (advinhar == i):
          acertos[indice] = i
      indice += 1

def quantidade_letra(palavra):
  return ["_" for i in palavra]


def forca(errou):
  print("____________  ")
  print("\|/      |    ")

  if(errou == 1):
    print(" |       O    ")
    print(" |            ")
    print(" |            ")
    print(" |            ")
    print(" |            ")

  if(errou == 2):
    print(" |        O   ")
    print(" |        |   ")
    print(" |            ")
    print(" |            ")
    print(" |            ")

  if(errou == 3):
    print(" |        O   ")
    print(" |       /|   ")
    print(" |            ")
    print(" |            ")
    print(" |            ")

  if(errou == 4):
    print(" |       O    ")
    print(" |      /|\   ")
    print(" |            ")
    print(" |            ")
    print(" |            ")

  if(errou == 5):
    print(" |       O    ")
    print(" |      /|\   ")
    print(" |       |    ")
    print(" |            ")
    print(" |            ")

  if(errou == 6):
    print(" |       O    ")
    print(" |      /|\   ")
    print(" |       |    ")
    print(" |      /     ")
    print(" |            ")

  if (errou == 7):
    print(" |       O    ")
    print(" |      /|\   ")
    print(" |       |    ")
    print(" |      / \   ")
    print(" |            ")

  if (errou == 8):
    print(" |       Ô    ")
    print(" |      /|\   ")
    print(" |       |    ")
    print(" |      / \   ")
    print(" |            ")

  print(" |            ")
  print("_|____________")
  print()

def menu():
  pgt=input("Pressione 'F' para inicar as Forca \nDigite 'Sair' para encerrar\n").upper()
  if pgt == "SAIR":
    return

  if pgt == "F":
    errou = 0

    print("Bem vindo ao jogo da Forca!!!")
    palavra_escolhida = escolher_palavra(palavras)
    print("Palavra já selecionada")
    forca(errou)
    qtd = quantidade_letra(palavra_escolhida)
    print(qtd)
    letras_faltando = len(qtd)

    while True:
      advinhar = letra()

      if (advinhar in palavra_escolhida):
          percorrer_palavra(advinhar, qtd, palavra_escolhida)
          letras_faltando = str(qtd.count('_'))
          if (letras_faltando == "0"):
              print("Você ganhou parabéns !!! ")
              print(f'Palavra escolhida: {palavra_escolhida.upper()}')
              break
      else:
          errou += 1
          print(qtd)
          print(f'Ainda faltam acertar {letras_faltando} letras')
          print(f'Você ainda tem {8-errou} tentativas')
          forca(errou)

      if (errou == 8):
        print("Você foi enforcado! XD")
        break
      
      print(qtd)
menu()


