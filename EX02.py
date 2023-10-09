import random

def jogar(): 
    iniciou() 
    ganhou = False 
    perdeu = False 
    velha = False 

    iniciar = 0 

    possiveis() 
    posicoes = [["_","_","_"], 

                ["_","_","_"], 

                ["_","_","_"]] 

    ordem = jogada(iniciar, posicoes) 

 

    while (not ganhou and not perdeu and not velha): 

        if(ordem == 0):

            print("Próxima vez!")

            linha = int(input("Número da linha")) 
            coluna = int(input("Número da coluna"))
            posicoes[linha][coluna] = ("X") 
            for n in range(0, 3):
                print(posicoes[n]) 
            ordem = ordem + 1 
            print("\n") 

        else: 

            print("Próxima vez!") 

            linha = int(input("Número da linha")) 
            coluna = int(input("Núero da coluna")) 
            posicoes[linha][coluna] = ("O") 
            for n in range(0, 3): 
                print(posicoes[n]) 
            ordem = ordem - 1 
            print("\n") 


def iniciou(): 
  print("Bem vindo ao jogo da velha!!!\n") 
  pgt=input("Pressione 'F' para inicar o Jogo \nDigite 'Sair' para encerrar\n").upper()
 

def possiveis(): 
    print("0,0","|","0,1","|","0,2") 
    print("1,0","|","1,1","|","1,2") 
    print("2,0","|","2,1","|","2,2") 

def jogada( start, posicoes): 
    if(start == 1): 

        print("Vez do Jogador 1") 
        linha = int(input("Linha: ")) 
        coluna = int(input("Coluna: ")) 
        posicoes[linha][coluna] = ("X") 
        for n in range(0,3): 
            print(posicoes[n]) 
        ordem = 1 

    else: 
        print("Vez do Jogador 2") 
        linha = int(input("Linha: ")) 
        coluna = int(input("Coluna: ")) 
        posicoes[linha][coluna] = ("O") 
        for n in range(0,3): 
            print(posicoes[n]) 
        ordem = 0  
    return ordem 
jogar()
