# https://www.codewars.com/kata/57c5bc6ec60eb2ce67000076/train/python

def has_permission(user_info: set[str], accessing_data: str) -> bool:
    permissions = {"books": False, "movies": False, "games": False}
    for permission in user_info:
        actions = permission.split("_")
        if actions[0] == "*":
            set_all(permissions, actions[1] == "allow")
        else:
            permissions[actions[0]] = actions[1] == "allow"
    return permissions[accessing_data]


def set_all(permissions: dict, value: bool):
    for key in permissions:
        permissions[key] = value