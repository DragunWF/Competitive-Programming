# https://www.codewars.com/kata/54dba07f03e88a4cec000caf/train/python

class Dog():
  def __init__(self, breed):
    self.breed = breed

snoopy = Dog("Beagle")
snoopy.bark = lambda: "Woof"
scoobydoo = Dog("Great Dane")
scoobydoo.bark = lambda: "Woof"