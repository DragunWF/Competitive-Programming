# https://www.codewars.com/kata/58bee820e9f98b215200007c/train/python

def select(memory: str) -> str:
    people = [person.strip() for person in memory.split(", ")]
    hated_people = set()
    is_contagion = False
    get_name = lambda name: name if not name.startswith("!") else name[1:]
    for person in people:
        is_hated = person.startswith("!")
        person = get_name(person)
        if is_hated or is_contagion:
            hated_people.add(person)
        is_contagion = is_hated
    return ", ".join([get_name(person) for person in people if not get_name(person) in hated_people])


def test():
    print(select("Jesse Cox, !Selena Gomez"))  # 'Jesse Cox'


if __name__ == "__main__":
    test()

# def select(memory: str) -> str:
#     people = memory.split(", ")
#     modified_memory = []
#     hated_people = set()
#     is_contaminated = False
#     for person in people:
#         person = person.strip()
#         if person in hated_people:
#             is_contaminated = False
#             continue
#         if person.startswith("!") or is_contaminated:
#             hated_people.add(person[1:] if person.startswith("!") else person)
#             is_contaminated = person.startswith("!")
#             continue
#         is_contaminated = False
#         modified_memory.append(person)
#     return ", ".join(modified_memory)
