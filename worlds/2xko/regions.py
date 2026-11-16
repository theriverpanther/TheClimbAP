from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import ClimbWorld

def create_and_connect_regions(world: ClimbWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: ClimbWorld) -> None:
    starter = Region("Starter", world.player, world.multiworld)
    ahri = Region("Ahri", world.player, world.multiworld)
    akali = Region("Akali", world.player, world.multiworld)
    blitzcrank = Region("Blitzcrank", world.player, world.multiworld)
    braum = Region("Braum", world.player, world.multiworld)
    caitlyn = Region("Caitlyn", world.player, world.multiworld)
    darius = Region("Darius", world.player, world.multiworld)
    ekko = Region("Ekko", world.player, world.multiworld)
    illaoi = Region("Ilaoi", world.player, world.multiworld)
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
    starter = world.get_region("Starter")
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

    # TO DO: Make entrances based on the items being in the multiworld
