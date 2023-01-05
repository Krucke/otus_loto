from classes import create_cart, Player

from pytest import fixture, mark, param

EMPTY_CART = [
    ['','','','','','','','',''],
    ['','','','','','','','',''],
    ['','','','','','','','',''],
]

CART_WITH_NUMBERS = [
    [1,2,3,4,5,'','','',''],
    [1,2,3,4,5,'','','',''],
    [1,2,3,4,5,'','','',''],
]

@fixture
def cart():
    return create_cart()


@fixture
def player_instance(request):
    name, cart = request.param
    return Player(name, cart)


def test_create_cart_row_length(cart):
    assert len(cart) == 3


def test_create_cart_elements_in_row_length(cart):
    assert len(cart[0]) == 9


@mark.parametrize("cart_data, result", [
    ("cart", 12),
])    
def test_create_cart_empty_elements_in_row_length(cart_data, result, request):
    cart_data = request.getfixturevalue(cart_data)
    length_empty = 0
    for row in cart_data:
        for value in row:
            if not str(value).isdigit():
                length_empty += 1
    assert length_empty == result


class TestCartochka:

    @mark.parametrize("player_instance, result", [
        param(('player name', []), False),
        param(('player name 2', EMPTY_CART), True)
    ], indirect=['player_instance'])
    def test_is_cart_empty(self, player_instance, result):
        assert player_instance.cart.is_cart_empty() == result

    
    @mark.parametrize('player_instance, bochonok, result', [
        param(('player name', CART_WITH_NUMBERS), 10, False),
        param(('player name2', CART_WITH_NUMBERS), 1, True)
    ], indirect=['player_instance'])
    def test_is_value(self, player_instance, bochonok, result):
        assert player_instance.cart.is_value(bochonok) == result
