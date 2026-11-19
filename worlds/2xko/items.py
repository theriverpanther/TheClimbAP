from __future__ import annotations
from .options import StartingChampions, StartingFuse, AbilitySanity

from typing import TYPE_CHECKING, Dict, NamedTuple

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import ClimbWorld

ITEM_NAME_TO_ID = {
    "Ahri": 1,
    "Akali": 2,
    "Blitzcrank": 3,
    "Braum": 4,
    "Caitlyn": 5,
    "Darius": 6,
    "Ekko": 7,
    "Illaoi": 8,
    "Jinx": 9,
    "Lux": 10,
    "Samira": 11,
    "Senna": 12,
    "Sett": 13,
    "Teemo": 14,
    "Thresh": 15,
    "Vi": 16,
    "Warwick": 17,
    "Yasuo": 18,

    "Double Down": 19,
    "Juggernaut": 20,
    "Sidekick": 21,
    "2X Assist": 22,
    "Freestyle": 23,
    "Teamfight": 24,

    # Still Need to add the registry of augments to this list
    "Progressive S1": 100,
    "Progressive S2": 101,
    "Jump": 102,
    "Crouch": 103,
    "Block": 104,
    "Ultimate": 105,
    "Grab": 106,
    "Parry": 107,
    "Assist": 108,
    "Break": 109,
    "Taunt": 110,

    "LP": 200,
}

AUGMENTS = {

}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "Ahri": ItemClassification.progression | ItemClassification.useful,
    "Akali": ItemClassification.progression | ItemClassification.useful,
    "Blitzcrank": ItemClassification.progression | ItemClassification.useful,
    "Braum": ItemClassification.progression | ItemClassification.useful,
    "Caitlyn": ItemClassification.progression | ItemClassification.useful,
    "Darius": ItemClassification.progression | ItemClassification.useful,
    "Ekko": ItemClassification.progression | ItemClassification.useful,
    "Illaoi": ItemClassification.progression | ItemClassification.useful,
    "Jinx": ItemClassification.progression | ItemClassification.useful,
    "Lux": ItemClassification.progression | ItemClassification.useful,
    "Samira": ItemClassification.progression | ItemClassification.useful,
    "Senna": ItemClassification.progression | ItemClassification.useful,
    "Sett": ItemClassification.progression | ItemClassification.useful,
    "Teemo": ItemClassification.progression | ItemClassification.useful,
    "Thresh": ItemClassification.progression | ItemClassification.useful,
    "Vi": ItemClassification.progression | ItemClassification.useful,
    "Warwick": ItemClassification.progression | ItemClassification.useful,
    "Yasuo": ItemClassification.progression | ItemClassification.useful,

    "Double Down": ItemClassification.useful,
    "Juggernaut": ItemClassification.useful,
    "Sidekick": ItemClassification.useful,
    "2X Assist": ItemClassification.useful,
    "Freestyle": ItemClassification.useful,
    "Teamfight": ItemClassification.useful,

    "Progressive S1": ItemClassification.progression,
    "Progressive S2": ItemClassification.progression,
    "Jump": ItemClassification.progression,
    "Crouch": ItemClassification.progression,
    "Block": ItemClassification.progression,
    "Ultimate": ItemClassification.progression,
    "Grab": ItemClassification.progression,
    "Parry": ItemClassification.progression,
    "Assist": ItemClassification.progression,
    "Break": ItemClassification.progression,
    "Taunt": ItemClassification.progression,

    "LP": ItemClassification.filler,
}

CHAMPIONS = {
    "Ahri",
    "Akali",
    "Blitzcrank",
    "Braum",
    "Caitlyn",
    "Darius",
    "Ekko",
    "Illaoi",
    "Jinx",
    "Lux",
    "Samira",
    "Senna",
    "Sett",
    "Teemo",
    "Thresh",
    "Vi",
    "Warwick",
    "Yasuo",
}

ABILITIES = {
    "Progressive S1",
    "Progressive S2",
    "Jump",
    "Crouch",
    "Block",
    "Ultimate",
    "Grab",
    "Parry",
    "Assist",
    "Break",
    "Taunt",
}

FUSES = {
    "Double Down",
    "Juggernaut",
    "Sidekick",
    "2X Assist",
    "Freestyle",
    "Teamfight",
}

class ClimbItem(Item):
    game = "2XkO - The Climb"

def get_random_filler_item_name(world: ClimbWorld) -> str:
    #  is where I'd add traps, will consider if I want to implement any at the moment.
    return "LP"

def create_item_with_correct_classification(world: ClimbWorld, name: str) -> ClimbItem:
    # Creates item based off of the name sent into the function
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    # If items need to have modular logic based on toggles, do it here

    return ClimbItem(name, classification, ITEM_NAME_TO_ID[name], world.player)

# Using the filler + classification helpers, actually add the items to the itempool
def create_all_items(world: ClimbWorld) -> None:

    # Give the players starting items

    main_champ = 0
    alt_champ = 1

    if len(world.options.starting_champions.value) < 2:
        if len(world.options.starting_champions.value) == 0:
            main_champ = world.random.choice(list(CHAMPIONS))
        else:
            main_champ = list(world.options.starting_champions.value)[0]
        alt_champ = main_champ
        while alt_champ == main_champ:
            alt_champ = world.random.choice(list(CHAMPIONS))
    elif len(world.options.starting_champions.value) == 2:
        main_champ = list(world.options.starting_champions.value)[0]
        alt_champ = list(world.options.starting_champions.value)[1]
    else:
        main_champ = world.random.choice(list(world.starting_champions.value))
        alt_champ = main_champ
        while main_champ == alt_champ:
            alt_champ = world.random.choice(list(world.starting_champions.value))

    world.push_precollected(world.create_item(main_champ))
    world.push_precollected(world.create_item(alt_champ))

    ability = -1
    if world.options.ability_sanity == 1:
        ability = world.random.choice(list(ABILITIES))

    if ability != -1:
        world.push_precollected(world.create_item(ability))

    fuse = -1
    if world.options.starting_fuse.value != 6:
        fuse = world.options.starting_fuse.current_key
        fuse = fuse.title()
        fuse = fuse.replace("_", " ")

    else:
        fuse = world.random.choice(list(FUSES))
    world.push_precollected(world.create_item(fuse))

    # Start the item pool with items that will always be in the pool
    itempool: list[Item] = []
    for x in CHAMPIONS:
        if x != main_champ and x != alt_champ:
            itempool.append(world.create_item(x))

    for x in FUSES:
        if x != fuse:
            itempool.append(world.create_item(x))

    # For each augment value range in the options menu, add augments corresponding to the count

    # Check for ability sanity
    if world.options.ability_sanity:
        for x in ABILITIES:
            if x != ability:
                itempool.append(world.create_item(x))
                if x < 2:
                    itempool.append(world.create_item(x))

    # Calculate the fillers needed
    number_of_items = len(itempool)

    number_unfilled_loc = len(world.multiworld.get_unfilled_locations(world.player))

    number_fillers = number_of_items - number_unfilled_loc

    itempool+= [world.create_filler() for _ in range(number_fillers)]

    # Finalize the itempool
    world.multiworld.itempool += itempool

