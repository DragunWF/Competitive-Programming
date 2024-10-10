# https://www.codewars.com/kata/569d488d61b812a0f7000015/train/python

def data_reverse(data):
    output, byte = [], ""
    data = "".join([str(n) for n in data])
    for i in range(len(data)):
        byte += data[i]
        if (i + 1) % 8 == 0:
            output.append(byte)
            byte = ""
    output.reverse()
    return [int(n) for n in "".join(output)]
