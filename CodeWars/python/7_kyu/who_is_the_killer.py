# https://www.codewars.com/kata/5f709c8fb0d88300292a7a9d/train/python


def killer(suspect_info, dead):
    for person in suspect_info:
        for dead_person in dead:
            if not dead_person in suspect_info[person]:
                break
        else:
            return person