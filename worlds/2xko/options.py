from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle

class Ascendancy(Toggle):
    """
    Rather than having your clear condition at the end of one run, opt to instead require an amount of ascendancies taken in order to gain a clear.
    """

    display_name: "Ascendancy"

class AbilitySanity(Toggle):
    """
    Adds basic fighting abilities to the item pool, reducing base functionality to just Light, Medium, and Heavy.
    Drops include Jump, Crouch, Block, S1, S2, Supers, Ultimate, Grab, Parry, Assist, Break, and Taunt
    """

    display_name: "AbilitySanity"

class StartingChampion(Choice):
    """
    Choose the starting champion pair
    """

    display_name: "Starting Champion"

class StartingFuse(Choice):
    """
    Choose the starting fuse
    """

    display_name: "Starting Fuse"