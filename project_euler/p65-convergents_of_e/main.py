def nth_continued_fraction(sequence: list):
    numerator = 1
    denominator = sequence.pop()
    while len(sequence):
        current_element = sequence.pop()
        numerator = numerator + current_element * denominator
        denominator, numerator = numerator, denominator
    return denominator, numerator


def generate_e_sequence(length):
    seq = [2, 1]
    k = 1
    l = 0
    for _ in range(length - 2):
        if l == 0:
            seq.append(k * 2)
            k += 1
            l += 1
        elif l == 2:
            l = 0
            seq.append(1)
        else:
            l += 1
            seq.append(1)
    return seq


e_sequence = generate_e_sequence(length=100)
numerator, denominator = nth_continued_fraction(e_sequence)
#print(numerator / denominator)
print(f"Sum of digits in the numerator of the 100th convergent of the continued fraction for the euler number: {sum([int(a) for a in str(numerator)])}")
