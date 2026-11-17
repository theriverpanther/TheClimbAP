from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from world import ClimbWorld

LOCATION_NAME_TO_ID = {
    # TO DO, determine how checks are hashed out (per character per progression, per node, etc)
    "Starting Champion 1": 1,
    "Starting Champion 2": 2,
    "Starting Fuse": 3,

    "Ahri 1": 4,
    "Ahri 2": 5,
    "Ahri 3": 6,
    "Ahri 4": 7,
    "Ahri 5": 8,
    "Ahri 6": 9,
    "Ahri 7": 10,
    "Ahri 8": 11,
    "Ahri 9": 12,
    "Ahri 10": 13,
    "Ahri 11": 14,
    "Ahri 12": 15,
    "Ahri 13": 16,
    "Akali 1": 17,
    "Akali 2": 18,
    "Akali 3": 19,
    "Akali 4": 20,
    "Akali 5": 21,
    "Akali 6": 22,
    "Akali 7": 23,
    "Akali 8": 24,
    "Akali 9": 25,
    "Akali 10": 26,
    "Akali 11": 27,
    "Akali 12": 28,
    "Akali 13": 29,
    "Blitzcrank 1": 30,
    "Blitzcrank 2": 31,
    "Blitzcrank 3": 32,
    "Blitzcrank 4": 33,
    "Blitzcrank 5": 34,
    "Blitzcrank 6": 35,
    "Blitzcrank 7": 36,
    "Blitzcrank 8": 37,
    "Blitzcrank 9": 38,
    "Blitzcrank 10": 39,
    "Blitzcrank 11": 40,
    "Blitzcrank 12": 41,
    "Blitzcrank 13": 42,
    "Braum": 43,
    "Braum 2": 44,
    "Braum 3": 45,
    "Braum 4": 46,
    "Braum 5": 47,
    "Braum 6": 48,
    "Braum 7": 49,
    "Braum 8": 50,
    "Braum 9": 51,
    "Braum 10": 52,
    "Braum 11": 53,
    "Braum 12": 54,
    "Braum 13": 55,
    "Caitlyn": 56,
    "Caitlyn 2": 57,
    "Caitlyn 3": 58,
    "Caitlyn 4": 59,
    "Caitlyn 5": 60,
    "Caitlyn 6": 61,
    "Caitlyn 7": 62,
    "Caitlyn 8": 63,
    "Caitlyn 9": 64,
    "Caitlyn 10": 65,
    "Caitlyn 11": 66,
    "Caitlyn 12": 67,
    "Caitlyn 13": 68,
    "Darius 1": 69,
    "Darius 2": 70,
    "Darius 3": 71,
    "Darius 4": 72,
    "Darius 5": 73,
    "Darius 6": 74,
    "Darius 7": 75,
    "Darius 8": 76,
    "Darius 9": 77,
    "Darius 10": 78,
    "Darius 11": 79,
    "Darius 12": 80,
    "Darius 13": 81,
    "Ekko 1": 82,
    "Ekko 2": 83,
    "Ekko 3": 84,
    "Ekko 4": 85,
    "Ekko 5": 86,
    "Ekko 6": 87,
    "Ekko 7": 88,
    "Ekko 8": 89,
    "Ekko 9": 90,
    "Ekko 10": 91,
    "Ekko 11": 92,
    "Ekko 12": 93,
    "Ekko 13": 94,
    "Illaoi 1": 95,
    "Illaoi 2": 96,
    "Illaoi 3": 97,
    "Illaoi 4": 98,
    "Illaoi 5": 99,
    "Illaoi 6": 100,
    "Illaoi 7": 101,
    "Illaoi 8": 102,
    "Illaoi 9": 103,
    "Illaoi 10": 104,
    "Illaoi 11": 105,
    "Illaoi 12": 106,
    "Illaoi 13": 107,
    "Jinx 1": 108,
    "Jinx 2": 109,
    "Jinx 3": 110,
    "Jinx 4": 111,
    "Jinx 5": 112,
    "Jinx 6": 113,
    "Jinx 7": 114,
    "Jinx 8": 115,
    "Jinx 9": 116,
    "Jinx 10": 117,
    "Jinx 11": 118,
    "Jinx 12": 119,
    "Jinx 13": 120,
    "Lux 1": 121,
    "Lux 2": 122,
    "Lux 3": 123,
    "Lux 4": 124,
    "Lux 5": 125,
    "Lux 6": 126,
    "Lux 7": 127,
    "Lux 8": 128,
    "Lux 9": 129,
    "Lux 10": 130,
    "Lux 11": 131,
    "Lux 12": 132,
    "Lux 13": 133,
    "Samira 1": 134,
    "Samira 2": 135,
    "Samira 3": 136,
    "Samira 4": 137,
    "Samira 5": 138,
    "Samira 6": 139,
    "Samira 7": 140,
    "Samira 8": 141,
    "Samira 9": 142,
    "Samira 10": 143,
    "Samira 11": 144,
    "Samira 12": 145,
    "Samira 13": 146,
    "Senna 1": 147,
    "Senna 2": 148,
    "Senna 3": 149,
    "Senna 4": 150,
    "Senna 5": 151,
    "Senna 6": 152,
    "Senna 7": 153,
    "Senna 8": 154,
    "Senna 9": 155,
    "Senna 10": 156,
    "Senna 11": 157,
    "Senna 12": 158,
    "Senna 13": 159,
    "Sett 1": 160,
    "Sett 2": 161,
    "Sett 3": 162,
    "Sett 4": 163,
    "Sett 5": 164,
    "Sett 6": 165,
    "Sett 7": 166,
    "Sett 8": 167,
    "Sett 9": 168,
    "Sett 10": 169,
    "Sett 11": 170,
    "Sett 12": 171,
    "Sett 13": 172,
    "Teemo 1": 173,
    "Teemo 2": 174,
    "Teemo 3": 175,
    "Teemo 4": 176,
    "Teemo 5": 177,
    "Teemo 6": 178,
    "Teemo 7": 179,
    "Teemo 8": 180,
    "Teemo 9": 181,
    "Teemo 10": 182,
    "Teemo 11": 183,
    "Teemo 12": 184,
    "Teemo 13": 185,
    "Thresh 1": 186,
    "Thresh 2": 187,
    "Thresh 3": 188,
    "Thresh 4": 189,
    "Thresh 5": 190,
    "Thresh 6": 191,
    "Thresh 7": 192,
    "Thresh 8": 193,
    "Thresh 9": 194,
    "Thresh 10": 195,
    "Thresh 11": 196,
    "Thresh 12": 197,
    "Thresh 13": 198,
    "Vi 1": 199,
    "Vi 2": 200,
    "Vi 3": 201,
    "Vi 4": 202,
    "Vi 5": 203,
    "Vi 6": 204,
    "Vi 7": 205,
    "Vi 8": 206,
    "Vi 9": 207,
    "Vi 10": 208,
    "Vi 11": 209,
    "Vi 12": 210,
    "Vi 13": 211,
    "Warwick 1": 212,
    "Warwick 2": 213,
    "Warwick 3": 214,
    "Warwick 4": 215,
    "Warwick 5": 216,
    "Warwick 6": 217,
    "Warwick 7": 218,
    "Warwick 8": 219,
    "Warwick 9": 220,
    "Warwick 10": 221,
    "Warwick 11": 222,
    "Warwick 12": 223,
    "Warwick 13": 224,
    "Yasuo 1": 225,
    "Yasuo 2": 226,
    "Yasuo 3": 227,
    "Yasuo 4": 228,
    "Yasuo 5": 229,
    "Yasuo 6": 230,
    "Yasuo 7": 231,
    "Yasuo 8": 232,
    "Yasuo 9": 233,
    "Yasuo 10": 234,
    "Yasuo 11": 235,
    "Yasuo 12": 236,
    "Yasuo 13": 237,
}

class ClimbLocation(Location):
    game = "2XKO - The Climb"

# Helper method to translate strings from dictionaries into their IDs
def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: ClimbWorld) -> None:
    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: ClimbWorld) -> None:
    # Place location checks into regions
    # Probably make each character have their own

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
         "Ahri 11", "Ahri 12", "Ahri 13"]
    )

    ahri.add_locations(ahri_locs, ClimbLocation)

    akali_locs = get_location_names_with_ids(
        ["Akali 1", "Akali 2", "Akali 3", "Akali 4", "Akali 5",
         "Akali 6", "Akali 7", "Akali 8", "Akali 9", "Akali 10",
         "Akali 11", "Akali 12", "Akali 13"]
    )

    akali.add_locations(akali_locs, ClimbLocation)

    blitzcrank_locs = get_location_names_with_ids(
        ["Blitzcrank 1", "Blitzcrank 2", "Blitzcrank 3", "Blitzcrank 4", "Blitzcrank 5",
         "Blitzcrank 6", "Blitzcrank 7", "Blitzcrank 8", "Blitzcrank 9", "Blitzcrank 10",
         "Blitzcrank 11", "Blitzcrank 12", "Blitzcrank 13"]
    )

    blitzcrank.add_locations(blitzcrank_locs, ClimbLocation)

    braum_locs = get_location_names_with_ids(
        ["Braum 1", "Braum 2", "Braum 3", "Braum 4", "Braum 5",
         "Braum 6", "Braum 7", "Braum 8", "Braum 9", "Braum 10",
         "Braum 11", "Braum 12", "Braum 13"]
    )

    braum.add_locations(braum_locs, ClimbLocation)

    caitlyn_locs = get_location_names_with_ids(
        ["Caitlyn 1", "Caitlyn 2", "Caitlyn 3", "Caitlyn 4", "Caitlyn 5",
         "Caitlyn 6", "Caitlyn 7", "Caitlyn 8", "Caitlyn 9", "Caitlyn 10",
         "Caitlyn 11", "Caitlyn 12", "Caitlyn 13"]
    )

    caitlyn.add_locations(caitlyn_locs, ClimbLocation)

    darius_locs = get_location_names_with_ids(
        ["Darius 1", "Darius 2", "Darius 3", "Darius 4", "Darius 5",
         "Darius 6", "Darius 7", "Darius 8", "Darius 9", "Darius 10",
         "Darius 11", "Darius 12", "Darius 13"]
    )

    darius.add_locations(darius_locs, ClimbLocation)

    ekko_locs = get_location_names_with_ids(
        ["Ekko 1", "Ekko 2", "Ekko 3", "Ekko 4", "Ekko 5",
         "Ekko 6", "Ekko 7", "Ekko 8", "Ekko 9", "Ekko 10",
         "Ekko 11", "Ekko 12", "Ekko 13"]
    )

    ekko.add_locations(ekko_locs, ClimbLocation)

    illaoi_locs = get_location_names_with_ids(
        ["Illaoi 1", "Illaoi 2", "Illaoi 3", "Illaoi 4", "Illaoi 5",
         "Illaoi 6", "Illaoi 7", "Illaoi 8", "Illaoi 9", "Illaoi 10",
         "Illaoi 11", "Illaoi 12", "Illaoi 13"]
    )

    illaoi.add_locations(illaoi_locs, ClimbLocation)

    jinx_locs = get_location_names_with_ids(
        ["Jinx 1", "Jinx 2", "Jinx 3", "Jinx 4", "Jinx 5",
         "Jinx 6", "Jinx 7", "Jinx 8", "Jinx 9", "Jinx 10",
         "Jinx 11", "Jinx 12", "Jinx 13"]
    )

    jinx.add_locations(jinx_locs, ClimbLocation)

    lux_locs = get_location_names_with_ids(
        ["Lux 1", "Lux 2", "Lux 3", "Lux 4", "Lux 5",
         "Lux 6", "Lux 7", "Lux 8", "Lux 9", "Lux 10",
         "Lux 11", "Lux 12", "Lux 13"]
    )

    lux.add_locations(lux_locs, ClimbLocation)

    samira_locs = get_location_names_with_ids(
        ["Samira 1", "Samira 2", "Samira 3", "Samira 4", "Samira 5",
         "Samira 6", "Samira 7", "Samira 8", "Samira 9", "Samira 10",
         "Samira 11", "Samira 12", "Samira 13"]
    )

    samira.add_locations(samira_locs, ClimbLocation)

    senna_locs = get_location_names_with_ids(
        ["Senna 1", "Senna 2", "Senna 3", "Senna 4", "Senna 5",
         "Senna 6", "Senna 7", "Senna 8", "Senna 9", "Senna 10",
         "Senna 11", "Senna 12", "Senna 13"]
    )

    senna.add_locations(senna_locs, ClimbLocation)

    sett_locs = get_location_names_with_ids(
        ["Sett 1", "Sett 2", "Sett 3", "Sett 4", "Sett 5",
         "Sett 6", "Sett 7", "Sett 8", "Sett 9", "Sett 10",
         "Sett 11", "Sett 12", "Sett 13"]
    )

    sett.add_locations(sett_locs, ClimbLocation)

    teemo_locs = get_location_names_with_ids(
        ["Teemo 1", "Teemo 2", "Teemo 3", "Teemo 4", "Teemo 5",
         "Teemo 6", "Teemo 7", "Teemo 8", "Teemo 9", "Teemo 10",
         "Teemo 11", "Teemo 12", "Teemo 13"]
    )

    teemo.add_locations(teemo_locs, ClimbLocation)

    thresh_locs = get_location_names_with_ids(
        ["Thresh 1", "Thresh 2", "Thresh 3", "Thresh 4", "Thresh 5",
         "Thresh 6", "Thresh 7", "Thresh 8", "Thresh 9", "Thresh 10",
         "Thresh 11", "Thresh 12", "Thresh 13"]
    )

    thresh.add_locations(thresh_locs, ClimbLocation)

    vi_locs = get_location_names_with_ids(
        ["Vi 1", "Vi 2", "Vi 3", "Vi 4", "Vi 5",
         "Vi 6", "Vi 7", "Vi 8", "Vi 9", "Vi 10",
         "Vi 11", "Vi 12", "Vi 13"]
    )

    vi.add_locations(vi_locs, ClimbLocation)

    warwick_locs = get_location_names_with_ids(
        ["Warwick 1", "Warwick 2", "Warwick 3", "Warwick 4", "Warwick 5",
         "Warwick 6", "Warwick 7", "Warwick 8", "Warwick 9", "Warwick 10",
         "Warwick 11", "Warwick 12", "Warwick 13"]
    )

    warwick.add_locations(warwick_locs, ClimbLocation)

    yasuo_locs = get_location_names_with_ids(
        ["Yasuo 1", "Yasuo 2", "Yasuo 3", "Yasuo 4", "Yasuo 5",
         "Yasuo 6", "Yasuo 7", "Yasuo 8", "Yasuo 9", "Yasuo 10",
         "Yasuo 11", "Yasuo 12", "Yasuo 13"]
    )

    yasuo.add_locations(yasuo_locs, ClimbLocation)

def create_events(world: ClimbWorld) -> None:
    starter = world.get_region("Starter")

    starter_locs = get_location_names_with_ids(
        ["Starting Champion 1", "Starting Champion 2", "Starting Fuse"]
    )

    starter.add_locations(starter_locs, ClimbLocation)