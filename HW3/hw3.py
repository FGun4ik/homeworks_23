"""Module containing classes for a game."""


from typing import Any, Self


def checker(new_value: Any, classes: tuple[type] | type[Any]):
    """
    Check if the given value matches any of the specified types.

    Args:
        new_value (Any): The value to be checked.
        classes (tuple[type] | type[Any]): Acceptable types for the value.

    Raises:
        TypeError: Raised if the type of the value does not match any of the specified types.
    """
    if not isinstance(new_value, classes):
        value_type = type(new_value).__name__
        if isinstance(classes, tuple):
            cls_names = [class_.__name__ for class_ in classes]
        else:
            cls_names = classes.__name__
        raise TypeError(f'{new_value} of {value_type} should be {cls_names}')


class Weapon():
    """Class responsible for weapons in the game.

    Attributes:
        weapon_name (str): The name of the weapon.
        damage (int | float): The damage inflicted by the weapon.

    Methods:
        __init__(self, weapon_name: str, damage: int | float) -> None:
            Initializes new Weapon instance with the specified name and damage.
    """

    def __init__(self, weapon_name: str, damage: int | float) -> None:
        """Initialize a new Weapon instance with the specified name and damage.

        Args:
            weapon_name (str): The name of the weapon.
            damage (int | float): The damage inflicted by the weapon.
        """
        self.weapon_name = weapon_name
        self.damage = damage

    def __str__(self) -> str:
        """
        Display the name and characteristics a weapon.

        Returns:
            str: string with name of weapon.
        """
        return self.weapon_name

    @property
    def weapon_name(self) -> str:
        """Get the name of weapon.

        Returns:
            str: The name of weapon.
        """
        return self._weapon_name

    @property
    def damage(self) -> int | float:
        """Get the damage of the weapon.

        Returns:
            int | float: The damage of the weapon.
        """
        return self._damage

    @weapon_name.setter
    def weapon_name(self, new_weapon_name: str) -> None:
        """Set the name of weapon.

        Args:
            new_weapon_name (str): New name for the weapon_name variable.

        Raises:
            ValueError: error if name is empty
        """
        checker(new_weapon_name, (str))
        if new_weapon_name == '':
            raise ValueError(f'{new_weapon_name} should have name')
        self._weapon_name = new_weapon_name

    @damage.setter
    def damage(self, new_damage: int | float) -> None:
        """Set the damage of weapon.

        Args:
            new_damage (int | float): New damage for the damage variable.

        Raises:
            ValueError: error if damage is less than zero.
        """
        checker(new_damage, (int | float))
        if new_damage < 0:
            raise ValueError(f'Damage of {self.name} less than 0')
        self._damage = new_damage


class Unit:
    """
    A class representing a unit in a game.

    Attributes:
        name (str): The name of the unit.
        hp (int | float): The health points of the unit.
        weapon (Weapon): The weapon equipped by the unit.

    Methods:
        __init__(self, name: str, hp: int | float, weapon: Weapon) -> None:
            Initializes a new Unit instance.

        attack(self, target: 'Unit') -> None:
            Attack another unit with the equipped weapon.

            Args:
                target (Unit): The unit to attack.
    """

    def __init__(self, name: str, hp: int | float, weapon: Weapon) -> None:
        """
        Initialize a new Unit instance.

        Args:
            name (str): name of unit.
            hp(int | float): health of unit.
            weapon (Weapon): weapon of unit.
        """
        self.name = name
        self.hp = hp
        self.weapon = weapon

    @property
    def name(self) -> str:
        """
        Get the name of the unit.

        Returns:
            str: The name of the unit.
        """
        return self._name

    @property
    def hp(self) -> int | float:
        """
        Get the health of the unit.

        Returns:
            int | float: The health of the unit.
        """
        return self._hp

    @property
    def weapon(self) -> Weapon:
        """Get the weapon of the unit.

        Returns:
            Weapon: The weapon_name.
        """
        return self._weapon

    @name.setter
    def name(self, new_name: str) -> None:
        """Set the name of the unit.

        Args:
            new_name (str): New name value to assign to the name variable.

        Raises:
            ValueError: error if nam is empty.
        """
        checker(new_name, (str))
        if new_name == '':
            raise ValueError(f'{new_name} should have name')
        self._name = new_name

    @hp.setter
    def hp(self, new_hp: int | float) -> None:
        """Set the health of the unit.

        Args:
            new_hp (int|float): New health value to assign to the hp variable.

        Raises:
            ValueError: error if hp less than 0.
        """
        checker(new_hp, (int | float))
        if new_hp < 0:
            raise ValueError(f'Health {self.hp} less than 0')
        self._hp = new_hp

    @weapon.setter
    def weapon(self, new_weapon: Weapon) -> None:
        """Set the weapon of the unit.

        Args:
            new_weapon (Weapon): New weapon value for the weapon variable.
        """
        checker(new_weapon, (Weapon))
        self._weapon = new_weapon

    def attack(self, target: 'Unit') -> None:
        """Attack the target unit.

        Args:
            target (Unit): The unit to attack.

        Returns:
                Attack info
        """
        checker(target, (Unit))
        return (f'{self.name} attacks {target.name}')


class Player(Unit):
    """
    A class representing a player unit in a game.

    Attributes:
        name (str): The name of the player.
        hp (int | float): The health points of the player.
        weapon (Weapon): The weapon equipped by the player.
        level (int): The level of the player.

    Methods:
        __init__(self, name: str, hp: int | float,
        weapon: Weapon, level: int) -> None:
    """

    def __init__(self, name: str, hp: int | float, weapon: Weapon, lvl: int) -> None:
        """
        Initialize a new Player instance.

        Args:
            name (str): name of unit.
            hp(int | float): health of unit.
            weapon (Weapon): weapon of unit.
            lvl(int): lvl of unit
        """
        super().__init__(name, hp, weapon)
        self.lvl = lvl

    @property
    def lvl(self) -> int:
        """Get the level of the player.

        Returns:
            int: The level of the player.
        """
        return self._lvl

    @lvl.setter
    def lvl(self, new_lvl: int) -> None:
        """Set the level of the player.

        Args:
            new_lvl (int): New level value to assign to the level variable.

        Raises:
            ValueError: error if lvl less than 0.
        """
        checker(new_lvl, (int))
        if new_lvl < 0:
            raise ValueError(f'Level {self.lvl} less than 0')
        self._lvl = new_lvl


class Enemy(Unit):
    """A class representing an enemy unit in a game.

    Attributes:
        name (str): The name of the enemy.
        hp (int | float): The health points of the enemy.
        weapon (Weapon): The weapon equipped by the enemy.
    """


class Game:
    """A class representing a game instance.

    Attributes:
        players (list): A list of player objects in the game.
        weapons (list): A list of weapon objects available in the game.
        enemies (list): A list of enemy objects in the game.

    Methods:
        __init__(self) -> None:
            Initializes a new Game instance.
        add_player(self, player: Player) -> None:
            Adds a player to the game.
        remove_player(self, player: Player) -> None:
            Removes a player from the game.
        add_weapon(self, weapon: Weapon) -> None:
            Adds a weapon to the game.
        remove_weapon(self, weapon: Weapon) -> None:
            Removes a weapon from the game.
        add_enemy(self, enemy: Enemy) -> None:
            Adds an enemy to the game.
        remove_enemy(self, enemy: Enemy) -> None:
            Removes an enemy from the game.
    """

    def __init__(self, players: list[Player], weapons: list[Weapon], enemies: list[Enemy]) -> None:
        """
        Initialize a new Game instance.

        Args:
            players (list[Player]): The list of players participating in the game.
            weapons (list[Weapon]): The list of weapons available in the game.
            enemies (list[Enemy]): The list of enemies in the game.
        """
        self._players = players
        self._weapons = weapons
        self._enemies = enemies

    def __iadd__(self, new_obj: Player | Weapon | Enemy) -> Self:
        """
        Add new object.

        Args:
            new_obj (Player | Weapon | Enemy): new object to add.

        Raises:
            TypeError: error if new_object not Player|Weapon|Enemy.

        Returns:
            Self: new_obj.
        """
        if isinstance(new_obj, Player):
            self.add_player(new_obj)
        elif isinstance(new_obj, Weapon):
            self.add_weapon(new_obj)
        elif isinstance(new_obj, Enemy):
            self.add_enemy(new_obj)
        else:
            raise TypeError('Unsupported type')
        return self

    def __isub__(self, old_obj: Player | Weapon | Enemy) -> Self:
        """
        Remove old object.

        Args:
            old_obj(Player | Weapon | Enemy): object for remove

        Raises:
            TypeError: error if new_obj is not Player | Weapon | Enemy.

        Returns:
            Self: old object
        """
        if old_obj.__class__.__name__ == Player.__name__:
            self.remove_player(old_obj)
        elif old_obj.__class__.__name__ == Weapon.__name__:
            self.remove_weapon(old_obj)
        elif old_obj.__class__.__name__ == Enemy.__name__:
            self.remove_enemy(old_obj)
        else:
            old_type_obj = type(old_obj)
            raise TypeError(f'{old_type_obj} should be Player | Weapon | Enemy')
        return self

    @property
    def players(self) -> list[Player]:
        """
        Get the list of players.

        Returns:
            list[Player]: The list of players.
        """
        return self._players

    @property
    def weapons(self) -> list[Weapon]:
        """Get the list of weapons.

        Returns:
            list[Weapon]: The list of weapons.
        """
        return self._weapons

    @property
    def enemies(self) -> list[Enemy]:
        """Get the list of enemies.

        Returns:
            list[Enemy]: The list of enemies.
        """
        return self._enemies

    def add_player(self, player: Player) -> None:
        """Add a player to the game.

        Args:
            player (Player): The player object to add.
        """
        self._players.append(player)

    def remove_player(self, player: Player) -> None:
        """Remove a player from the game.

        Args:
            player (Player): The player object to remove.
        """
        self._players.remove(player)

    def add_weapon(self, weapon: Weapon) -> None:
        """Add a weapon to the game.

        Args:
            weapon (Weapon): The weapon object to add.
        """
        self._weapons.append(weapon)

    def remove_weapon(self, weapon: Weapon) -> None:
        """Remove a weapon from the game.

        Args:
            weapon (Weapon): The weapon object to remove.
        """
        self._weapons.remove(weapon)

    def add_enemy(self, enemy: Enemy) -> None:
        """Add an enemy to the game.

        Args:
            enemy (Enemy): The enemy object to add.
        """
        self._enemies.append(enemy)

    def remove_enemy(self, enemy: Enemy) -> None:
        """Remove an enemy from the game.

        Args:
            enemy (Enemy): The enemy object to remove.
        """
        self._enemies.remove(enemy)
