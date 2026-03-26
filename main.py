import random
import string
from rich.panel import Panel
from rich.align import Align
from rich import box
from rich import print
from rich.traceback import install

install()


def mostrar_menu():
    menu = Panel(
        Align.center(
            "[bold green]GERADOR DE SENHAS[/]\n\n"
            "[cyan]1[/] Gerar senha\n"
            "[cyan]2[/] Sobre\n"
            "[cyan]0[/] Sair\n"
        ),
        title="[bold yellow]MENU PRINCIPAL[/]",
        border_style="blue",
        box=box.DOUBLE,
        width=50
    )

    print(menu)


def gerar_senha():
    # Verifica se o que foi digitado é um número inteiro, caso não seja, pedirá para digitar novamente.
    while True:
        try:
            tamanho = int(input("Qual o tamanho da senha desejada? "))

            if tamanho < 8:
                print(
                    f"[bold red]A senha deve ter no mínimo 8 caracteres, TENTE NOVAMENTE!!!")
                continue

            break

        except ValueError:
            print(f"[bold red]Por favor, digite apenas números! [/]")

    # Dá ao código a opção de todos os caratecteres(aA, 123 e #@!).
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # Garante que a senha terá pelo menos um caractere de cada.
    senha = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]

    for i in range(tamanho - 4):
        caractere = random.choice(caracteres)
        senha.append(caractere)

    random.shuffle(senha)

    senha_final = "".join(senha)

    print(f"Senha segura: [bold green]{senha_final}[/]")

    continuar = input(
        f"Deseja reutilizar o programa?(s/n) ").lower()

    if continuar != "s":
        print("[white on blue]Obrigado por utilizar o gerador de senha by: droLz1n.[/]")
        return False
    else:
        return True


while True:
    mostrar_menu()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print(f"[purple]Gerando senha...[/]\n")

        continuar = gerar_senha()

        if not continuar:
            break

    elif opcao == "2":
        print(f"[purple]Projeto de gerador de senhas com Python.[/]\n")

    elif opcao == "0":
        print(f"[bold red]Saindo...[/]")
        break
    else:
        print(f"[bold red]Opção inválida!")
