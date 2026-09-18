# https://www.codewars.com/kata/6aa8e25b5ae7dfbbe29e8fb8/train/python

# from preloaded import fuel_map
fuel_map = {
    "Asteroid": 1,
    "Mercury": 2,
    "Venus": 4,
    "Mars": 3,
    "Jupiter": 12,
    "Saturn": 11,
    "Uranus": 8,
    "Neptune": 7
}


def successful_mission(solar_system: list[str], destination_planet: str, fuel: int) -> bool:
    earth_index, target_index = get_indicies(solar_system, destination_planet)
    cost = 0
    if target_index > earth_index:
        for i in range(earth_index + 1, target_index):
            cost += fuel_map[solar_system[i]]
    else:
        for i in range(earth_index - 1, target_index, -1):
            cost += fuel_map[solar_system[i]]
    cost += fuel_map[solar_system[target_index]] * 2
    return fuel >= cost


def get_indicies(solar_system: list[str], target_planet: str) -> tuple[int]:
    earth_index = -1
    target_index = -1
    for i, item in enumerate(solar_system):
        if item == "Earth":
            earth_index = i
        elif item == target_planet:
            target_index = i
    return (earth_index, target_index)


def test() -> None:
    planets = ["Mercury", "Asteroid", "Earth", "Asteroid", "Saturn", "Venus", "Neptune", "Asteroid"]
    # Expected: True
    print(successful_mission(planets, "Neptune", 33))


if __name__ == "__main__":
    test()
