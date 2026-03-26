import random
import string
from rich import print
from rich.traceback import install
install()

#Verifica se o que foi digitado é um número inteiro, caso não seja, pedirá para digitar novamente.
while True:                                                     
    try:
        tamanho = int(input("Qual o tamanho da senha desejada? "))
        
        if tamanho < 8:
            print(f"[bold red]A senha deve ter no mínimo 8 caracteres")
            continue
        
        break
    
    except ValueError:
        print("[bold red]Por favor, digite apenas números![/]")
        
#Dá ao código a opção de todos os caratecteres(aA, 123 e #@!).
caracteres = string.ascii_letters + string.digits + string.punctuation   

#Garante que a senha terá pelo menos um caractere de cada.
senha = [                                                      
    random.choice(string.ascii_lowercase),
    random.choice(string.ascii_uppercase),
    random.choice(string.digits),
    random.choice(string.punctuation),
]

for _ in range(tamanho - 4):
    caractere = random.choice(caracteres)
    senha.append(caractere)
    
random.shuffle(senha)

senha_final = "".join(senha)

print(f"Senha segura: [bold green]{senha_final}[/]")