import random
import time


def create_cart() -> list:
    cart: list = []
    exlude_values: list = []
    values = [i for i in range(1, 91)]
    for step in range(3):
        row = []
        for _ in range(9):
            value = random.choice([x for x in values if x not in exlude_values])
            exlude_values.append(value)
            row.append(value)

        row = sorted(row)
        exlude_empty_value = []
        for _ in range(4):
            random_replace = random.choice([x for x in range(9) if x not in exlude_empty_value])
            exlude_empty_value.append(random_replace)
            row[random_replace] = ''
        cart.append(row)
        
    return cart


def check_result(game, player, answer: str, boconok) -> bool:
    if answer == 'y' and not player.cart.is_value(boconok):
        print('Игра остановлена так как нет цифры в карте')
        game.is_game_end = True
        return False

    if answer == 'n' and player.cart.is_value(boconok):
        print('Игра остановлена так как есть цифра в карте')
        game.is_game_end = True
        return False
    
    return True


def check_for_player_win(game, player) -> bool:
    if player.cart.is_cart_empty():
        print(f'Победил игрок "{player.name}"!')
        game.is_game_end =True
        return True
    return False


class Cartochka():

    def __init__(self, cart, name_cart) -> None:
        self.cart = cart
        self.name_cart = name_cart

    def __str__(self) -> str:
        s = f'------ Карточка {self.name_cart} -----'
        for item in self.cart:
            s += f'\n {" ".join(map(str, item))}'
        s += '\n--------------------------'
        return s

    def is_value(self, value):
        for row in self.cart:
            if value in row:
                row[row.index(value)] = "+"
                return True
        return False

    
    def is_cart_empty(self):
        result = True
        for row in self.cart:
            for value in row:
                if isinstance(value, int):
                    return False
        return result


class Player():

    def __init__(self, name, is_pc=False):
        self.name = name
        self.is_pc = is_pc
        self.cart = Cartochka(create_cart(), self.name)


class Meshok():
    
    def __init__(self) -> None:
        self.meshok = [i for i in range(1, 91)]

    
    def get_bochonok(self) -> int:
        bochonok = random.choice([x for x in self.meshok])
        del self.meshok[self.meshok.index(bochonok)]
        return bochonok

    
    def __str__(self) -> str:
        return f'Осталось бочонков - {len(self.meshok)}'


class Game():

    def __init__(self, game_type, players) -> None:
        self.players = players
        self.game_type = game_type
        self.meshok = Meshok()
        self.is_game_end = False


    def brosok(self):
        boconok = self.meshok.get_bochonok()
        print(f'Новый бочонок: {boconok} ({self.meshok})\n')
        if self.game_type == 1:
            for player in self.players:
                print(player.cart)
            res = input(f'Зачеркнуть цифру {boconok}? (y/n)')
            checking_result = check_result(self, self.players[0], res, boconok)       
            self.players[1].cart.is_value(boconok)

            for player in self.players:
                is_player_win = check_for_player_win(self, player)
                if is_player_win:
                    return False
        
        if self.game_type == 2:
            for player in self.players:
                print(player.cart)
                res = input(f'Вопрос игроку "{player.name}". Зачеркнуть цифру {boconok}? (y/n)')
                checking_result = check_result(self, player, res, boconok)
                if not checking_result:
                    return False

                is_player_win = check_for_player_win(self, player)
                if is_player_win:
                    return False

        if self.game_type == 3:
            for player in self.players:
                print(player.cart)
                player.cart.is_value(boconok)
                is_player_win = check_for_player_win(self, player)
                if is_player_win:
                    return False
            time.sleep(1)