# Hangman Game - MIT Problem Set 2 🎮
Este projeto é a minha implementação do jogo da Forca (Hangman) proposto no curso _6.100L Introduction to Computer Science and Programming in Python_ do **MIT OpenCourseWare**. As funções principais mantêm a nomenclatura original em inglês para garantir a compatibilidade com os testes automáticos do curso. Já as funções auxiliares foram criadas em português com o objetivo de facilitar o desenvolvimento e a leitura.

## 🚀 Funcionalidades

* **Lógica de Tentativas**: O jogador começa com 10 vidas.
* **Dedução Inteligente**: Perda de 2 pontos para vogais erradas e 1 ponto para consoantes.
* **Sistema de Ajuda (`!`)**: Permite revelar uma letra oculta ao custo de 3 tentativas. Se o jogador não possuir tentativas o suficiente, ele não perderá os pontos.
* **Cálculo da Pontuação**: Pontuação final baseada nas tentativas restantes e no número de letras únicas da palavra secreta.
* **Validação de Input**: Garante que o usuário insira apenas letras válidas do alfabeto.

## 🛠️ Como executar

1. Certifique-se de ter o Python instalado.
2. Mantenha o arquivo `words.txt` na mesma pasta que o script.
3. No terminal, execute:
   ```bash
   python hangman.py**

## 🛠️ Documentação Técnica

| Função | Descrição |
| :--- | :--- |
| `get_word_progress` | Gera a representação visual da palavra, exibindo as letras certas e ocultando as demais com asteriscos (`*`). |
| `get_available_letters` | Retorna uma string com as letras do alfabeto que o jogador ainda não utilizou. |
| `escolher_letra` | Seleciona aleatoriamente uma letra ainda não descoberta para a funcionalidade de ajuda.|
| `has_player_won` | Verifica se todas as letras da palavra secreta já foram adivinhadas. |

## 📝 Exemplo de Uso

```text
Welcome to Hangman!
A palavra secreta tem 4 letras
--------------
Você tem 10 tentativas sobrando
Letras disponíveis: abcdefghijklmnopqrstuvwxyz
Por favor adivinhe uma letra: a
Good guess: *a*a
--------------
Você tem 10 tentativas sobrando
Letras disponíveis: bcdefghijklmnopqrstuvwxyz
Por favor adivinhe uma letra: !
Letra revelada: c
--------------
Você tem 7 tentativas sobrando
Letras disponíveis: bdefghijklmnopqrstuvwxyz
Por favor adivinhe uma letra: s
Good guess: casa
--------------
Parabéns você ganhou em 3 tentativas
Sua pontuação para esse jogo é: 28
