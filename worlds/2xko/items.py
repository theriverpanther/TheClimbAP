from __future__ import annotations

from typing import TYPE_CHECKING

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

class ClimbItem(Item):
    game = "2XkO - The Climb"

def get_random_filler_item_name(world: ClimbWorld) -> str:
    #  is where I'd add traps, will consider if I want to implement any at the moment.
    return "LP"

def create_item_with_correct_classification(world: ClimbWorld) -> ClimbItem:
    # Creates item based off of the name sent into the function
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    # If items need to have modular logic based on toggles, do it here

    return ClimbItem(name, classification, ITEM_NAME_TO_ID[name], world.player)

# Using the filler + classification helpers, actually add the items to the itempool
def create_all_items(world: ClimbWorld) -> None:

    # Start the item pool with items that will always be in the pool
    itempool: list[Item] = [
        world.create_item("Ahri"),
        world.create_item("Akali"),
        world.create_item("Blitzcrank"),
        world.create_item("Braum"),
        world.create_item("Caitlyn"),
        world.create_item("Darius"),
        world.create_item("Ekko"),
        world.create_item("Illaoi"),
        world.create_item("Jinx"),
        world.create_item("Lux"),
        world.create_item("Samira"),
        world.create_item("Senna"),
        world.create_item("Sett"),
        world.create_item("Teemo"),
        world.create_item("Thresh"),
        world.create_item("Vi"),
        world.create_item("Warwick"),
        world.create_item("Yasuo"),
        world.create_item("Double Down"),
        world.create_item("Juggernaut"),
        world.create_item("Sidekick"),
        world.create_item("2X Assist"),
        world.create_item("Freestyle"),
        world.create_item("Teamfight"),
    ]
    if world.options.ability_sanity:
        itempool.append(world.create_item("Progressive S1"))
        itempool.append(world.create_item("Progressive S1"))
        itempool.append(world.create_item("Progressive S2"))
        itempool.append(world.create_item("Progressive S2"))
        itempool.append(world.create_item("Jump"))
        itempool.append(world.create_item("Crouch"))
        itempool.append(world.create_item("Block"))
        itempool.append(world.create_item("Ultimate"))
        itempool.append(world.create_item("Grab"))
        itempool.append(world.create_item("Parry"))
        itempool.append(world.create_item("Assist"))
        itempool.append(world.create_item("Break"))
        itempool.append(world.create_item("Taunt"))

    # When options for augments are added, append to the list from this area
    # itempool+= [world.create_item("augment name") for _ in range(world.options.x_augment_count)]

    # Calculate the fillers needed
    number_of_items = len(itempool)

    number_unfilled_loc = len(world.multiworld.get_unfilled_locations(world.player))

    number_fillers = number_of_items - number_unfilled_loc

    itempool+= [world.create_filler() for _ in range(number_fillers)]

    # Finalize the itempool
    world.multiworld.itempool += itempool

    # Give the players starting items
    if world.options.starting_champion:
        startingChampion = world.create_item(world.options.starting_champion)

    if world.options.starting_fuse:
        startingFuse = world.create_item(world.options.starting_fuse)

