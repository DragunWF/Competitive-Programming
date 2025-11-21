seats = []

def solve() -> None:
    create_seats()
    while True:
        print_menu()
        choice = input_num("Choice: ")
        if choice == 1:
            assign_a_seat()
        elif choice == 2:
            view_seatings()
        elif choice == 3:
            break
        else:
            print("Input is an invalid choice")


def input_num(input_str: str) -> int:
    try:
        return int(input(input_str))
    except ValueError:
        print("Invalid integer")
        return input_num(input_str)


def print_menu() -> None:
    print("Choice Menu for Airplane: ")
    print("1 - Assign a seat")
    print("2 - View seating chart")
    print("3 - Exit")


def assign_a_seat() -> None:
    ticket_types = {
        "first class": { "min": 1, "max": 2 },
        "economy": { "min": 3, "max": 13 },
        "nonsmoking": { "min": 3, "max": 7 },
        "smoking": { "min": 8, "max": 13 }
    }
    print("Available Ticket Types")
    for ticket in ticket_types:
        if ticket == "smoking" or ticket == "nonsmoking":
            continue
        print(f"- {ticket.title()}")

    while True:
        chosen_ticket_type = input("Ticket type? ").lower().strip()
        if chosen_ticket_type == "first class":
            break
        elif chosen_ticket_type == "economy":
            print("Smoking or nonsmoking?")
            # TODO
        else:
            print("Invalid ticket type!")

    desired_seat = extract_seat()
    rows = {
        "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5
    }
    seats[rows[desired_seat["row"]]][desired_seat["seat"]] = "*"
    # TODO: (incomplete but problem 5 is done)



def view_seatings() -> None:
    print(f'{" " * 6} A B C D E F')
    for i, row in enumerate(seats):
        row_str = " ".join(row)
        row_num = i + 1
        if row_num >= 10:
            print(f"Row {row_num} {row_str}")
            continue
        print(f"Row {row_num}  {row_str}")
    print()  # Spacing


def create_seats() -> None:
    for i in range(13):
        row = []
        for j in range(6):
            row.append("*")
        seats.append(row)


def fill_up_seats() -> None:
    pass


def extract_seat() -> dict:
    desired_seat = input("Desired seat? ")
    valid_seats = "ABCDEF"
    seat_num = ""
    row_letter = ""
    for char in desired_seat:
        if char.isdigit():
            seat_num += char
        else:
            row_letter += char

    if not seat_num or len(row_letter) != 1 or not row_letter.upper() in valid_seats:
        print("Invalid seat!")
        return extract_seat()

    return { "seat": int(seat_num),  "row": row_letter}


if __name__ == "__main__":
    solve()