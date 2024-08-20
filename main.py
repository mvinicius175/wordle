import random
import sys
from termcolor import colored

def menu() -> None:
    print("Bem vindo!!!")
    print("Digite uma palavra de 5 letras e aperte 'espaço'")

def ler_palavra_aleatoria() -> str:
    with open('palavras.txt', 'r') as file:
        palavras: list[str] = file.read().splitlines()
        return random.choice(palavras)

def tentar(palavra) -> None:
    for i in range(1, 7):
        tentativa: str = input("\n\n").upper()

        for j in range( min(len(tentativa), 5) ):
            if tentativa[j] == palavra[j]:
                print(colored(tentativa[j], 'green'), end='')
            elif tentativa[j] in palavra:
                print(colored(tentativa[j], 'yellow'), end='')
            else:
                print(tentativa[j], end='')

        if tentativa == palavra:
            print(colored(f"\nParabéns, você acertou a palavra em {i} tentativas!", 'green'))
            sys.exit(0)
    print(colored("\n\nVocê não conseguiu adivinhar a palavra :(", 'blue'))

def main() -> None:
    menu()
    palavra: str = ler_palavra_aleatoria()
    tentar(palavra)


if __name__ == "__main__":
    main()
