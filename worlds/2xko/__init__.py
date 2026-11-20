from . import components as components
from typing import Any
from . import items, locations, regions, rules
from collections.abc import Mapping
from BaseClasses import Tutorial
from worlds.AutoWorld import World, WebWorld
from .options import ClimbOptions, option_groups, option_presets

class ClimbWebWorld(WebWorld):
    game = "2XKO - The Climb"

    theme = "partyTime"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to set up 2XKO - The Climb up for a MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["RiverPanther"],
    )

    tutorials = [setup_en]

    option_groups = option_groups
    option_presets = option_presets


class ClimbWorld(World):
    """
    2XKO - The Climb is a fighting game roguelike, where the player fights against AI enemies to reach the end.
    Throughout the game, the player fights bosses in order to gain augments that help them to fight the final boss.
    """
    game = "2XKO - The Climb"

    web = ClimbWebWorld()

    options_dataclass = ClimbOptions
    options: ClimbOptions

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
            "goal_character_count", "ability_sanity", "starting_champions", "starting_fuse", "deathlink"
        )



