from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location
from rule_builder.rules import Has

from . import items

if TYPE_CHECKING:
    from __init__ import ClimbWorld

LOCATION_NAME_TO_ID = {
    # TO DO, determine how checks are hashed out (per character per progression, per node, etc)
    "Ahri 1": 1,
    "Ahri 2": 2,
    "Ahri 3": 3,
    "Ahri 4": 4,
    "Ahri 5": 5,
    "Ahri 6": 6,
    "Ahri 7": 7,
    "Ahri 8": 8,
    "Ahri 9": 9,
    "Ahri 10": 10,
    "Ahri 11": 11,
    "Ahri 12": 12,
    "Ahri Win": 13,
    "Akali 1": 14,
    "Akali 2": 15,
    "Akali 3": 16,
    "Akali 4": 17,
    "Akali 5": 18,
    "Akali 6": 19,
    "Akali 7": 20,
    "Akali 8": 21,
    "Akali 9": 22,
    "Akali 10": 23,
    "Akali 11": 24,
    "Akali 12": 25,
    "Akali Win": 26,
    "Blitzcrank 1": 27,
    "Blitzcrank 2": 28,
    "Blitzcrank 3": 29,
    "Blitzcrank 4": 30,
    "Blitzcrank 5": 31,
    "Blitzcrank 6": 32,
    "Blitzcrank 7": 33,
    "Blitzcrank 8": 34,
    "Blitzcrank 9": 35,
    "Blitzcrank 10": 36,
    "Blitzcrank 11": 37,
    "Blitzcrank 12": 38,
    "Blitzcrank Win": 39,
    "Braum 1": 40,
    "Braum 2": 41,
    "Braum 3": 42,
    "Braum 4": 43,
    "Braum 5": 44,
    "Braum 6": 45,
    "Braum 7": 46,
    "Braum 8": 47,
    "Braum 9": 48,
    "Braum 10": 49,
    "Braum 11": 50,
    "Braum 12": 51,
    "Braum Win": 52,
    "Caitlyn 1": 53,
    "Caitlyn 2": 54,
    "Caitlyn 3": 55,
    "Caitlyn 4": 56,
    "Caitlyn 5": 57,
    "Caitlyn 6": 58,
    "Caitlyn 7": 59,
    "Caitlyn 8": 60,
    "Caitlyn 9": 61,
    "Caitlyn 10": 62,
    "Caitlyn 11": 63,
    "Caitlyn 12": 64,
    "Caitlyn Win": 65,
    "Darius 1": 66,
    "Darius 2": 67,
    "Darius 3": 68,
    "Darius 4": 69,
    "Darius 5": 70,
    "Darius 6": 71,
    "Darius 7": 72,
    "Darius 8": 73,
    "Darius 9": 74,
    "Darius 10": 75,
    "Darius 11": 76,
    "Darius 12": 77,
    "Darius Win": 78,
    "Ekko 1": 79,
    "Ekko 2": 80,
    "Ekko 3": 81,
    "Ekko 4": 82,
    "Ekko 5": 83,
    "Ekko 6": 84,
    "Ekko 7": 85,
    "Ekko 8": 86,
    "Ekko 9": 87,
    "Ekko 10": 88,
    "Ekko 11": 89,
    "Ekko 12": 90,
    "Ekko Win": 91,
    "Illaoi 1": 92,
    "Illaoi 2": 93,
    "Illaoi 3": 94,
    "Illaoi 4": 95,
    "Illaoi 5": 96,
    "Illaoi 6": 97,
    "Illaoi 7": 98,
    "Illaoi 8": 99,
    "Illaoi 9": 100,
    "Illaoi 10": 101,
    "Illaoi 11": 102,
    "Illaoi 12": 103,
    "Illaoi Win": 104,
    "Jinx 1": 105,
    "Jinx 2": 106,
    "Jinx 3": 107,
    "Jinx 4": 108,
    "Jinx 5": 109,
    "Jinx 6": 110,
    "Jinx 7": 111,
    "Jinx 8": 112,
    "Jinx 9": 113,
    "Jinx 10": 114,
    "Jinx 11": 115,
    "Jinx 12": 116,
    "Jinx Win": 117,
    "Lux 1": 118,
    "Lux 2": 119,
    "Lux 3": 120,
    "Lux 4": 121,
    "Lux 5": 122,
    "Lux 6": 123,
    "Lux 7": 124,
    "Lux 8": 125,
    "Lux 9": 126,
    "Lux 10": 127,
    "Lux 11": 128,
    "Lux 12": 129,
    "Lux Win": 130,
    "Samira 1": 131,
    "Samira 2": 132,
    "Samira 3": 133,
    "Samira 4": 134,
    "Samira 5": 135,
    "Samira 6": 136,
    "Samira 7": 137,
    "Samira 8": 138,
    "Samira 9": 139,
    "Samira 10": 140,
    "Samira 11": 141,
    "Samira 12": 142,
    "Samira Win": 143,
    "Senna 1": 144,
    "Senna 2": 145,
    "Senna 3": 146,
    "Senna 4": 147,
    "Senna 5": 148,
    "Senna 6": 149,
    "Senna 7": 150,
    "Senna 8": 151,
    "Senna 9": 152,
    "Senna 10": 153,
    "Senna 11": 154,
    "Senna 12": 155,
    "Senna Win": 156,
    "Sett 1": 157,
    "Sett 2": 158,
    "Sett 3": 159,
    "Sett 4": 160,
    "Sett 5": 161,
    "Sett 6": 162,
    "Sett 7": 163,
    "Sett 8": 164,
    "Sett 9": 165,
    "Sett 10": 166,
    "Sett 11": 167,
    "Sett 12": 168,
    "Sett Win": 169,
    "Teemo 1": 170,
    "Teemo 2": 171,
    "Teemo 3": 172,
    "Teemo 4": 173,
    "Teemo 5": 174,
    "Teemo 6": 175,
    "Teemo 7": 176,
    "Teemo 8": 177,
    "Teemo 9": 178,
    "Teemo 10": 179,
    "Teemo 11": 180,
    "Teemo 12": 181,
    "Teemo Win": 182,
    "Thresh 1": 183,
    "Thresh 2": 184,
    "Thresh 3": 185,
    "Thresh 4": 186,
    "Thresh 5": 187,
    "Thresh 6": 188,
    "Thresh 7": 189,
    "Thresh 8": 190,
    "Thresh 9": 191,
    "Thresh 10": 192,
    "Thresh 11": 193,
    "Thresh 12": 194,
    "Thresh Win": 195,
    "Vi 1": 196,
    "Vi 2": 197,
    "Vi 3": 198,
    "Vi 4": 199,
    "Vi 5": 200,
    "Vi 6": 201,
    "Vi 7": 202,
    "Vi 8": 203,
    "Vi 9": 204,
    "Vi 10": 205,
    "Vi 11": 206,
    "Vi 12": 207,
    "Vi Win": 208,
    "Warwick 1": 209,
    "Warwick 2": 210,
    "Warwick 3": 211,
    "Warwick 4": 212,
    "Warwick 5": 213,
    "Warwick 6": 214,
    "Warwick 7": 215,
    "Warwick 8": 216,
    "Warwick 9": 217,
    "Warwick 10": 218,
    "Warwick 11": 219,
    "Warwick 12": 220,
    "Warwick Win": 221,
    "Yasuo 1": 222,
    "Yasuo 2": 223,
    "Yasuo 3": 224,
    "Yasuo 4": 225,
    "Yasuo 5": 226,
    "Yasuo 6": 227,
    "Yasuo 7": 228,
    "Yasuo 8": 229,
    "Yasuo 9": 230,
    "Yasuo 10": 231,
    "Yasuo 11": 232,
    "Yasuo 12": 233,
    "Yasuo Win": 234,
}

class ClimbLocation(Location):
    game = "2XKO - The Climb"

"""
    Attempt at making the dictionary procedural. Could work if the dict is too messy, even if it's meant to be a constant

def define_dict(self) -> None:
    champs = ["Ahri","Akali","Blitzcrank","Braum","Caitlyn","Darius","Ekko","Illaoi","Jinx","Lux","Samira","Senna","Sett","Teemo","Thresh","Vi","Warwick","Yasuo"]
    counter = 1
    for x in champs
        for y in range(13)
            LOCATION_NAME_TO_ID[champs[x] + " " + (y+1)] = counter
            counter++
"""



# Helper method to translate strings from dictionaries into their IDs
def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: ClimbWorld) -> None:
    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: ClimbWorld) -> None:
    # Place location checks into regions
    ahri = world.get_region("Ahri")
    akali = world.get_region("Akali")
    blitzcrank = world.get_region("Blitzcrank")
    braum = world.get_region("Braum")
    caitlyn = world.get_region("Caitlyn")
    darius = world.get_region("Darius")
    ekko = world.get_region("Ekko")
    illaoi = world.get_region("Illaoi")
    jinx = world.get_region("Jinx")
    lux = world.get_region("Lux")
    samira = world.get_region("Samira")
    senna = world.get_region("Senna")
    sett = world.get_region("Sett")
    teemo = world.get_region("Teemo")
    thresh = world.get_region("Thresh")
    vi = world.get_region("Vi")
    warwick = world.get_region("Warwick")
    yasuo = world.get_region("Yasuo")

    ahri_locs = get_location_names_with_ids(
        ["Ahri 1", "Ahri 2", "Ahri 3", "Ahri 4", "Ahri 5",
         "Ahri 6", "Ahri 7", "Ahri 8", "Ahri 9", "Ahri 10",
         "Ahri 11", "Ahri 12", "Ahri Win"]
    )

    ahri.add_locations(ahri_locs, ClimbLocation)

    akali_locs = get_location_names_with_ids(
        ["Akali 1", "Akali 2", "Akali 3", "Akali 4", "Akali 5",
         "Akali 6", "Akali 7", "Akali 8", "Akali 9", "Akali 10",
         "Akali 11", "Akali 12", "Akali Win"]
    )

    akali.add_locations(akali_locs, ClimbLocation)

    blitzcrank_locs = get_location_names_with_ids(
        ["Blitzcrank 1", "Blitzcrank 2", "Blitzcrank 3", "Blitzcrank 4", "Blitzcrank 5",
         "Blitzcrank 6", "Blitzcrank 7", "Blitzcrank 8", "Blitzcrank 9", "Blitzcrank 10",
         "Blitzcrank 11", "Blitzcrank 12", "Blitzcrank Win"]
    )

    blitzcrank.add_locations(blitzcrank_locs, ClimbLocation)

    braum_locs = get_location_names_with_ids(
        ["Braum 1", "Braum 2", "Braum 3", "Braum 4", "Braum 5",
         "Braum 6", "Braum 7", "Braum 8", "Braum 9", "Braum 10",
         "Braum 11", "Braum 12", "Braum Win"]
    )

    braum.add_locations(braum_locs, ClimbLocation)

    caitlyn_locs = get_location_names_with_ids(
        ["Caitlyn 1", "Caitlyn 2", "Caitlyn 3", "Caitlyn 4", "Caitlyn 5",
         "Caitlyn 6", "Caitlyn 7", "Caitlyn 8", "Caitlyn 9", "Caitlyn 10",
         "Caitlyn 11", "Caitlyn 12", "Caitlyn Win"]
    )

    caitlyn.add_locations(caitlyn_locs, ClimbLocation)

    darius_locs = get_location_names_with_ids(
        ["Darius 1", "Darius 2", "Darius 3", "Darius 4", "Darius 5",
         "Darius 6", "Darius 7", "Darius 8", "Darius 9", "Darius 10",
         "Darius 11", "Darius 12", "Darius Win"]
    )

    darius.add_locations(darius_locs, ClimbLocation)

    ekko_locs = get_location_names_with_ids(
        ["Ekko 1", "Ekko 2", "Ekko 3", "Ekko 4", "Ekko 5",
         "Ekko 6", "Ekko 7", "Ekko 8", "Ekko 9", "Ekko 10",
         "Ekko 11", "Ekko 12", "Ekko Win"]
    )

    ekko.add_locations(ekko_locs, ClimbLocation)

    illaoi_locs = get_location_names_with_ids(
        ["Illaoi 1", "Illaoi 2", "Illaoi 3", "Illaoi 4", "Illaoi 5",
         "Illaoi 6", "Illaoi 7", "Illaoi 8", "Illaoi 9", "Illaoi 10",
         "Illaoi 11", "Illaoi 12", "Illaoi Win"]
    )

    illaoi.add_locations(illaoi_locs, ClimbLocation)

    jinx_locs = get_location_names_with_ids(
        ["Jinx 1", "Jinx 2", "Jinx 3", "Jinx 4", "Jinx 5",
         "Jinx 6", "Jinx 7", "Jinx 8", "Jinx 9", "Jinx 10",
         "Jinx 11", "Jinx 12", "Jinx Win"]
    )

    jinx.add_locations(jinx_locs, ClimbLocation)

    lux_locs = get_location_names_with_ids(
        ["Lux 1", "Lux 2", "Lux 3", "Lux 4", "Lux 5",
         "Lux 6", "Lux 7", "Lux 8", "Lux 9", "Lux 10",
         "Lux 11", "Lux 12", "Lux Win"]
    )

    lux.add_locations(lux_locs, ClimbLocation)

    samira_locs = get_location_names_with_ids(
        ["Samira 1", "Samira 2", "Samira 3", "Samira 4", "Samira 5",
         "Samira 6", "Samira 7", "Samira 8", "Samira 9", "Samira 10",
         "Samira 11", "Samira 12", "Samira Win"]
    )

    samira.add_locations(samira_locs, ClimbLocation)

    senna_locs = get_location_names_with_ids(
        ["Senna 1", "Senna 2", "Senna 3", "Senna 4", "Senna 5",
         "Senna 6", "Senna 7", "Senna 8", "Senna 9", "Senna 10",
         "Senna 11", "Senna 12", "Senna Win"]
    )

    senna.add_locations(senna_locs, ClimbLocation)

    sett_locs = get_location_names_with_ids(
        ["Sett 1", "Sett 2", "Sett 3", "Sett 4", "Sett 5",
         "Sett 6", "Sett 7", "Sett 8", "Sett 9", "Sett 10",
         "Sett 11", "Sett 12", "Sett Win"]
    )

    sett.add_locations(sett_locs, ClimbLocation)

    teemo_locs = get_location_names_with_ids(
        ["Teemo 1", "Teemo 2", "Teemo 3", "Teemo 4", "Teemo 5",
         "Teemo 6", "Teemo 7", "Teemo 8", "Teemo 9", "Teemo 10",
         "Teemo 11", "Teemo 12", "Teemo Win"]
    )

    teemo.add_locations(teemo_locs, ClimbLocation)

    thresh_locs = get_location_names_with_ids(
        ["Thresh 1", "Thresh 2", "Thresh 3", "Thresh 4", "Thresh 5",
         "Thresh 6", "Thresh 7", "Thresh 8", "Thresh 9", "Thresh 10",
         "Thresh 11", "Thresh 12", "Thresh Win"]
    )

    thresh.add_locations(thresh_locs, ClimbLocation)

    vi_locs = get_location_names_with_ids(
        ["Vi 1", "Vi 2", "Vi 3", "Vi 4", "Vi 5",
         "Vi 6", "Vi 7", "Vi 8", "Vi 9", "Vi 10",
         "Vi 11", "Vi 12", "Vi Win"]
    )

    vi.add_locations(vi_locs, ClimbLocation)

    warwick_locs = get_location_names_with_ids(
        ["Warwick 1", "Warwick 2", "Warwick 3", "Warwick 4", "Warwick 5",
         "Warwick 6", "Warwick 7", "Warwick 8", "Warwick 9", "Warwick 10",
         "Warwick 11", "Warwick 12", "Warwick Win"]
    )

    warwick.add_locations(warwick_locs, ClimbLocation)

    yasuo_locs = get_location_names_with_ids(
        ["Yasuo 1", "Yasuo 2", "Yasuo 3", "Yasuo 4", "Yasuo 5",
         "Yasuo 6", "Yasuo 7", "Yasuo 8", "Yasuo 9", "Yasuo 10",
         "Yasuo 11", "Yasuo 12", "Yasuo Win"]
    )

    yasuo.add_locations(yasuo_locs, ClimbLocation)

def create_events(world: ClimbWorld) -> None:
    sorted_champs = sorted(items.CHAMPIONS)
    for x in sorted_champs:
        region = world.get_region(x)
        region.add_event(x + " Win Flag", "Win", location_type = ClimbLocation, item_type=items.ClimbItem)