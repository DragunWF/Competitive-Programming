# https://www.codewars.com/kata/536c00e21da4dc0a0700128b/train/python

def get_villain_name(birthdate: str) -> str:
    first = ["The Evil", "The Vile", "The Cruel", "The Trashy", "The Despicable", "The Embarrassing",
             "The Disreputable", "The Atrocious", "The Twirling",  "The Orange", "The Terrifying", "The Awkward"]
    last = ["Mustache", "Pickle", "Hood Ornament", "Raisin", "Recycling Bin",
            "Potato", "Tomato", "House Cat", "Teaspoon", "Laundry Basket"]

    date_values = str(birthdate).split(" ")[0].split("-")
    month = int(date_values[1])
    day = int(date_values[2][-1])
    return f"{first[month - 1]} {last[day]}"
