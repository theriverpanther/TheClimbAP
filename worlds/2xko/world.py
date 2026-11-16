from collections.abc import Mapping
from typing import Any

from worlds.AutoWorld import World

from . import items, locations, regions, rules, web_world
from . import options as climb_options

class ClimbWorld(World):
    """
    2XKO - The Climb is a fighting game roguelike, where the player fights against AI enemies to reach the end.
    Throughout the game, the player fights bosses in order to gain augments that help them to fight the final boss.
    """
    game = "2XKO - The Climb"

    web = web.world.ClimbWebWorld()

    options_dataclass = climb_options.ClimbOptions
    options: climb_options.ClimbOptions

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    def create_regions(self) -> None:
            regions.create_and_connect_regions(self)
            locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.ClimbItem:
        return items.create_item_with_correct_classification(self,name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict(
            "ascendancy", "ability_sanity", "starting_champion", "starting_fuse"
        )
