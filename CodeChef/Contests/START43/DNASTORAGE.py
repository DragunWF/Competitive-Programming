t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    replacements = {"00": "A", "01": "T", "10": "C", "11": "G"}
    output = ""
    sequence = ""
    for j in range(n):
        sequence += s[j]
        if (j + 1) % 2 == 0:
            output += replacements[sequence]
            sequence = ""
    print(output)
