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

class Shadow(Toggle):
    """Makes a clone follow you and duplicates your attacks."""
    display_name = "Enable Shadow Augment"

class FloorIsLava(Toggle):
    """Makes the ground persistently hurt, while being airborne heals you."""
    display_name = "Enable Floor Is Lava Augment"

class HoldWToBlock(Toggle):
    """Prevents blocking, but buffs damage."""
    display_name = "Enable W To Block Augment"

class WildPulse(Toggle):
    """Turns light attacks into Wild Combo chains by mashing L."""
    display_name = "Enable Wild Pulse Augment"

class FirstToTen(Toggle):
    """Allows break to build faster by reducing 10% hp per attack (with a full heal at match start)."""
    display_name = "Enable First To Ten Augment"

class Destroyer(Toggle):
    """An originally boss only augment that kills a champion in a single hit."""
    display_name = "Enable Destroyer Augment"

class PowerOfFriendship(Range):
    """Assist damage buff."""
    display_name = "Power of Friendship"
    range_start = 0
    range_end = 10
    default = 4

class ShakeOnIt(Range):
    """Stackable amount of extra handshake tags."""
    display_name = "Shake On It"
    range_start = 0
    range_end = 10
    default = 4

class FastFriends(Range):
    """Stackable cooldown reduction on assist actions."""
    display_name = "Fast Friends"
    range_start = 0
    range_end = 10
    default = 4

class ChipChop(Range):
    """Stackable quantity of chip damage added to each hit."""
    display_name = "Chip Chop"
    range_start = 0
    range_end = 10
    default = 4

class Bloodthirsty(Range):
    """Stackable amount of health healed on each attack dealt."""
    display_name = "Bloodthirsty"
    range_start = 0
    range_end = 10
    default = 4

class PoisonOnHit(Range):
    """Stackable amount of poison applied to the enemy on each attack dealt."""
    display_name = "Poison On Hit"
    range_start = 0
    range_end = 10
    default = 4

class MashHarder(Range):
    """Grants normal attacks 1 stack of armor per applied augment."""
    display_name = "Mash Harder"
    range_start = 0
    range_end = 10
    default = 4

class ButterThief(Range):
    """Steal super meter on hit, stacks increase quantity gained."""
    display_name = "Butter Thief"
    range_start = 0
    range_end = 10
    default = 4

class MeterOnTaunt(Range):
    """Gain 1 stock of meter per taunt per augment."""
    display_name = "Meter On Taunt"
    range_start = 0
    range_end = 10
    default = 4

class Energize(Range):
    """Increase Super Meter maximum by 1 per augment."""
    display_name = "Energize"
    range_start = 0
    range_end = 10
    default = 4

class LaughItOff(Range):
    """Restore a quantity of hp on taunt, stacks increase quantity."""
    display_name = "Laugh It Off"
    range_start = 0
    range_end = 10
    default = 4

class DamageUp(Range):
    """Flat increase damage dealt per augment. 75% chance to be a 5% buff, 25% chance to be a 10% buff"""
    display_name = "Damage Up"
    range_start = 0
    range_end = 20
    default = 8

class HitMe(Range):
    """Taunts gain 1 hit of armor per augment."""
    display_name = "Hit Me!"
    range_start = 0
    range_end = 10
    default = 4

class BuiltDifferent(Range):
    """Assists gain 1 hit of armor per augment."""
    display_name = "Built Different"
    range_start = 0
    range_end = 10
    default = 4

class HandsOff(Range):
    """Pushblock does damage, damage increases per augment."""
    display_name = "Hands Off!"
    range_start = 0
    range_end = 10
    default = 4

class RollForCrit(Range):
    """Hits have a chance to critical hit for increased damage, each augment increases chance and damage."""
    display_name = "Roll For Crit!"
    range_start = 0
    range_end = 10
    default = 4

class DeathLink(DeathLink):
    """Share deaths with other players in the multiworld. Losing sends a Death Link. Receiving one kills your active champion."""

@dataclass
class ClimbOptions(PerGameCommonOptions):
    goal_character_count: GoalCharacterCount
    ability_sanity: AbilitySanity
    starting_champions: StartingChampions
    starting_fuse: StartingFuse
    deathlink: DeathLink
    shadow: Shadow
    floor_is_lava: FloorIsLava
    hold_w_to_block: HoldWToBlock
    wild_pulse: WildPulse
    first_to_ten: FirstToTen
    destroyer: Destroyer
    power_of_friendship: PowerOfFriendship
    shake_on_it: ShakeOnIt
    fast_friends: FastFriends
    chip_chop: ChipChop
    bloodthirsty: Bloodthirsty
    poison_on_hit: PoisonOnHit
    mash_harder: MashHarder
    butter_thief: ButterThief
    meter_on_taunt: MeterOnTaunt
    energize: Energize
    laugh_it_off: LaughItOff
    damage_up: DamageUp
    hit_me: HitMe
    built_different: BuiltDifferent
    hands_off: HandsOff
    roll_for_crit: RollForCrit


option_groups = [
    OptionGroup(
        "Core Gameplay", [GoalCharacterCount, AbilitySanity]
    ),
    OptionGroup(
        "Starting Selection", [StartingChampions, StartingFuse]
    ),
    OptionGroup(
        "Augments", [Shadow, FloorIsLava, HoldWToBlock, WildPulse, FirstToTen, Destroyer,
                     PowerOfFriendship, ShakeOnIt, FastFriends, ChipChop, Bloodthirsty, PoisonOnHit,MashHarder,ButterThief,
                     MeterOnTaunt, Energize, LaughItOff, DamageUp, HitMe, BuiltDifferent, HandsOff, RollForCrit]
    ),
    OptionGroup(
        "Deathlink", [DeathLink]
    )
]

option_presets = {
    "Basic Progression": {
        "goal_character_count": 4,
        "ability_sanity": False,
        "starting_champions": ["Ahri","Ekko"],
        "starting_fuse": "Double Down",
        "deathlink": False,
        "shadow": True,
        "floor_is_lava": True,
        "hold_w_to_block": True,
        "wild_pulse": True,
        "first_to_ten": True,
        "destroyer": True,
        "power_of_friendship": 4,
        "shake_on_it": 4,
        "fast_friends": 4,
        "chip_chop": 4,
        "bloodthirsty": 4,
        "poison_on_hit": 4,
        "mash_harder": 4,
        "butter_thief": 4,
        "meter_on_taunt": 4,
        "energize": 4,
        "laugh_it_off": 4,
        "damage_up": 8,
        "hit_me": 4,
        "built_different": 4,
        "hands_off": 4,
        "roll_for_crit": 4,
    },
    "Hard Mode": {
        "goal_character_count": 18,
        "ability_sanity": True,
        "starting_champions": ["Ahri","Ekko"],
        "starting_fuse": "Juggernaut",
        "deathlink": True,
        "shadow": True,
        "floor_is_lava": True,
        "hold_w_to_block": True,
        "wild_pulse": True,
        "first_to_ten": True,
        "destroyer": False,
        "power_of_friendship": 2,
        "shake_on_it": 2,
        "fast_friends": 2,
        "chip_chop": 2,
        "bloodthirsty": 2,
        "poison_on_hit": 2,
        "mash_harder": 2,
        "butter_thief": 2,
        "meter_on_taunt": 2,
        "energize": 2,
        "laugh_it_off": 2,
        "damage_up": 4,
        "hit_me": 2,
        "built_different": 2,
        "hands_off": 2,
        "roll_for_crit": 2,
    }
}
