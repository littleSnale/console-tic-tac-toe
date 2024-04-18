import os


# константа (переменная которую не будем менять) lines с линиями
LINES = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
)
BOARD_COLOR = '\033[0;34m'
X_COLOR = '\033[0;32m'
O_COLOR = '\033[0;35m'


def main():
    # таблица
    windows = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    is_working = True
    # windows[2] = 'x'
    print(f'Приветствую в крестиках-ноликах!')
    input('Нажмите ENTER для начала')
    os.system('cls')
    print_table(windows)
    player = f'{X_COLOR}x{BOARD_COLOR}'
    while is_working:
        is_successful = replace(windows, player)
        if is_successful:  # если replace прошёл успешно, то передаётся ход
            # проверка победы
            if is_win(windows):
                print(f'Победил {player}')
                is_working = False
            elif is_draw(windows):
                print('Ничья')
                is_working = False

            # передача хода
            if player == f'{X_COLOR}x{BOARD_COLOR}':
                player = f'{O_COLOR}o{BOARD_COLOR}'
            else:
                player = f'{X_COLOR}x{BOARD_COLOR}'
        print_table(windows)


# печатает таблица на экран
def print_table(windows: list):
    print(BOARD_COLOR)
    print(f'_{windows[0]}_|_{windows[1]}_|_{windows[2]}_')
    print(f'_{windows[3]}_|_{windows[4]}_|_{windows[5]}_')
    print(f'_{windows[6]}_|_{windows[7]}_|_{windows[8]}_')


# возвращает True - если победа, False - если нет
def is_win(windows: list) -> bool:
    for line in LINES:
        if windows[line[0]] == windows[line[1]] == windows[line[2]]:
            return True
    return False


def is_draw(windows: list) -> bool:
    for window in windows:
        # если не занята
        if type(window) is int:
            return False
    return True


# ставит x и o в ячейки
def replace(windows: list, x_or_o: str) -> bool:
    # попробуем получить int input
    try:
        input_ = int(input(f'Куда поставить {x_or_o}: '))
    # в случае ошибки ValueError
    except ValueError:
        print('Введите число от 1 до 9')
        return False

    # проверяем что введена возможная цифра
    if input_ > 9 or input_ < 1:
        print('Введите число от 1 до 9')
        return False

    # проверяем занята ли клетка
    if windows[input_ - 1] == f'{X_COLOR}x{BOARD_COLOR}' or windows[input_ - 1] == f'{O_COLOR}o{BOARD_COLOR}':
        print('Клетка занята')
        # вернём информацию об ошибке
        return False
    else:
        windows[input_ - 1] = x_or_o
        os.system('cls')
        return True


if __name__ == '__main__':
    main()
    input('Нажмите enter для выхода')
