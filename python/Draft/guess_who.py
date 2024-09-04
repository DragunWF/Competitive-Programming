# https://www.codewars.com/kata/58b2c5de4cf8b90723000051

class GuessWho():
    def __init__(self, character):
        self.characteristic = [["Jean-Claude", ["Male", "Glasses", "Brown eyes", "Bald", "White hair", "Small mouth", "Small nose"]],
                               ["Pierre", ["Male", "Mustache", "Brown eyes",
                                           "Brown hair", "Big mouth", "Small nose"]],
                               ["Jean", ["Male", "White hair",
                                         "Big nose", "Big mouth", "Blue eyes"]],
                               ["Amelie", ["Female", "Hat", "Brown hair", "Small mouth",
                                           "Long hair", "Brown eyes", "Small nose"]],
                               ["Mirabelle", ["Female", "Black hair", "Earrings",
                                              "Small mouth", "Brown eyes", "Big nose"]],
                               ["Isabelle", ["Female", "Blonde hair", "Glasses",
                                             "Hat", "Small mouth", "Small nose", "Brown eyes"]],
                               ["Antonin", ["Male", "Brown eyes",
                                            "Black hair", "Small nose", "Big mouth"]],
                               ["Bernard", ["Male", "Brown eyes",
                                            "Brown hair", "Small nose", "Hat"]],
                               ["Owen", ["Male", "Blue eyes", "Blonde hair",
                                         "Small nose", "Small mouth"]],
                               ["Dylan", ["Male", "Brown eyes", "Blonde hair",
                                          "Small nose", "Small mouth", "Bald", "Beard"]],
                               ["Herbert", ["Male", "Brown eyes", "Blonde hair",
                                            "Big nose", "Small mouth", "Bald"]],
                               ["Christine", ["Female", "Blue eyes", "Blonde hair",
                                              "Small nose", "Small mouth", "Long hair"]],
                               ["Luc", ["Male", "Brown eyes", "White hair",
                                        "Small nose", "Small mouth", "Glasses"]],
                               ["Cecilian", ["Male", "Brown eyes",
                                             "Ginger hair", "Small nose", "Small mouth"]],
                               ["Lionel", ["Male", "Brown eyes", "Brown hair",
                                           "Big nose", "Big mouth", "Mustache"]],
                               ["Benoit", ["Male", "Brown eyes", "Brown hair",
                                           "Small mouth", "Small nose", "Mustache", "Beard"]],
                               ["Robert", ["Male", "Blue eyes",
                                           "Brown hair", "Big nose", "Big mouth"]],
                               ["Charline", ["Female", "Brown hair",
                                             "White hair", "Small nose", "Big mouth"]],
                               ["Renaud", ["Male", "Brown eyes", "Blonde hair",
                                           "Small nose", "Big mouth", "Mustache"]],
                               ["Michel", ["Male", "Brown eyes", "Blonde hair",
                                           "Small nose", "Big mouth", "Beard"]],
                               ["Pierre-Louis", ["Male", "Blue eyes", "Brown hair",
                                                 "Small nose", "Small mouth", "Bald", "Glasses"]],
                               ["Etienne", ["Male", "Brown eyes", "Blonde hair",
                                            "Small nose", "Small mouth", "Glasses"]],
                               ["Henri", ["Male", "Brown eyes", "White hair",
                                          "Small nose", "Big mouth", "Hat"]],
                               ["Damien", ["Male", "Brown eyes", "Blonde hair", "Small nose", "Big mouth", "Hat"]]]
        self.character = character
        self.target_traits = ""
        self.turns = 0

    def guess(self, guess: str) -> list[str]:
        self.turns += 1
        if guess == self.character:
            return [f"Correct! in {self.turns} turns"]
        suspects = []
        has_trait = guess in self.target_traits
        for character, traits in self.characteristic:
            if has_trait and guess in traits:
                suspects.append(character)
            elif not has_trait and not guess in traits:
                suspects.append(character)
        return suspects

    def get_traits(self) -> list[str]:
        for character, traits in self.characteristic:
            if character == self.character:
                return traits


def test():
    # Not part of the solution, just testing
    game = GuessWho("Amelie")
    print(game.guess("Male"))
    print(game.guess("Hat"))
    print(game.guess("Isabelle"))


if __name__ == "__main__":
    test()
