from __future__ import annotations

from typing import TYPE_CHECKING
from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .__init__ import ClimbWorld

ITEM_NAME_TO_ID = {
    # Champs
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

    # Fuses
    "Double Down": 19,
    "Juggernaut": 20,
    "Sidekick": 21,
    "2X Assist": 22,
    "Freestyle": 23,
    "Teamfight": 24,

    # Abilities
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

    # One of One Augments
    "Thick Skin": 200,
    "Thicker Skin": 201,
    "Thickest Skin": 202,
    "Shield": 203,
    "Focused Impact": 204,
    "I'm Angry!": 205,
    "Turtle Parry God": 206,
    "Instant Charge": 207,
    "Open Cancel": 208,
    "Life Is Meter": 209,
    "Defense Discount": 210,
    "Friend Zone": 211,
    "Free At Last": 212,
    "Just Guess Who Cares": 213,
    "Rise and Shine": 214,
    "Real Pushy": 215,
    "Shield Breaker": 216,
    "Parry for Free": 217,
    "Debt Collector": 218,
    "Don't Go Up There": 219,
    "Infinite Disrespect": 220,
    "No-Kizeme": 221,

    # Stackable Augments
    "Power Of Friendship": 222,
    "Let's Shake On It": 223,
    "Fast Friends": 224,
    "Chip Chop": 225,
    "Bloodthirsty": 226,
    "Poison On Hit": 227,
    "Mash Harder": 228,
    "Butter Thief": 229,
    "Meter On Taunt": 230,
    "Energize": 231,
    "Laugh It Off": 232,
    "Damage Up Up": 233,
    "Damage Up": 234,
    "Hit Me!": 235,
    "Built Different": 236,
    "Hands Off!": 237,
    "Roll For Crit!": 238,

    # Optional Augments
    "Shadow": 239,
    "Floor Is Lava": 240,
    "Hold W To Block": 241,
    "Wild Pulse": 242,
    "First To Ten": 243,
    "Destroyer": 244,

    # Filler Augments
    "Abundance": 245,
    "Get Healthy": 246,
    "Get Healthier": 247,
    "Get Healthiest": 248,

    # Filler + Event ID
    "LP": 500,
    "Win": 501,
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "Ahri": ItemClassification.progression,
    "Akali": ItemClassification.progression,
    "Blitzcrank": ItemClassification.progression,
    "Braum": ItemClassification.progression,
    "Caitlyn": ItemClassification.progression,
    "Darius": ItemClassification.progression,
    "Ekko": ItemClassification.progression,
    "Illaoi": ItemClassification.progression,
    "Jinx": ItemClassification.progression,
    "Lux": ItemClassification.progression,
    "Samira": ItemClassification.progression,
    "Senna": ItemClassification.progression,
    "Sett": ItemClassification.progression,
    "Teemo": ItemClassification.progression,
    "Thresh": ItemClassification.progression,
    "Vi": ItemClassification.progression,
    "Warwick": ItemClassification.progression,
    "Yasuo": ItemClassification.progression,

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

    # One Off Augments
    "Thick Skin": ItemClassification.useful,
    "Thicker Skin": ItemClassification.useful,
    "Thickest Skin": ItemClassification.useful,
    "Shield": ItemClassification.useful,
    "Focused Impact": ItemClassification.useful,
    "I'm Angry!": ItemClassification.useful,
    "Turtle Parry God": ItemClassification.useful,
    "Instant Charge": ItemClassification.useful,
    "Open Cancel": ItemClassification.useful,
    "Life Is Meter": ItemClassification.useful,
    "Defense Discount": ItemClassification.useful,
    "Friend Zone": ItemClassification.useful,
    "Free At Last": ItemClassification.useful,
    "Just Guess Who Cares": ItemClassification.useful,
    "Rise and Shine": ItemClassification.useful,
    "Real Pushy": ItemClassification.useful,
    "Shield Breaker": ItemClassification.useful,
    "Parry for Free": ItemClassification.useful,
    "Debt Collector": ItemClassification.useful,
    "Don't Go Up There": ItemClassification.useful,
    "Infinite Disrespect": ItemClassification.useful,
    "No-Kizeme": ItemClassification.useful,

    # Stackable Augments
    "Power Of Friendship": ItemClassification.useful,
    "Let's Shake On It": ItemClassification.useful,
    "Fast Friends": ItemClassification.useful,
    "Chip Chop": ItemClassification.useful,
    "Bloodthirsty": ItemClassification.useful,
    "Poison On Hit": ItemClassification.useful,
    "Mash Harder": ItemClassification.useful,
    "Butter Thief": ItemClassification.useful,
    "Meter On Taunt": ItemClassification.useful,
    "Energize": ItemClassification.useful,
    "Laugh It Off": ItemClassification.useful,
    "Damage Up Up": ItemClassification.useful,
    "Damage Up": ItemClassification.useful,
    "Hit Me!": ItemClassification.useful,
    "Built Different": ItemClassification.useful,
    "Hands Off!": ItemClassification.useful,
    "Roll For Crit!": ItemClassification.useful,

    # Optional Augments
    "Shadow": ItemClassification.useful,
    "Floor Is Lava": ItemClassification.useful,
    "Hold W To Block": ItemClassification.useful,
    "Wild Pulse": ItemClassification.useful,
    "First To Ten": ItemClassification.useful,
    "Destroyer": ItemClassification.useful,

    # Filler Augments
    "Abundance": ItemClassification.filler,
    "Get Healthy": ItemClassification.filler,
    "Get Healthier": ItemClassification.filler,
    "Get Healthiest": ItemClassification.filler,

    "LP": ItemClassification.filler,
    "Win": ItemClassification.progression,


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

AUGMENTS = {
    "Thick Skin", # HP
    "Thicker Skin", # HP
    "Thickest Skin", # HP
    "Shield", # Persistent 1 hit of armor
    "Focused Impact", # H hold = armor + can be dash cancelled
    "I'm Angry!", # Fury always active, health drain
    "Turtle Parry God", # Hold parry input to keep parry window
    "Instant Charge", # Most reach instant
    "Open Cancel", # Stack 1x for specials, Supers replaced by Normal attack cancelling to each other
    "Life Is Meter", # Life instead of super meter
    "Defense Discount", # Parry cost 50% less, gives 50% less meter
    "Friend Zone", # Zero team cd
    "Free At Last", # Super assist needs no meter
    "Just Guess Who Cares", # Parry high or low to deflect any attack
    "Rise and Shine", # Getup attack size incr
    "Real Pushy", # Pushblock wallbounce
    "Shield Breaker", # atk breaks armor
    "Parry for Free", # No meter parry
    "Debt Collector", # Track meter spent and refund on next hit, lose all if hit
    "Don't Go Up There", # Anti air stops opp from jumping til hit
    "Infinite Disrespect", # Hyperarmor on taunt
    "No-Kizeme", # Getup attack on wakeup
}

STACKABLE_AUGMENTS = {
    "Power Of Friendship", # Stackable, assist dmg buff
    "Let's Shake On It", # Stackable, extra handshake tag
    "Fast Friends", # Stackable, assist cdr
    "Chip Chop", # Stackable, increased chip damage
    "Bloodthirsty", # Stackable, damage = health resto
    "Poison On Hit", # Stackable, add poison on hit
    "Mash Harder", # Stackable, normal attacks get 1 hit of armor
    "Butter Thief", # Stackable, steal super meter on hit
    "Meter On Taunt", # Stackable, gain 1 stock of meter on taunt
    "Energize", # Stackable, increase max Super Meter by 1
    "Laugh It Off", # Stackable, Restore hp on taunt
    "Damage Up Up", # Stackable, 10% atk buff
    "Damage Up", # Stackable, 5% atk buff
    "Hit Me!", # Stackable, Taunts have 1 hit of armor
    "Built Different",  # Stackable, assists 1 hit of armor
    "Hands Off!",  # Stackable, pushblock does damage
    "Roll For Crit!", # Stackable, incr both damage and chance
}

OPTIONAL_AUGMENTS = {
    "Shadow", # A shadow mirrors your attacks
    "Floor Is Lava", # Ground is dangerous, regain hp airborne
    "Hold W To Block", # No blocking, but dmg buff
    "Wild Pulse", # L = Wild Comboes
    "First To Ten", # Attacks remove 10% hp, start at full hp, break build buff
    "Destroyer", # Instant kill
}

BUFFS = {
    "Abundance", # Super infinite for the match
    "Get Healthy", # 10% Heal
    "Get Healthier", # 30% Heal
    "Get Healthiest", # 50% Heal
}

class ClimbItem(Item):
    game = "2XKO - The Climb"

def get_random_filler_item_name(world: ClimbWorld) -> str:
    rand_val = world.random.randint(1,8)

    # This is where I'd add traps, current thoughts include input scrambling, unbound input, random input
    if rand_val <= 1:
        return "LP"
    elif rand_val <= 3:
        return "Abundance"
    else:
        rand_heal = world.random.randint(1, 10)
        if rand_heal <= 1:
            return "Get Healthiest"
        elif rand_heal <= 3:
            return "Get Healthier"
        else:
            return "Get Healthy"

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

    # Check for ability sanity
    if world.options.ability_sanity:
        for x in ABILITIES:
            if x != ability:
                itempool.append(world.create_item(x))
                if "Progressive" in x:
                    itempool.append(world.create_item(x))

    # Start off with one of one augments
    for augment in AUGMENTS:
        itempool.append(world.create_item(augment))

    # Iterate on the chosen amount for each augment
    for x in range(world.options.power_of_friendship):
        itempool.append(world.create_item("Power Of Friendship"))

    for x in range(world.options.shake_on_it):
        itempool.append(world.create_item("Let's Shake On It"))

    for x in range(world.options.fast_friends):
        itempool.append(world.create_item("Fast Friends"))

    for x in range(world.options.chip_chop):
        itempool.append(world.create_item("Chip Chop"))

    for x in range(world.options.bloodthirsty):
        itempool.append(world.create_item("Bloodthirsty"))

    for x in range(world.options.poison_on_hit):
        itempool.append(world.create_item("Poison On Hit"))

    for x in range(world.options.mash_harder):
        itempool.append(world.create_item("Mash Harder"))

    for x in range(world.options.butter_thief):
        itempool.append(world.create_item("Butter Thief"))

    for x in range(world.options.meter_on_taunt):
        itempool.append(world.create_item("Meter On Taunt"))

    for x in range(world.options.energize):
        itempool.append(world.create_item("Energize"))

    for x in range(world.options.laugh_it_off):
        itempool.append(world.create_item("Laugh It Off"))

    for x in range(world.options.damage_up):
        # Weigh towards weaker buff
        rand_val = world.random.randint(1,4)
        if rand_val == 4:
            itempool.append(world.create_item("Damage Up Up"))
        else:
            itempool.append(world.create_item("Damage Up"))

    for x in range(world.options.hit_me):
        itempool.append(world.create_item("Hit Me!"))

    for x in range(world.options.built_different):
        itempool.append(world.create_item("Built Different"))

    for x in range(world.options.hands_off):
        itempool.append(world.create_item("Hands Off!"))

    for x in range(world.options.roll_for_crit):
        itempool.append(world.create_item("Roll For Crit!"))


    # Calculate the fillers needed
    number_of_items = len(itempool)

    number_unfilled_loc = len(world.multiworld.get_unfilled_locations(world.player))

    number_fillers = number_unfilled_loc - number_of_items

    itempool+= [world.create_filler() for _ in range(number_fillers)]

    # Finalize the itempool
    world.multiworld.itempool += itempool

