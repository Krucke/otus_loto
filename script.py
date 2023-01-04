from classes import Player, Game


BEGIN_TEXT = f'''
1. Пользователь vs Компьютер
2. Пользователь vs Пользователь
3. Компьютер vs Компьютер
'''

def main():
    print('Добро пожаловать в игру "Лото". Пожалуйста, выберите тип игры (1-3)')
    type_game_input = int(input(BEGIN_TEXT))
    players = []
    if type_game_input not in range(1,4):
        print('Указано некорректное значение!')
        return False
    if type_game_input == 1:
        username = input('Пожалуйста, введите Ваше имя\n')
        players.append(Player(username))
        players.append(Player('Компьютер 1', True))
    if type_game_input == 2:
        count_of_players_input = int(input('Пожалуйста, укажите количество игроков (максимум 4)\n'))
        if count_of_players_input > 4 or count_of_players_input <= 0:
            print('Указано неверное количество игроков!')
            return False
        for player in range(1, count_of_players_input+1):
            username = input(f'Пожалуйста, введите имя {player} игрока\n')
            players.append(Player(username))

    if type_game_input == 3:
        players.append(Player('Компьютер 1', True))
        players.append(Player('Компьютер 2', True))

    game = Game(type_game_input, players)

    while not game.is_game_end:
        game.brosok()


if __name__ == '__main__':
    main()