from itertools import product
import random


# brute force algorithm
def brute_force(seq1, seq2):
    max = 0
    max_sub = str()
    # Δημιουργία λίστας με όλους τους πιθανούς συνδιασμούς True - False, ώστε να πάρουμε και όλες τις υποακολουθίες της πρώτης ακολουθίας
    true_false_list = [x for x in product([True, False], repeat=len(seq1))]
    for true_false in true_false_list:
        subsequence = str()
        for index, boolean in enumerate(true_false):
            if boolean == True:
                subsequence += seq1[index]
        if len(subsequence) == 0:
            continue
        # Εύρεση της μέγιστης κοινής υποακολουθίας και του μήκους της
        found = 0
        for letter in seq2:
            if letter == subsequence[found]:
                found += 1
            if found == len(subsequence):
                if len(subsequence) > max:
                    max = len(subsequence)
                    max_sub = subsequence
                break

    return max, max_sub


# Κατασκευή τυχαίων ακολουθιών dna
def create_dna_sequense(n, chars, available_chars):
    dna_sequences = list()
    for _ in range(n):
        new_sequence = str()
        for _ in range(chars):
            new_sequence += available_chars[random.randint(0, 3)]
        dna_sequences.append(new_sequence)
    return dna_sequences


# Longest Common Subsequence Algorithm
def lcs(seq1, seq2):
    length_seq1 = len(seq1)
    length_seq2 = len(seq2)
    table = lcs_table(seq1, seq2)
    if length_seq1 == 0 or length_seq2 == 0:
        return str()
    common_subsequnce = str()
    i_index = length_seq1
    j_index = length_seq2
    while i_index >= 0 and j_index >= 0:
        current = table[i_index][j_index]
        up = table[i_index][j_index - 1]
        left = table[i_index - 1][j_index]
        if current > left and current > up:
            common_subsequnce += seq1[i_index - 1]
            i_index -= 1
            j_index -= 1
        elif current == left:
            i_index -= 1
        elif current == up:
            j_index -= 1
    return len(common_subsequnce), common_subsequnce[::-1]


# Δημιουργία του πίνακα του αλγορίθμου lcs
def lcs_table(seq1, seq2):
    length_seq1 = len(seq1)
    length_seq2 = len(seq2)
    value = [[0 for _ in range(length_seq2 + 1)] for _ in range(length_seq1 + 1)]
    for i in range(1, length_seq1 + 1):
        for j in range(1, length_seq2 + 1):
            if seq1[i - 1] == seq2[j - 1]:
                value[i][j] = value[i - 1][j - 1] + 1
            else:
                value[i][j] = max(value[i - 1][j], value[i][j - 1])
    return value
