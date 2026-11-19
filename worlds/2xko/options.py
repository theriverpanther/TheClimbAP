from dataclasses import dataclass

from Options import OptionSet, Choice, Range, Toggle, DeathLink, PerGameCommonOptions, OptionGroup

# from .items import CHAMPIONS as CHAMPS

# class Ascendancy(Toggle):
"""
Rather than having your clear condition at the end of one run, opt to instead require an amount of ascendancies taken in order to gain a clear.
"""

# display_name: "Ascendancy"

class GoalCharacterCount(Range):
    """
    Determines your win condition based on the amount of leading champions that defeat the boss encounter.
    """
    display_name = "Character Win Count"
    range_start = 1
    range_end = 18
    default = 4

class AbilitySanity(Toggle):
    """
    Adds basic fighting abilities to the item pool, reducing base functionality to just Light, Medium, and Heavy Attacks.
    Drops include Jump, Crouch, Block, S1, S2, Supers, Ultimate, Grab, Parry, Assist, Break, and Taunt
    """
    display_name = "AbilitySanity"

class StartingChampions(OptionSet):
    """
    Choose your starting champions. If less than two champions are picked, champions will be randomly selected to bring the total to two starters.
    If greater than two are picked, your starting champions will be randomly selected from among the total list

    Roster: 'Ahri', 'Akali', 'Blitzcrank', 'Braum', 'Caitlyn', 'Darius', 'Ekko', 'Illaoi', 'Jinx', 'Lux',
    'Samira', 'Senna', 'Sett', 'Teemo', 'Thresh', 'Vi', 'Warwick', 'Yasuo'
    """

    display_name = "Starting Champions"
    valid_keys = ["Ahri","Akali","Blitzcrank","Braum","Caitlyn","Darius","Ekko","Illaoi",
                  "Jinx","Lux","Samira","Senna","Sett","Teemo","Thresh","Vi","Warwick","Yasuo"]
    default = ["Ahri", "Ekko"]
    valid_keys_casefold = False


class StartingFuse(Choice):
    """
    Choose which fuse to start with
    """
    display_name = "Starting Fuse"
    option_double_down = 0
    option_juggernaut = 1
    option_sidekick = 2
    option_2X_Assist = 3
    option_freestyle = 4
    option_teamfight = 5
    random = 6
    default = 0

class DeathLink(DeathLink):
    """Share deaths with other players in the multiworld. Losing sends a Death Link. Receiving one kills your active champion"""

@dataclass
class ClimbOptions(PerGameCommonOptions):
    goal_character_count: GoalCharacterCount
    ability_sanity: AbilitySanity
    starting_champions: StartingChampions
    starting_fuse: StartingFuse
    deathlink: DeathLink

option_groups = [
    OptionGroup(
        "Core Gameplay", [GoalCharacterCount, AbilitySanity]
    ),
    OptionGroup(
        "Starting Selection", [StartingChampions, StartingFuse]
    )
]

option_presets = {
    "Basic Progression": {
        "goal_character_count": 4,
        "ability_sanity": False,
        "starting_champions": ["Ahri","Ekko"],
        "starting_fuse": "Double Down",
        "deathlink": False,
    },
    "Hard Mode": {
        "goal_character_count": 18,
        "ability_sanity": True,
        "starting_champions": ["Ahri","Ekko"],
        "starting_fuse": "Juggernaut",
        "deathlink": True,
    }
}
