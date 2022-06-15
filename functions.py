import os, random, time 

from desenhos import desenhoForca
def limparTela():
    os.system ("cls")
#-----------------------------_-----------------------------------------------#
def verificarChute(palavraSecreta, letra, letrasChutadas,):
    chute = ""
    condicaoAcerto = False
    if letra in palavraSecreta:
        condicaoAcerto = True
    for i in palavraSecreta:
        if i in letrasChutadas:
            chute += i
        else:
            chute += "_" 
    tentativa = chute
    return condicaoAcerto, tentativa
#-----------------------------_-----------------------------------------------#
def correto(tentativa):
    limparTela()
    print("Essa letra pertence a Palavra\n")    
    print("Palavra{}".format(tentativa.upper()))
    input("Press Enter to continue...")
    limparTela()

def incorreto(tentativa,erros):
    limparTela()
    print("Essa letra não pertence a palavra :( \n")
    print("palavra{}".format(tentativa.upper()))
    desenhoForca(erros)
    input("Press to continue...")
    limparTela()

def amigos():
    arquivo = open("competidores.txt" ,"w")
    arquivo.close

def vencedor(desafiante , competidor, palavraSecreta):
    print("{} Parabens voçê ganhou!!".format(competidor))
    print("{} Voçê perdeu :(" .format(desafiante))
    arquivo = open ("competidores.txt", "a")
    arquivo.write(desafiante + "\n" + competidor )

    arquivo.close()
    input("Press enter to continue...")
    limparTela()

def lerArquivos():
    try: 
        arquivo = open("competidores.txt", "r")
        superficie = arquivo.read()
        arquivo.close()
        print(superficie)
    except:
        print("Histórico não habilitado")
        input("Press enter to continue...")
        limparTela()

def letrasChutadasPelaPessoa(letrasChutadas):
    if len(letrasChutadas) > 0:
        noticia = letrasChutadas
        print(f"{letrasChutadas}")