from worlds.LauncherComponents import Component, Type, components, launch

def run_client(*args: str) -> None:
    # from .client.launch import launch_climb_client
    # Just copying as reference from the APQuest directory.
    # Will look into direct launch if it's a desired feature.
    print("client launch enter")

components.append(
    Component(
        "2XKO - The Climb Client",
        func=run_client,
        game_name="2XKO - The Climb",
        component_type=Type.CLIENT,
        supports_uri=True,
    )
)

