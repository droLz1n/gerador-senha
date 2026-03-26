# Gerador de Senhas no Terminal

Este projeto consiste em um gerador de senhas desenvolvido em Python, com interface no terminal utilizando a biblioteca Rich para aprimorar a visualização.

A aplicação permite ao usuário gerar senhas seguras de forma interativa, garantindo a inclusão de diferentes tipos de caracteres e validação de entrada.

## Funcionalidades

- Geração de senhas seguras com tamanho definido pelo usuário
- Validação de entrada (apenas números inteiros)
- Garantia de pelo menos:
  - uma letra minúscula
  - uma letra maiúscula
  - um número
  - um caractere especial
- Interface no terminal utilizando Rich (Panel, cores e formatação)
- Menu interativo com navegação simples
- Opção de reutilizar o programa ou encerrar a execução

## Tecnologias utilizadas

- Python
- Biblioteca Rich

## Estrutura do projeto

O projeto está organizado em funções principais:

- `mostrar_menu()`  
  Responsável por exibir o menu principal utilizando Panel.

- `gerar_senha()`  
  Responsável pela lógica de geração de senha, validação de entrada e controle de continuidade.

## Como executar o projeto

1. Clone o repositório:

```bash
git clone https://github.com/droLz1n/gerador-senha.git