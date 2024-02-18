"""Test for hw3."""


import pytest

from hw3 import Enemy, Game, Player, Weapon

DAMAGE = 25
HP_PLAYER = 98.5
HP_ENEMY = 50
lvl = 6

TEST_WEAPON = (
    ('AK-47', DAMAGE),
    ('M4A4', DAMAGE),
)


@pytest.mark.parametrize('name_weapon, damage', TEST_WEAPON)
def test_weapon(name_weapon: str, damage: int | float) -> None:
    """
    Test funcion for weapon.

    Args:
        name_weapon (str): name of weapon.
        damage (int | float): damage of weapon.
    """
    assert Weapon(name_weapon, damage)


TEST_WEAPON_FAIL = (
    (HP_PLAYER, DAMAGE),
    (True, 'bimbimbambam'),
)


@pytest.mark.parametrize('name_weapon, damage', TEST_WEAPON_FAIL)
def test_weapon_fail(name_weapon: str, damage: int | float) -> None:
    """
    Test function for wrong weapon.

    Args:
        name_weapon (str): name of weapon.
        damage (int | float): damage of weapon.
    """
    with pytest.raises(TypeError):
        assert Weapon(name_weapon, damage)


TEST_PLAYER = (
    ('Boombl4', HP_PLAYER, Weapon('M4A4', DAMAGE), lvl),
    ('Dyrachyo', HP_PLAYER, Weapon('Microwave', DAMAGE), lvl),
)


@pytest.mark.parametrize('name, hp, weapon, lvl', TEST_PLAYER)
def test_player(name: str, hp: int | float, weapon: Weapon, lvl: int) -> None:
    """
    Test function for player.

    Args:
        name (str): name of player.
        hp (int | float): hp of player.
        weapon (Weapon): weapon of player.
        lvl (int): lvl of player.
    """
    assert Player(name, hp, weapon, lvl)


TEST_PLAYER_FAIL = (
    (DAMAGE, 'ZeroTwo', HP_PLAYER, '1234'),
    ('bim', 'bimbim', 'bam', 'bambam'),
)


@pytest.mark.parametrize('name, hp, weapon, lvl', TEST_PLAYER_FAIL)
def test_player_fail(name: str, hp: int | float, weapon: Weapon, lvl: int) -> None:
    """
    Test function for wrong player.

    Args:
        name (str): name of player.
        hp (int | float): hp of player.
        weapon (Weapon): weapon of player.
        lvl (int): lvl of player.
    """
    with pytest.raises(TypeError):
        assert Weapon(name, hp, weapon, lvl)


TEST_ENEMY = (
    ('Anti-mage', HP_ENEMY, Weapon('Mana-void', DAMAGE)),
    ('Kunkka', HP_ENEMY, Weapon('Sword', DAMAGE)),
)


@pytest.mark.parametrize('name, hp, weapon', TEST_ENEMY)
def test_enemy(name: str, hp: int | float, weapon: Weapon) -> None:
    """
    Test function for enemy.

    Args:
        name (str): name of enemy.
        hp (int | float): hp of enemy.
        weapon (Weapon): weapon of enemy.
    """
    assert Enemy(name, hp, weapon)


TEST_ENEMY_FAIL = (
    (HP_ENEMY, DAMAGE, 'bima'),
    (HP_PLAYER, 'bimbam', DAMAGE),
)


@pytest.mark.parametrize('name, hp, weapon', TEST_ENEMY_FAIL)
def test_enemy_fail(name: str, hp: int | float, weapon: Weapon) -> None:
    """
    Test function for wrong enemy.

    Args:
        name (str): name of enemy.
        hp (int | float): hp of enemy.
        weapon (Weapon): weapon of enemy
    """
    with pytest.raises(TypeError):
        assert Enemy(name, hp, weapon)


TEST_ADD_PLAYER = (
    [
        Player('Dima', HP_PLAYER, Weapon('Vilka', DAMAGE), lvl),
        Player('Sashka', HP_PLAYER, Weapon('Sosiska', DAMAGE), lvl),
    ],
    [Weapon('Bloodstone', DAMAGE), Weapon('Claymore', DAMAGE)],
    [
        Enemy('Bristleback', HP_ENEMY, Weapon('Spikes', DAMAGE)),
        Enemy('Windranger', HP_ENEMY, Weapon('Bow', DAMAGE)),
    ],
)


def test_add_player():
    """
    Test function for add_player.

    Asserts:
        True if new_player add.
    """
    game = Game(*TEST_ADD_PLAYER)
    new_player = Player('Abaddon', HP_PLAYER, Weapon('Mist Coil', DAMAGE), lvl)
    game += new_player
    assert new_player in game.players


TEST_REMOVE_PLAYER = (
    [
        Player('Boombl4', HP_PLAYER, Weapon('AWP', DAMAGE), lvl),
        Player('Dyrachyo', HP_PLAYER, Weapon('Microwave', DAMAGE), lvl),
    ],
    [Weapon('AK-47', DAMAGE), Weapon('M4A4', DAMAGE)],
    [
        Enemy('Anti-mage', HP_ENEMY, Weapon('Mana-void', DAMAGE)),
        Enemy('Kunkka', HP_ENEMY, Weapon('Sword', DAMAGE)),
    ],
)


def test_remove_player():
    """
    Test function for remove_player.

    Asserts:
        True if old_player remove.
    """
    game = Game(*TEST_REMOVE_PLAYER)
    old_player = Player('Boombl4', HP_PLAYER, Weapon('AWP', DAMAGE), lvl)
    game += old_player
    game -= old_player
    assert old_player not in game.players


TEST_ADD_WEAPON = (
    [
        Player('Miracle', HP_PLAYER, Weapon('Gaming Mouse', DAMAGE), lvl),
        Player('Lays', HP_PLAYER, Weapon('Potato', DAMAGE), lvl),
    ],
    [Weapon('Magic wand', DAMAGE), Weapon('Magic sword', DAMAGE)],
    [
        Enemy('Chaos Knight', HP_ENEMY, Weapon('Chaos Strike', DAMAGE)),
        Enemy('Legion Commander', HP_ENEMY, Weapon('Duel', DAMAGE)),
    ],
)


def test_add_weapon():
    """
    Test function for add_weapon.

    Asserts:
        True if new_weapon add.
    """
    game = Game(*TEST_ADD_WEAPON)
    new_weapon = Weapon('Shadow blade', DAMAGE)
    game += new_weapon
    assert new_weapon in game.weapons


TEST_REMOVE_WEAPON = (
    [
        Player('Miracle', HP_PLAYER, Weapon('Gaming Mouse', DAMAGE), lvl),
        Player('Lays', HP_PLAYER, Weapon('Potato', DAMAGE), lvl),
    ],
    [Weapon('Crystallys', DAMAGE), Weapon('Meteor Rain', DAMAGE)],
    [
        Enemy('Chaos Knight', HP_ENEMY, Weapon('Chaos Strike', DAMAGE)),
        Enemy('Legion Commander', HP_ENEMY, Weapon('Duel', DAMAGE)),
    ],
)


def test_remove_weapon():
    """
    Test function for remove_weapon.

    Asserts:
        True if old_weapon remove.
    """
    game = Game(*TEST_REMOVE_WEAPON)
    old_weapon = Weapon('Crystallys', DAMAGE)
    game += old_weapon
    game -= old_weapon
    assert old_weapon not in game.weapons


TEST_ADD_ENEMY = (
    [
        Player('Yosumo', HP_PLAYER, Weapon('Shadow strike', DAMAGE), lvl),
        Player('Sonya', HP_PLAYER, Weapon('Pen', DAMAGE), lvl),
    ],
    [Weapon('Huawei', DAMAGE), Weapon('Lamzu', DAMAGE)],
    [
        Enemy('Lion', HP_ENEMY, Weapon('Mana-drain', DAMAGE)),
        Enemy('Phoenix', HP_ENEMY, Weapon('Magic-fire', DAMAGE)),
    ],
)


def test_add_enemy():
    """
    Test function for add_enemy.

    Asserts:
        True if new_enemy add.
    """
    game = Game(*TEST_ADD_ENEMY)
    new_enemy = Enemy('Asta', HP_ENEMY, Weapon('Anti-magic swords', DAMAGE))
    game += new_enemy
    assert new_enemy in game.enemies


TEST_REMOVE_ENEMY = (
    [
        Player('Yosumo', HP_PLAYER, Weapon('Shadow strike', DAMAGE), lvl),
        Player('Sonya', HP_PLAYER, Weapon('Pen', DAMAGE), lvl),
    ],
    [Weapon('Lipton', DAMAGE), Weapon('Fire', DAMAGE)],
    [
        Enemy('Phoenix', HP_ENEMY, Weapon('Magic-fire', DAMAGE)),
        Enemy('Lion', HP_ENEMY, Weapon('Mana-drain', DAMAGE)),
    ],
)


def test_remove_enemy():
    """
    Test function for remove_enemy.

    Asserts:
        True if old_enemy remove.
    """
    game = Game(*TEST_REMOVE_ENEMY)
    old_enemy = Enemy('Lion', HP_ENEMY, Weapon('Mana-drain', DAMAGE))
    game += old_enemy
    game -= old_enemy
    assert old_enemy not in game.enemies
