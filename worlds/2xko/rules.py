from __future__ import annotations
from copy import copy

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasFromListUnique, Rule

from .items import CHAMPIONS

if TYPE_CHECKING:
    from .world import ClimbWorld

def set_all_rules(world: ClimbWorld) -> None:
    # Call each logic helper function
    set_all_location_rules(world)
    set_goal_condition(world)

def set_all_location_rules(world: ClimbWorld) -> None:
    for x in CHAMPIONS:
        world.set_rule(world.get_entrance(x), Has(x))


def set_goal_condition(world: ClimbWorld) -> None:
    num_chars = world.options.goal_character_count.value
    temp_chars = copy(CHAMPIONS)
    for x in CHAMPIONS:
        x = x + " Win"

    char_strings = tuple(temp_chars)

    assert num_chars > 0
    world.set_completion_rule(HasFromListUnique(char_strings, count=num_chars))


