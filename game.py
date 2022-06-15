
import os
from tkinter import E
from tracemalloc import stop
from functions import  verificarChute, correto, incorreto, amigos, vencedor, lerArquivos, letrasChutadasPelaPessoa, limparTela
from desenhos import  desenhoForca, noticiaVencedor, noticiaPerdedor


while True:
    
    limparTela()
    
    erros = 0
    dica = 3
    letrasJogadas = []
    letrasPossibilitadas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ]
    letrasDeChute = []

    print("="*20)
    print("Bem vindos ao jogo da forca!!")
    print("="*20)

    while True:
        print("(1) New Game ")
        print("(2) Historic ")
        print("(3) Close ")
        inicio = input(" Escolha uma opção ")
        if inicio == "1":
            limparTela()
            break
        elif inicio == "2":
            lerArquivos()
        elif inicio == "3":
            quit()
        else:
            print("Opção Inexistente")

    desafiante = input("Digite o nome do desafiante: ").capitalize()
    competidor = input("Digite o nome do competidor: ").capitalize()
    limparTela()

    while True:
        verPalavras = True
        palavraSecreta = str(input("Digite a palavra secreta do jogo: ").upper())
        for i in palavraSecreta:
            if i not in palavraSecreta:
                if i not in letrasPossibilitadas:
                    verPalavras = False
        if verPalavras == False:
            print("A palavra possui um caractere incorreto")
            input("Press enter to continue...")
        elif verPalavras:
            break

    chuteInicial = "_" *len(palavraSecreta)
    limparTela()

    dicas = []
    dicas.append(input("Digite uma dica: "))
    dicas.append(input("Digite a segunda dica: "))
    dicas.append(input("Digite a terceira dica: "))
    limparTela()

    while erros != 6 and chuteInicial != palavraSecreta:
        desenhoForca(erros)
        print("Palavra {}" .format(chuteInicial.upper()))
        print("Você possui {} dicas!" .format(dica))
        print("(1) Jogar" )
        print("(2) Solicitar dica")
        while True:
            try:
                op = (int(input("Como você deseja prosseguir: ")))
                break
            except:
                print("Opção Inexistente: ")
                input("Press enter to continue" )
            limparTela()    
    
        if op == 1:
            while True:
                letrasChutadasPelaPessoa(letrasDeChute)
                letra = input("Digite a palvra que você deseja chutar: ").upper().strip()
                if len(letra) == 1 and letra not in letrasPossibilitadas:
                    print("Caractere inválido")
                elif letra in letrasDeChute:
                    print("Você já usou essa letra!")
                else:
                    break
        
            if len(letra) < 1:
                if letra == palavraSecreta:
                    chuteInicial = letra
                    break
                else:
                    print("A palavra não está correta!")
                    erros += 1
                    desenhoForca(erros)
                    input("Press enter to continue...")
                    limparTela()
            else:
                letrasDeChute.append(letra)
                condicaoAcerto, chuteInicial = verificarChute(palavraSecreta, letra, letrasDeChute)

            if condicaoAcerto:
                correto(chuteInicial)
            else:
                erros += 1
                incorreto(chuteInicial, erros)

        elif op == 2:
            if dica > 0:
                print("Sua dica é: ",dicas [-(dica)])
                dica -= 1
            else:
                print("Você não possui dicas!")

            while True:
                letrasChutadasPelaPessoa(letrasDeChute)
                letra = input("Digite a palvra que você deseja chutar: ").upper().strip()
                if len(letra) == 1 and letra not in letrasPossibilitadas:
                    print("Caractere inválido")
                elif letra in letrasDeChute:
                    print("Você já usou essa letra!")
                else:
                    break

            if len(letra) > 1:
                if letra == palavraSecreta:
                    chuteInicial = letra 
                    break
                else:
                    print("A palavra NÃO está correta!")
                    erros += 1
                    desenhoForca(erros)
            else:
                letrasDeChute.append(letra)
                condicaoAcerto, chuteInicial = verificarChute(palavraSecreta, letra, letrasDeChute)

                if condicaoAcerto:
                    correto(chuteInicial)
                else:
                    incorreto(chuteInicial,erros)
                    erros += 1
                    desenhoForca(erros)
                    input("Press enter to continue...")
                    limparTela()
        else:
            print("Opção Inválida")
            input("Press enter to continue...")
            limparTela()
    
    if chuteInicial == palavraSecreta:
        noticiaVencedor()
        try:
            vencedor(desafiante, competidor, palavraSecreta) 
        except:
            amigos()
            vencedor(desafiante, competidor, palavraSecreta)
    
    elif erros == 6:
        noticiaPerdedor()
        try:
            vencedor(desafiante, competidor, palavraSecreta)
        except:
            amigos()
            vencedor(desafiante, competidor, palavraSecreta)
