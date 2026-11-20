from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Region
from .items import CHAMPIONS

if TYPE_CHECKING:
    from .__init__ import ClimbWorld

from Utils import visualize_regions

def create_and_connect_regions(world: ClimbWorld) -> None:
    create_all_regions(world)
    connect_regions(world)
    visualize_regions(world.multiworld.get_region("Menu", world.player), "2xko.puml")

def create_all_regions(world: ClimbWorld) -> None:
    starter = Region("Menu", world.player, world.multiworld)
    ahri = Region("Ahri", world.player, world.multiworld)
    akali = Region("Akali", world.player, world.multiworld)
    blitzcrank = Region("Blitzcrank", world.player, world.multiworld)
    braum = Region("Braum", world.player, world.multiworld)
    caitlyn = Region("Caitlyn", world.player, world.multiworld)
    darius = Region("Darius", world.player, world.multiworld)
    ekko = Region("Ekko", world.player, world.multiworld)
    illaoi = Region("Illaoi", world.player, world.multiworld)
    jinx = Region("Jinx", world.player, world.multiworld)
    lux = Region("Lux", world.player, world.multiworld)
    samira = Region("Samira", world.player, world.multiworld)
    senna = Region("Senna", world.player, world.multiworld)
    sett = Region("Sett", world.player, world.multiworld)
    teemo = Region("Teemo", world.player, world.multiworld)
    thresh = Region("Thresh", world.player, world.multiworld)
    vi = Region("Vi", world.player, world.multiworld)
    warwick = Region("Warwick", world.player, world.multiworld)
    yasuo = Region("Yasuo", world.player, world.multiworld)

    regions = [starter,ahri,akali,blitzcrank,braum,caitlyn,darius,ekko,illaoi,jinx,lux,samira,senna,sett,teemo,thresh,vi,warwick,yasuo]

    world.multiworld.regions += regions

def connect_regions(world: ClimbWorld) -> None:
    # Take the isolated regions and actually link them together
    starter = world.get_region("Menu")

    for x in CHAMPIONS:
        champ = world.get_region(x)
        starter.connect(champ, x, lambda state: state.has(x, world.player))
