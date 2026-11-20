from __future__ import annotations
from copy import copy

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has
from worlds.AutoWorld import CollectionState

from .items import CHAMPIONS

if TYPE_CHECKING:
    from .__init__ import ClimbWorld

def set_all_rules(world: ClimbWorld) -> None:
    # Call each logic helper function
    set_all_location_rules(world)
    set_goal_condition(world)

def set_all_location_rules(world: ClimbWorld) -> None:
    # for champ in CHAMPIONS:
        # region = world.get_region(champ)
        # for loc in region.locations:
            # world.set_rule(loc, Has(champ, 1))
    print ("meh")

def set_goal_condition(world: ClimbWorld) -> None:
    num_chars = world.options.goal_character_count.value

    assert num_chars > 0
    world.set_completion_rule(Has("Win", num_chars))


