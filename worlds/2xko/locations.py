from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from world import ClimbWorld

LOCATION_NAME_TO_ID = {
    # TO DO, determine how checks are hashed out (per character per progression, per node, etc)
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
    ahri

def create_events(world: ClimbWorld) -> None:
