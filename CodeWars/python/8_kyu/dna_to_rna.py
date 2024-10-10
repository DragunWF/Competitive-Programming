# https://www.codewars.com/kata/5556282156230d0e5e000089

def dna_to_rna(dna):
    output = ""
    for x in dna:
        output += x if x != "T" else "U"
    return output
