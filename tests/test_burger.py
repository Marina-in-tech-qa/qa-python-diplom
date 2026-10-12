import pytest

from unittest.mock import Mock

from praktikum.burger import Burger


def test_set_buns():
    burger = Burger()
    bun = Mock()

    burger.set_buns(bun)

    assert burger.bun is bun


def test_add_ingredient():
    burger = Burger()
    ingredient = Mock()

    burger.add_ingredient(ingredient)

    assert burger.ingredients == [ingredient]


def test_remove_ingredient():
    burger = Burger()
    ingredient_1 = Mock()
    ingredient_2 = Mock()

    burger.add_ingredient(ingredient_1)
    burger.add_ingredient(ingredient_2)

    burger.remove_ingredient(0)

    assert burger.ingredients == [ingredient_2]


def test_remove_ingredient_invalid_index():
    burger = Burger()
    ingredient = Mock()
    burger.add_ingredient(ingredient)

    with pytest.raises(IndexError):
        burger.remove_ingredient(5)


@pytest.mark.parametrize(
    "index, new_index, expected_order",
    [
        (0, 2, [1, 2, 0]),
        (2, 0, [2, 0, 1]),
        (1, 1, [0, 1, 2]),
    ]
)
def test_move_ingredient(index, new_index, expected_order):
    burger = Burger()
    ingredients = [Mock() for _ in range(3)]

    for ingredient in ingredients:
        burger.add_ingredient(ingredient)

    burger.move_ingredient(index, new_index)

    assert burger.ingredients == [
        ingredients[i] for i in expected_order
    ]


def test_get_price():
    burger = Burger()

    bun = Mock()
    bun.get_price.return_value = 100

    ingredient_1 = Mock()
    ingredient_1.get_price.return_value = 150

    ingredient_2 = Mock()
    ingredient_2.get_price.return_value = 50

    burger.set_buns(bun)
    burger.add_ingredient(ingredient_1)
    burger.add_ingredient(ingredient_2)

    assert burger.get_price() == 400



def test_get_price_without_ingredients():
    burger = Burger()

    bun = Mock()
    bun.get_price.return_value = 100

    burger.set_buns(bun)

    assert burger.get_price() == 200



def test_get_receipt():
    burger = Burger()

    bun = Mock()
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100

    ingredient = Mock()
    ingredient.get_type.return_value = "SAUCE"
    ingredient.get_name.return_value = "sour cream"
    ingredient.get_price.return_value = 50

    burger.set_buns(bun)
    burger.add_ingredient(ingredient)

    expected_receipt = (
        "(==== black bun ====)\n"
        "= sauce sour cream =\n"
        "(==== black bun ====)\n"
        "\n"
        "Price: 250"
    )

    assert burger.get_receipt() == expected_receipt


