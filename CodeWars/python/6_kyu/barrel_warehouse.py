# https://www.codewars.com/kata/67f2ef6f7ba2a69a66e3bd68/train/python

def insert_barrels(warehouse: list[str], barrels: list[str]) -> list[str]:
    REQUIRED_SPACE = len(barrels)

    if len(warehouse) == 1 and REQUIRED_SPACE == 1:
        return ["0"]

    min_found_space = None
    min_space_indexes = {"start": None, "end": None}
    space_indexes = {"start": None, "end": None}

    for i, tile in enumerate(warehouse):
        if tile == "0" and not space_indexes["start"] is None:
            space_indexes["end"] = i
            current_hole = space_indexes["end"] - space_indexes["start"]

            if current_hole >= REQUIRED_SPACE and (min_found_space is None or current_hole < min_found_space):
                min_found_space = current_hole
                min_space_indexes = space_indexes.copy()

            space_indexes["start"] = None
            space_indexes["end"] = None
        elif not tile and space_indexes["start"] is None:
            space_indexes["start"] = i

    if not space_indexes["start"] is None:
        end_index = len(warehouse) - 1
        current_hole = (end_index + 1) - space_indexes["start"]
        if current_hole >= REQUIRED_SPACE and (min_found_space is None or current_hole < min_found_space):
            min_found_space = current_hole
            min_space_indexes = {
                "start": space_indexes["start"], "end": end_index
            }

    if min_found_space is None:
        return warehouse

    filled_barrels = 0
    for i in range(min_space_indexes["start"], min_space_indexes["end"] + 1):
        warehouse[i] = "0"
        filled_barrels += 1
        if filled_barrels == REQUIRED_SPACE:
            break

    return warehouse


def test() -> None:
    # print(insert_barrels(['0', '', '', '0', '', '', '', '0'], ['0', '0']))
    # print(insert_barrels(['', '', '', '0', '', ''], ['0', '0']))
    print(insert_barrels(['0', '0', '', '', '', '0', '0', '0', ''], ['0']))
    # print(insert_barrels(['0', '0', '', '', '0', '', '', '', '0'], ['0']))
    # print(insert_barrels(['', '', '0', '0', '', '', '', '', '0'], ['0', '0', '0']))
    print(insert_barrels(["0", "0", ""], "0"))


if __name__ == "__main__":
    test()


# def insert_barrels_old(warehouse: list[str], barrels: list[str]) -> list[str]:
#     # Old Solution - Do not use
#     current_hole = 0
#     start_hole_index, end_hole_index = None, None
#     min_hole_start_index = None
#     min_found_space = None
#     required_space = len(barrels)

#     for i, tile in enumerate(warehouse):
#         if tile == "0":
#             if current_hole >= required_space and (min_found_space is None or current_hole < min_found_space):
#                 min_found_space = current_hole
#                 min_hole_start_index = start_hole_index
#                 end_hole_index = i
#             current_hole = 0
#         else:
#             if current_hole == 0:
#                 start_hole_index = i
#             current_hole += 1

#     if current_hole > 0 and (min_found_space is None or current_hole < min_found_space):
#         min_hole_start_index = start_hole_index
#         end_hole_index = len(warehouse) - 1

#     if min_found_space is None:
#         return warehouse

#     filled_barrels = 0
#     for i in range(min_hole_start_index, end_hole_index + 1):
#         warehouse[i] = '0'
#         filled_barrels += 1
#         if filled_barrels >= required_space:
#             break
#     return warehouse
