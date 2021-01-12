import os
import sys
from random import randint

from colored import back, fore, style


def welcome():
    """Boas vindas ao jogo. E uma breve explicação de como o jogo funciona."""
    print(
        style.RESET
        + "\n"
        + 12 * "==="
        + "*** "
        + fore.LIGHT_BLUE
        + style.BOLD
        + "Bem vindo ao GUESS NUMBER"
        + style.RESET
        + " ***"
        + 12 * "==="
        + "\n"
    )
    print(
        fore.LIGHT_BLUE
        + style.BOLD
        + "★ "
        + style.RESET
        + "O jogo é bem simples. "
        + "Eu vou pensar em um número e voce vai tentar "
        + "adivinhar que número eu pensei.\n"
        + "  Dependendo do nível escolhido, o ranger de números "
        + "para a minha escolha vai aumentar.\n"
    )


def explanations():
    """Mostra as opções ao jogador."""
    print(
        fore.CYAN
        + style.BOLD
        + "\n-> "
        + style.RESET
        + "Escolha o nível que você deseja jogar:"
        + fore.LIGHT_BLUE
        + style.BOLD
        + "\n1 - Facil\n2 - Normal\n3 - Difícil\n"
        + style.RESET
    )
    print(
        fore.LIGHT_YELLOW
        + style.BOLD
        + "* "
        + style.RESET
        + "Você também pode digitar"
        + fore.LIGHT_BLUE
        + style.BOLD
        + " sair "
        + style.RESET
        + "a qualquer momento para encerrar o jogo.\n"
    )


def think(initial_number, final_number):
    """Informando ao jogador que o número foi pensando.

    Recebe 2 argumentos que representam o ranger de números(opções) para a
    escolha do computador.
    """
    print(
        fore.CYAN
        + style.BOLD
        + "\n-> "
        + style.RESET
        + "Acabei de pensar em um número entre "
        + fore.LIGHT_BLUE
        + style.BOLD
        + f"{initial_number}"
        + style.RESET
        + " e "
        + fore.LIGHT_BLUE
        + style.BOLD
        + f"{final_number}"
        + style.RESET
        + ". "
        + "Tente adivinhar que número foi esse!\n"
    )


def wecome_again():
    """Boas vindas para um novo jogo."""
    print(
        fore.CYAN
        + style.BOLD
        + "\n-> "
        + style.RESET
        + "Que bom que você gostou do jogo."
        + "Já pensei em outro número, tente adivinhar qual."
    )


def clear_screen():
    """Limpar a tela"""
    os.system("clear")


def play_again_or_exit():
    """Pergunta ao jogador se ele quer jogar novamente ou sair."""
    print(
        fore.CYAN
        + style.BOLD
        + "\n-> "
        + style.RESET
        + "Digite "
        + style.RESET
        + fore.BLUE
        + style.BOLD
        + "sim "
        + style.RESET
        + "para jogar novamente ou digite "
        + style.RESET
        + fore.BLUE
        + style.BOLD
        + "sair "
        + style.RESET
        + "para finalizar o jogo."
    )
    respo = input(
        fore.CYAN
        + style.BOLD
        + "\n-> "
        + style.RESET
        + "Deseja jogar novamente?"
        + fore.LIGHT_GREEN
        + style.BOLD
        + "   "
    )
    if respo.strip().lower() in ["sim", "si", "s"]:
        clear_screen()
        game_the_number()

    print(
        style.RESET
        + style.BOLD
        + fore.DEEP_PINK_3A
        + "ツ"
        + style.RESET
        + " Até a próxima!!!"
    )
    clear_screen()
    sys.exit()


def player_odds(final_number):
    """Recebe um argumento que define o número de chances do jogador na partida."""
    if final_number == 500:
        count = 9
        print(back.PURPLE_1B + style.BOLD + f"💣Você tem {count} chances.💣" + style.RESET)
    elif final_number == 100:
        count = 9
        print(back.PURPLE_1B + style.BOLD + f"💣Você tem {count} chances.💣" + style.RESET)
        # print(f"Você tem {count} chances.")
    else:
        count = 10
        print(back.PURPLE_1B + style.BOLD + f"💣Você tem {count} chances.💣" + style.RESET)
        # print(f"Você tem {count} chances.")
    return count


def player_chances_are_over(count):
    """Função para verificar se o jogador ainda possui chances.

    Caso não tenha mais chances o jogo é encerrado. E o jogador é
    perguntado se deseja jogar novamente.
    """
    if count < 1:
        print(
            back.DEEP_PINK_3A
            + style.BOLD
            + "\n☠ Você perdeu. Suas chances acabaram. 💀💀💀"
            + style.RESET
        )
        play_again_or_exit()
        # return
    else:
        print(back.PURPLE_1B + style.BOLD + f"💣Você tem {count} chances.💣" + style.RESET)
        # print(f"Você tem {count} chances.")


def want_game(guess):
    """Verificar se o jogador quer jogar ou sair do jogo."""
    if guess.strip().lower() == "sair":
        print(
            style.RESET
            + style.BOLD
            + fore.DEEP_PINK_3A
            + "\nツ"
            + style.RESET
            + "Até a próxima!!!\n"
        )
        clear_screen()
        sys.exit()


def check_nivel(choice_nivel, initial_number, final_number):
    """Checa o nível escolhido pelo jogador e retorna

    o número inicial e final para o ranger de números para
    escolha do computador.
    """
    if choice_nivel == 1:
        initial_number = 1
        final_number = 50
    elif choice_nivel == 2:
        initial_number = 1
        final_number = 100
    elif choice_nivel == 3:
        initial_number = -500
        final_number = 500

    return initial_number, final_number


def nivel_game(initial_number, final_number, random_number):
    """Função para verificar a escolha do nível que o jogador escolher."""
    while True:
        explanations()
        choice_nivel = input(
            fore.CYAN
            + style.BOLD
            + "\n-> "
            + style.RESET
            + "Digite "
            + style.RESET
            + fore.BLUE
            + style.BOLD
            + "1"
            + style.RESET
            + ", "
            + style.RESET
            + fore.BLUE
            + style.BOLD
            + "2"
            + style.RESET
            + ", "
            + style.RESET
            + fore.BLUE
            + style.BOLD
            + "3 "
            + style.RESET
            + "ou "
            + style.RESET
            + fore.BLUE
            + style.BOLD
            + "sair "
            + style.RESET
            + fore.YELLOW_1
            + style.BOLD
            + "❯❯"
            + style.RESET
            + fore.LIGHT_GREEN
            + style.BOLD
            + "   "
        )
        want_game(choice_nivel)
        choice_nivel = turn_guess_int(choice_nivel)

        if choice_nivel is None:
            choice_nivel_error()
            continue
        if 1 <= choice_nivel <= 3:
            initial_number, final_number = check_nivel(
                choice_nivel, initial_number, final_number
            )
            random_number = randint(initial_number, final_number)
            return initial_number, final_number, random_number
        else:
            choice_nivel_error()
            continue


def choice_nivel_error():
    """Mensagem de error na escolha do nível."""
    print(
        style.RESET
        + back.RED
        + "\nVocê deve digitar apenas 1, 2 ou 3 para escolher o nível do jogo.\n"
        + style.RESET
    )


def guess_error():
    """Mensagem para digitar um valor após o jogador ter errado no palpite."""
    print(
        fore.CYAN
        + style.BOLD
        + "\n-> "
        + style.RESET
        + "Digite um número "
        + style.RESET
        + fore.YELLOW_1
        + style.BOLD
        + "❯❯"
        + style.RESET
        + fore.LIGHT_GREEN
        + style.BOLD
        + "   "
    )


def turn_guess_int(guess):
    """transforma o argumento em inteiro."""
    try:
        guess = int(guess)
        return guess
    except ValueError:
        return None


def check_guess_ok(guess, random_number):
    """Checa se o jogador acertou o número."""
    if guess < random_number:
        print(
            style.RESET
            + fore.DEEP_PINK_3A
            + style.BOLD
            + "\n🚨 Errou!!!"
            + style.RESET
            + "\n☢ Seu palpite foi baixo."
        )

    elif guess > random_number:
        print(
            style.RESET
            + fore.DEEP_PINK_3A
            + style.BOLD
            + "\n🚨 Errou!!!"
            + style.RESET
            + "\n☢ Seu palpite foi maior."
        )

    else:
        print(style.RESET + fore.ORCHID + "\nParabéns!!! Você acertou! 😁" + style.RESET)
        return True
    return False


def game_the_number():
    """Função que faz o jogo acontecer."""
    initial_number = 1
    final_number = 1
    random_number = 1

    # welcome()

    initial_number, final_number, random_number = nivel_game(
        initial_number, final_number, random_number
    )
    think(initial_number, final_number)

    print("\n=================> BOA SORTE <=================\n")
    count = player_odds(final_number)

    while True:

        # print(count)
        guess = input(
            fore.CYAN
            + style.BOLD
            + "\n-> "
            + style.RESET
            + "Digite um número "
            + style.RESET
            + fore.YELLOW_1
            + style.BOLD
            + "❯❯"
            + style.RESET
            + fore.LIGHT_GREEN
            + style.BOLD
            + "   "
        )
        want_game(guess)
        guess = turn_guess_int(guess)

        if guess is None:
            guess_error()
            continue

        if initial_number <= guess <= final_number:
            guess_ok = check_guess_ok(guess, random_number)
        else:
            guess_error()
            continue

        if guess_ok:
            play_again_or_exit()
            """ initial_number, final_number, random_number = nivel_game(
                initial_number, final_number, random_number
            )
            think(initial_number, final_number)
            count = player_odds(final_number) """

        else:
            count = count - 1
            player_chances_are_over(count)
            continue


if __name__ == "__main__":
    welcome()
    game_the_number()
