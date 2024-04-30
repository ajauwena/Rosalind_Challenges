# --- DNA Nucleotide Counter ---

#region: Function 1

# Create a function that takes in the all-uppercase sequence returned by Function 1.
def nuc_freq_counter(temp_seq):
    # Create a dictionary with nucleotides as keys (in the order "A," "C," "G," and "T") and 0s as values.
    temp_freq_dict = {"A": 0, "C": 0, "G": 0, "T": 0}
    # Iterate through every nucleotide in the all-uppercase sequence.
    for nuc in temp_seq:
        # Add the frequency of the corresponding nucleotide to the dictionary.
        temp_freq_dict[nuc] += 1
    # Return the dictionary, which now includes the frequency count of each nucleotide.
    return temp_freq_dict

#endregion

#region: Main

# Create a DNA sequence "seq".
seq = "ACCTACCCATTAGTATAGCAAACACCACCGTGAGTTTAGAAGAAGGCCTATCCTAGTTAAAGAACAATGGCGTGCCGGTCATTGTCTCCGTGGACCGTTACCTATAAATGTCCAGCATAGTCTAGCAGGGGCTTGGAGAGTGGTAGACCTCAGATACTCATCATGACTTGACCTTGAACGGCTAAAGAAACATCGCGGCCGGAGAGCTGAATCCCAGTGGACTGGATCCGCTACAGTCCCCGCACAGGGGTGTGCAGCTTTGTGCAGCGTTGTCCTGTCTATCTACACTTCGTCGATTAATCCTGCATCGAACCTGCGACTGTTCTCCGCGCCTGATGGAGGGCGAATGGGCGGCCTTTCTCAAGCCCGCTGTCACTGACACTTTACAATCCGTATCCCAAAACCCTGATGGTGCTTAATGCACACGCGGGTTGTTACATTATTGCAATAGATCATCCGTTCGGTGAAACTTCAGTAGCAAAGGCAGGCTTTCTCACAAATCTTGGCTGTAATTTAAGCAAGCGATCGATATGCTTGAAGTCCTTCCGACTGATTATCCTTCCTCTACACCGGGCTTAGATGTTGCTGCCACACTACATCGAGTAGGATTGACTGCATAAACCAAGTGCTGGACACATAGGTTCATTCATAGGCAAGTCAGTGTGACTTTAGGCTGGGGTGAGGGACCCGCGCTAACGGTAACTGTCCGGTTCACTGACTAGACGTCCGCCTGGGTGTGCCTTTTCGAGGCCGAGGATATCCCGGTTTCTTGGCACCATGGTCATCCGTCAGTCCCCTTATACCCCGAAGTTCGGGAGTCCATCTCTTCGTCGCACCCTTGCTTGACCGTATTGCAGCATGGGCACGACTCTTGCAGCATCTGAT"

# Create a dictionary "dict_nuc_and_freq" with nucleotides as keys and their frequencies as values.
dict_nuc_and_freq = nuc_freq_counter(seq)

# Create a list "list_nuc_and_freq" containing only the values of the dictionary created above.
list_nuc_and_freq = [str(val) for key, val in dict_nuc_and_freq.items()]

# Concatenate the elements of the list "list_nuc_and_freq" into a single string and print it.
print(" ".join([str(val) for key, val in dict_nuc_and_freq.items()]))

# The result (202, 236, 218, 229) is correct and we got an achievement!

#endregion