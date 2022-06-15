import os
def desenhoForca(erros):
    forca = """
    __
        |
        |
        -"""

    vazio = """
    """

    cabeca = """
        ()
    """

    tronco = """
        ()
        |
    """
    
    bracoEsquerdo = """
        ()
       /|
    """

    bracoDireito = """
        ()
       /|\\
    """

    pernaEsquerda = """
        ()
       /|\\
       /   
    """

    pernaDireita = """
        ()
       /|\\
       / \\  
    """
    
    chanceBoneco = [vazio, cabeca, tronco, bracoEsquerdo, bracoDireito, pernaEsquerda, pernaDireita,]

    print(forca + chanceBoneco[erros])

def noticiaVencedor():
    print("╔═════════════════╗")
    print("║ VOCÊ GANHOUUU! ♥║")
    print("╚═════════════════╝")

def noticiaPerdedor():
    print("Você perdeu!\n")
    print("(\__/)")
    print("(>-.-<)")
    print("(“)_(“)")

