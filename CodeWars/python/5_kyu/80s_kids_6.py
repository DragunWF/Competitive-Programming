# https://www.codewars.com/kata/566b490c8b164e03f8000002

from collections import deque


def fight(robot_1: dict, robot_2: dict, tactics: dict) -> str:
    # Performance optimizations
    robot_1["tactics"] = deque(robot_1["tactics"])
    robot_2["tactics"] = deque(robot_2["tactics"])

    # Solve Problem
    is_robot_1_turn = robot_1["speed"] >= robot_2["speed"]
    while robot_1["tactics"] or robot_2["tactics"]:
        if is_robot_1_turn:
            damage = tactics[robot_1["tactics"].popleft()] if robot_1["tactics"] else 0
            robot_2["health"] -= damage
            if robot_2["health"] <= 0:
                return f"{robot_1['name']} has won the fight."
        else:
            damage = tactics[robot_2["tactics"].popleft()] if robot_2["tactics"] else 0
            robot_1["health"] -= damage
            if robot_1["health"] <= 0:
                return f"{robot_2['name']} has won the fight."
        is_robot_1_turn = not is_robot_1_turn

    if robot_1["health"] == robot_2["health"]:
        return "The fight was a draw."
    return f"{robot_1['name'] if robot_1['health'] > robot_2['health'] else robot_2['name']} has won the fight."


def test() -> None:
    robot_1 = {
        "name": "Rocky",
        "health": 100,
        "speed": 20,
        "tactics": ["punch", "punch", "laser", "missile"]
    }
    robot_2 = {
        "name": "Missile Bob",
        "health": 100,
        "speed": 21,
        "tactics": ["missile", "missile", "missile", "missile"]
    }
    tactics = {
        "punch": 20,
        "laser": 30,
        "missile": 35
    }
    # Expected: "Missile Bob has won the fight."
    print(fight(robot_1, robot_2, tactics))

    robot_1 = {
        "name": "Rocky",
        "health": 100,
        "speed": 21,
        "tactics": ["space ray"]
    }
    robot_2 = {
        "name": "Missile Bob",
        "health": 100,
        "speed": 21,
        "tactics": ["space ray"]
    }
    tactics = {"space ray": 100}
    # Expected: "Rocky has won the fight."
    print(fight(robot_1, robot_2, tactics))


if __name__ == "__main__":
    test()
