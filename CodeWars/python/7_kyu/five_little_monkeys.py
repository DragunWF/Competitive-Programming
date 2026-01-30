# https://www.codewars.com/kata/69626db5a27d1aa35aeec789/train/python

# Forgive me for the single letter variables, the kata required
# the byte size of the code to be less than or equal to 450...

def monkeys():
    r=""
    n=("Five","Four","Three","Two","One")
    for i in range(5):
        x=i!=4
        a=f"little monkey{'s'if x else''} jumping on the bed,\n"
        r+=f"{n[i]} {a}"
        r+=f"{n[4]if x else'He'} fell off and bumped his head.\n"
        r+="Mother called the doctor and the doctor said:\n"
        r+="No more monkeys jumping on the bed!\n\n" if x else "Put those monkeys right to bed!"
    return r


def test() -> None:
    print(monkeys())


if __name__ == "__main__":
    test()
